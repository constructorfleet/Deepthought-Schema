import { Reflector } from '@nestjs/core';
import { LOGGING_CONTEXT_METADATA_KEY } from './loggingcontext.decorator';
import { LoggerService } from '../log.service';

export abstract class LoggingContextService {
  protected constructor(
    protected readonly reflector: Reflector,
    protected readonly logger: LoggerService,
  ) {
    const context: string | null = reflector.get(
      LOGGING_CONTEXT_METADATA_KEY,
      this.constructor
    );
    if (context) {
      this.logger.setContext(context);
    }
  }
}
