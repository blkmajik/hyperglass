<div align="center">
  <br/>
  <img src="https://res.cloudinary.com/hyperglass/image/upload/v1593916013/logo-light.svg" width=300></img>
  <br/>
  <h3>The network looking glass that tries to make the internet better.</h3>
  <br/>  
  A looking glass is implemented by network operators as a way of providing customers, peers, or the general public with a way to easily view elements of, or run tests from the provider's network.
</div>

<hr/>

<div align="center">

[**Documentation**](https://hyperglass.dev)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[**Live Demo**](https://demo.hyperglass.dev/)

[![PyPI](https://img.shields.io/pypi/v/hyperglass?style=for-the-badge)](https://pypi.org/project/hyperglass/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/hyperglass?color=%2340798C&style=for-the-badge)
[![GitHub Contributors](https://img.shields.io/github/contributors/thatmattlove/hyperglass?color=40798C&style=for-the-badge)](https://github.com/thatmattlove/hyperglass)

[![Frontend Tests](https://img.shields.io/github/workflow/status/thatmattlove/hyperglass/Frontend%20Testing?label=Frontend%20Tests&style=for-the-badge)](https://github.com/thatmattlove/hyperglass/actions?query=workflow%3A%Frontend+Testing%22)
[![Backend Tests](https://img.shields.io/github/workflow/status/thatmattlove/hyperglass/Backend%20Testing?label=Backend%20Tests&style=for-the-badge)](https://github.com/thatmattlove/hyperglass/actions?query=workflow%3A%Backend+Testing%22)
[![Installer Tests](https://img.shields.io/github/workflow/status/thatmattlove/hyperglass/Installer%20Testing?label=Installer%20Tests&style=for-the-badge)](https://github.com/thatmattlove/hyperglass/actions?query=workflow%3A%Installer+Testing%22)

<br/>

hyperglass is intended to make implementing a looking glass too easy not to do, with the lofty goal of improving the internet community at large by making looking glasses more common across autonomous systems of any size.

</div>

### [Changelog](https://github.com/thatmattlove/hyperglass/blob/v1.0.0/CHANGELOG.md)

## Features

- BGP Route, BGP Community, BGP AS Path, Ping, & Traceroute
- Full IPv6 support
- Customizable everything: features, theme, UI/API text, error messages, commands
- Built in support for:
    - Arista EOS
    - BIRD
    - Cisco IOS-XR
    - Cisco IOS/IOS-XE
    - Cisco NX-OS
    - FRRouting
    - Huawei
    - Juniper JunOS
    - Mikrotik
    - Nokia SR OS
    - TNSR
    - VyOS
- Configurable support for any other [supported platform](https://hyperglass.dev/docs/platforms)
- Optionally access devices via an SSH proxy/jump server
- VRF support
- Access List/prefix-list style query control to whitelist or blacklist query targets on a per-VRF basis
- REST API with automatic, configurable OpenAPI documentation
- Modern, responsive UI built on [ReactJS](https://reactjs.org/), with [NextJS](https://nextjs.org/) & [Chakra UI](https://chakra-ui.com/), written in [TypeScript](https://www.typescriptlang.org/)
- Query multiple devices simultaneously
- Browser-based DNS-over-HTTPS resolution of FQDN queries

*To request support for a specific platform, please [submit a Github Issue](https://github.com/thatmattlove/hyperglass/issues/new) with the **feature** label.*

### [Get Started →](https://hyperglass.dev/docs/introduction)

## Community

- [Slack](https://netdev.chat/)
- [Telegram](https://t.me/hyperglasslg)

Any users, potential users, or contributors of hyperglass are welcome to join and discuss usage, feature requests, bugs, and other things.

**hyperglass is developed with the express intention of being free to the networking community**.

*However, if you're feeling particularly helpful or generous, small donations are welcome.*

[![Donate](https://img.shields.io/badge/Donate-blue.svg?logo=paypal&style=for-the-badge)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=ZQFH3BB2B5M3E&source=url)

## Acknowledgements

hyperglass is built entirely on open-source software. Here are some of the awesome libraries used, check them out too!

- [FastAPI](https://fastapi.tiangolo.com/)
- [Netmiko](https://github.com/ktbyers/netmiko)
- [Scrapli](https://github.com/carlmontanari/scrapli)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Chakra UI](https://chakra-ui.com/)

[![GitHub](https://img.shields.io/github/license/thatmattlove/hyperglass?color=330036&style=for-the-badge)](https://github.com/thatmattlove/hyperglass/blob/v1.0.0/LICENSE)
