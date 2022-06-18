import { DynamicModule, LoggerService, Module } from '@nestjs/common';
import { GraphQLModule } from '@nestjs/graphql';
import { ApolloDriver, ApolloDriverAsyncConfig, ApolloDriverConfig } from '@nestjs/apollo';
import { ConfigModule, ConfigService } from '@nestjs/config';
import { SchemaService } from './schema.service';
import { DeepthoughtConfiguration } from '../app/config';

@Module({
  imports: [
    GraphQLModule.forRootAsync<ApolloDriverConfig>({
      driver: ApolloDriver,
      imports: [ConfigModule],
      useFactory: async (configService: ConfigService<DeepthoughtConfiguration>) => ({
        typePaths: configService
      }),
      inject: [ConfigService]
    }),
  ],
  providers: [
    SchemaService
  ],
})
export class SchemaModule {
}
