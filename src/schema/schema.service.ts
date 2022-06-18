import { WithLoggingContext } from '../logging/context/loggingcontext.decorator';
import { Injectable } from '@nestjs/common';
import { LoggingContextService } from '../logging/context/loggingContextService';
import { Reflector } from '@nestjs/core';
import { LoggerService } from '../logging/log.service';
import { ConfigService } from '@nestjs/config';
import { DeepthoughtConfiguration } from '../app/config';

import { loadSchema as SchemaLoader } from '@graphql-tools/load';
import { makeExecutableSchema } from '@graphql-tools/schema';
import { constraintDirective } from 'graphql-constraint-directive';
import { join } from 'path';
import { GraphQLSchema } from 'graphql';
import { GraphQLFileLoader } from '@graphql-tools/graphql-file-loader';

export type SchemaLoadResult = 'SUCCESS' | 'FAILURE';

@WithLoggingContext('SchemaService')
@Injectable()
export class SchemaService extends LoggingContextService {
  private readonly schemaDirectory: string;
  private _gqlSchema?: GraphQLSchema;

  constructor(
    private readonly configService: ConfigService<DeepthoughtConfiguration>,
    reflector: Reflector,
    logger: LoggerService,
  ) {
    super(
      reflector,
      logger,
    );
    this.schemaDirectory = configService.getOrThrow<string>(
      'schema.directory',
      {
        infer: true
      }
    );
  }

  async loadTypes(): Promise<SchemaLoadResult> {
    try {
      const schema: GraphQLSchema | null = await SchemaLoader(
        join(
          this.schemaDirectory,
          '**',
          '*.graphql',
        ),
        {
          loaders: [
            new GraphQLFileLoader(),
          ],
        });
      if (!schema) {
        this.logger.warn(
          'Null Schema Loaded'
        );
        return 'FAILURE';
      }
      this._gqlSchema =
        constraintDirective()(
          makeExecutableSchema(
            {
              typeDefs: schema,
            },
          ),
        );
      return this._gqlSchema ? 'SUCCESS' : 'FAILURE';
    } catch (e) {
      this.logger.error(
        'Error Loading Schema',
        this.schemaDirectory,
        e
      );
      return 'FAILURE';
    }
  }
}
