import { WithContext } from '../framework/context.decorator';
import { Injectable } from '@nestjs/common';
import { ContextService } from '../framework/context.service';
import { Reflector } from '@nestjs/core';
import { LoggerService } from '../logging/log.service';
import { ConfigService } from '@nestjs/config';
import { DeepthoughtConfiguration } from '../config';

@WithContext('SchemaService')
@Injectable()
export class SchemaService extends ContextService {
  private readonly schemaDirectory: string;
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
}
