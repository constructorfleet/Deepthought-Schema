import { LoggingContextService } from '../../logging/context/loggingContextService';
import { CanActivate, ExecutionContext } from '@nestjs/common';
import { Reflector } from '@nestjs/core';
import { LoggerService } from '../../logging/log.service';

export type GuardCallback<TArg, TReturn = true> =
  (arg: TArg) => TReturn;

export abstract class GuardService<TArg, TReturn = boolean> extends LoggingContextService implements CanActivate {
  protected abstract get METADATA_KEY(): string;

  protected constructor(
    reflector: Reflector,
    logger: LoggerService,
  ) {
    super(
      reflector,
      logger,
    );
  }

  protected abstract getGuardArgument(context: ExecutionContext): TArg;

  async canActivate(context: ExecutionContext): Promise<boolean> {
    const argument = this.getGuardArgument(context);
    const guards = this.getGuards(context);

    return guards.every(
      (guard) => guard(argument) ?? false,
    );
  }

  private getGuards(context: ExecutionContext): GuardCallback<TArg, TReturn>[] {
    return this.reflector.get<GuardCallback<TArg, TReturn>[]>(
      this.METADATA_KEY,
      context.getHandler,
    ) || [];
  }
}
