import { Injectable } from '@nestjs/common';
import { LoggingContextService } from '../logging/context/loggingContextService';
import { Reflector } from '@nestjs/core';
import { LoggerService } from '../logging/log.service';
import { WithLoggingContext } from '../logging/context/loggingcontext.decorator';

@Injectable()
@WithLoggingContext("ApplicationService")
export class AppService extends LoggingContextService {
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
