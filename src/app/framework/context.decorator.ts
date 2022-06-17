import { SetMetadata } from '@nestjs/common';

export const CONTEXT_METADATA_KEY = 'ContextName';

export const WithContext = (name: string) => SetMetadata(CONTEXT_METADATA_KEY, name);
