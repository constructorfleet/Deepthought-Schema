import { ConfigObject } from '@nestjs/config';
import { join, resolve } from 'path';

export const ASSET_DIRECTORY = resolve(
  join(
    'dist',
    'assets',
  ),
);

export const YAML_CONFIG_FILENAME = join(
  ASSET_DIRECTORY,
  'config.yaml',
);

console.log(ASSET_DIRECTORY);
console.log(YAML_CONFIG_FILENAME);

export interface DeepthoughtConfiguration extends ConfigObject {
  schema: {
    directory: string,
  };
}
