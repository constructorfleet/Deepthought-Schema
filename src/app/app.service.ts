import { Injectable } from '@nestjs/common';
import { ContextService } from './framework/context.service';
import { Reflector } from '@nestjs/core';
import { LoggerService } from './logging/log.service';
import { WithContext } from './framework/context.decorator';

@Injectable()
@WithContext("ApplicationService")
export class AppService extends ContextService {
  constructor(
    reflector: Reflector,
    logger: LoggerService,
  ) {
    super(
      reflector,
      logger,
    );
  }
}
