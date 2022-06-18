import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { GraphQLModule } from '@nestjs/graphql';
import { ApolloDriver, ApolloDriverAsyncConfig } from '@nestjs/apollo';
import { AppService } from './app.service';

import { readFileSync } from 'fs';
import * as yaml from 'js-yaml';
import { LoggerModule } from '../logging/log.module';
import { DeepthoughtConfiguration, YAML_CONFIG_FILENAME } from './config';
import { SchemaService } from '../schema/schema.service';
import { SchemaModule } from '../schema/schema.module';

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
    SchemaModule,
  ],
  providers: [
    AppService,
  ],
  exports: [
    LoggerModule,
    ConfigModule,
    SchemaModule
  ],
})
export class AppModule {
}
