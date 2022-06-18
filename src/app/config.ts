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

export interface DeepthoughtConfiguration extends ConfigObject {
  graphql: {
    typeDirectory: string;
  };
  apollo: {
    driver: "federated" | "base";
    enablePlayground: boolean;
    debugMode: boolean;
  };
}
