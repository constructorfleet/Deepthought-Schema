import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { AppService } from './app.service';

import { readFileSync } from 'fs';
import * as yaml from 'js-yaml';
import { join } from 'path';
import { LoggerModule } from './logging/log.module';
import { DeepthoughtConfiguration, YAML_CONFIG_FILENAME } from './config';
import { SchemaService } from './schema/schema.service';



const configuration = () => {
  return yaml.load(
    readFileSync(YAML_CONFIG_FILENAME, 'utf8'),
  ) as DeepthoughtConfiguration;
};

@Module({
  imports: [
    LoggerModule,
    ConfigModule.forRoot({
      isGlobal: true,
      load: [configuration],
    }),
  ],
  providers: [
    AppService,
    SchemaService,
  ],
})
export class AppModule {
}
