import { SetMetadata } from '@nestjs/common';

export const LOGGING_CONTEXT_METADATA_KEY = 'LoggingContextName';

export const WithLoggingContext = (name: string) =>
  SetMetadata(LOGGING_CONTEXT_METADATA_KEY, name);
