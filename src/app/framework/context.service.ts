import { Reflector } from '@nestjs/core';
import { CONTEXT_METADATA_KEY } from './context.decorator';
import { LoggerService } from '../logging/log.service';

export abstract class ContextService {
  protected constructor(
    private readonly reflector: Reflector,
    private readonly logger: LoggerService,
  ) {
    const context: string | null = reflector.get(
      CONTEXT_METADATA_KEY,
      this.constructor
    );
    if (context) {
      this.logger.setContext(context);
    }
  }
}
