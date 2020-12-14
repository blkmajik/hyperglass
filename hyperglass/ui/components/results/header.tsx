import { useMemo } from 'react';
import { AccordionIcon, Box, Spinner, HStack, Text, Tooltip } from '@chakra-ui/react';
import { BisError as Warning } from '@meronex/icons/bi';
import { FaCheckCircle as Check } from '@meronex/icons/fa';
import { useConfig, useColorValue } from '~/context';
import { useStrf } from '~/hooks';

import type { TResultHeader } from './types';

const runtimeText = (runtime: number, text: string): string => {
  let unit = 'seconds';
  if (runtime === 1) {
    unit = 'second';
  }
  return `${text} ${unit}`;
};

export const ResultHeader = (props: TResultHeader) => {
  const { title, loading, isError, errorMsg, errorLevel, runtime } = props;

  const status = useColorValue('primary.500', 'primary.300');
  const warning = useColorValue(`${errorLevel}.500`, `${errorLevel}.300`);
  const defaultStatus = useColorValue('success.500', 'success.300');

  const { web } = useConfig();
  const text = useStrf(web.text.complete_time, { seconds: runtime }, [runtime]);
  const label = useMemo(() => runtimeText(runtime, text), [runtime]);

  return (
    <HStack alignItems="center" w="100%">
      <Tooltip
        hasArrow
        placement="top"
        isDisabled={loading}
        label={isError ? errorMsg : label}
        colorScheme={isError ? errorLevel : 'success'}>
        {loading ? (
          <Spinner size="sm" mr={4} color={status} />
        ) : (
          <Box
            as={isError ? Warning : Check}
            color={isError ? warning : defaultStatus}
            mr={4}
            boxSize={6}
          />
        )}
      </Tooltip>

      <Text fontSize="lg">{title}</Text>
      <AccordionIcon ml="auto" />
    </HStack>
  );
};
