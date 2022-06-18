import { Module } from '@nestjs/common';
import { GraphQLModule } from '@nestjs/graphql';
import { ApolloDriver, ApolloDriverConfig } from '@nestjs/apollo';
import { ConfigService } from '@nestjs/config';
import { SchemaService } from './schema.service';
import { ASSET_DIRECTORY, DeepthoughtConfiguration } from '../app/config';
import { LoggerModule } from '../logging/log.module';
import { join } from 'path';

@Module({
  imports: [
    LoggerModule,
    GraphQLModule.forRootAsync<ApolloDriverConfig>({
      driver: ApolloDriver,
      useFactory: async (configService: ConfigService<DeepthoughtConfiguration>) => ({
        typePaths: [join(ASSET_DIRECTORY, configService.get<string>('graphql.typeDirectory') || '', '*.graphql')]
      }),
      inject: [ConfigService]
    }),
  ],
  providers: [
    SchemaService
  ],
  exports: [
    GraphQLModule,
    SchemaService
  ]
})
export class SchemaModule {
}
