"""Device-Agnostic Parsed Response Data Model."""

# Standard Library
import re
from typing import List, Literal
from ipaddress import ip_network

# Third Party
from pydantic import StrictInt, StrictStr, StrictBool, validator

# Project
from hyperglass.configuration import params
from hyperglass.external.rpki import rpki_state

# Local
from ..main import HyperglassModel

WinningWeight = Literal["low", "high"]


class BGPRoute(HyperglassModel):
    """Post-parsed BGP route."""

    prefix: StrictStr
    active: StrictBool
    age: StrictInt
    weight: StrictInt
    med: StrictInt
    local_preference: StrictInt
    as_path: List[StrictInt]
    communities: List[StrictStr]
    next_hop: StrictStr
    source_as: StrictInt
    source_rid: StrictStr
    peer_rid: StrictStr
    rpki_state: StrictInt

    @validator("communities")
    def validate_communities(cls, value):
        """Filter returned communities against configured policy.

        Actions:
            permit: only permit matches
            deny: only deny matches
        """

        def _permit(comm):
            """Only allow matching patterns."""
            valid = False
            for pattern in params.structured.communities.items:
                if re.match(pattern, comm):
                    valid = True
                    break
            return valid

        def _deny(comm):
            """Allow any except matching patterns."""
            valid = True
            for pattern in params.structured.communities.items:
                if re.match(pattern, comm):
                    valid = False
                    break
            return valid

        func_map = {"permit": _permit, "deny": _deny}
        func = func_map[params.structured.communities.mode]

        return [c for c in value if func(c)]

    @validator("rpki_state")
    def validate_rpki_state(cls, value, values):
        """If external RPKI validation is enabled, get validation state."""

        if params.structured.rpki.mode == "router":
            # If router validation is enabled, return the value as-is.
            return value

        elif params.structured.rpki.mode == "external":
            # If external validation is enabled, validate the prefix
            # & asn with Cloudflare's RPKI API.
            as_path = values["as_path"]

            if len(as_path) == 0:
                # If the AS_PATH length is 0, i.e. for an internal route,
                # return RPKI Unknown state.
                return 3
            else:
                # Get last ASN in path
                asn = as_path[-1]

        try:
            net = ip_network(values["prefix"])
        except ValueError:
            return 3

        # Only do external RPKI lookups for global prefixes.
        if net.is_global:
            return rpki_state(prefix=values["prefix"], asn=asn)
        else:
            return value


class BGPRouteTable(HyperglassModel):
    """Post-parsed BGP route table."""

    vrf: StrictStr
    count: StrictInt = 0
    routes: List[BGPRoute]
    winning_weight: WinningWeight

    def __init__(self, **kwargs):
        """Sort routes by prefix after validation."""
        super().__init__(**kwargs)
        self.routes = sorted(self.routes, key=lambda r: r.prefix)

    def __add__(self: "BGPRouteTable", other: "BGPRouteTable") -> "BGPRouteTable":
        """Merge another BGP table instance with this instance."""
        if isinstance(other, BGPRouteTable):
            self.routes = sorted([*self.routes, *other.routes], key=lambda r: r.prefix)
            self.count = len(self.routes)
        return self