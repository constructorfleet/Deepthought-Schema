import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { AppService } from './app.service';

import { readFileSync } from 'fs';
import * as yaml from 'js-yaml';
import { join } from 'path';
import { LoggerModule } from './logging/log.module';

const YAML_CONFIG_FILENAME = 'config.yaml';

const configuration = () => {
  return yaml.load(
    readFileSync(join(__dirname, YAML_CONFIG_FILENAME), 'utf8'),
  ) as Record<string, any>;
};

@Module({
  imports: [
    LoggerModule,
    ConfigModule.forRoot({
      isGlobal: true,
      envFilePath: [
        '.env',
      ],
      load: [configuration],
    }),
  ],
  providers: [
    AppService,
  ],
})
export class AppModule {
}
