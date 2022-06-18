import {
  Ability,
  AbilityBuilder,
  AbilityClass,
  ExtractSubjectType,
  InferSubjects
} from '@casl/ability';
import {
  applyDecorators,
  ExecutionContext,
  Injectable,
  SetMetadata,
  UseGuards
} from '@nestjs/common';
import { GuardCallback, GuardService } from '../../app/guards/guard';
import { WithLoggingContext } from '../../logging/context/loggingcontext.decorator';
import { LoggingContextService } from '../../logging/context/loggingContextService';
import { Reflector } from '@nestjs/core';
import { LoggerService } from '../../logging/log.service';

export class User {
  constructor(
    public readonly id: string,
    public readonly isAdmin: boolean,
  ) {
  }
}

export class Node {
  constructor(
    public readonly id: String,
  ) {
  }
}

export enum Action {
  Manage = 'manage',
  Create = 'create',
  Read = 'read',
  Update = 'update',
  Delete = 'delete',
}

export type Subjects = InferSubjects<typeof User | typeof Node> | 'all';
export type ScopeAbility = Ability<[Action, Subjects]>;
export type ScopeGuard = GuardCallback<ScopeAbility, boolean>;

export interface Scope {
  action: Action;
  subject: typeof User | typeof Node | 'all';
}

export const REQUIRES_SCOPE_METADATA_KEY = 'RequiresScope';

export const RequiresScopes = (...scopes: Scope[]) =>
  applyDecorators(
    SetMetadata(REQUIRES_SCOPE_METADATA_KEY, scopes.map(
      (scope) =>
        (ability: ScopeAbility) => ability.can(scope.action, scope.subject),
    )),
    UseGuards(ScopeGuardService),
  );

@Injectable()
export class ScopeGuardService extends GuardService<ScopeAbility, boolean> {
  constructor(
    private readonly scopeFactory: AuthorizedScopeFactory,
    reflector: Reflector,
    logger: LoggerService
  ) {
    super(
      reflector,
      logger
    );
  }

  protected get METADATA_KEY(): string {
    return REQUIRES_SCOPE_METADATA_KEY;
  }

  protected getGuardArgument(context: ExecutionContext): ScopeAbility {
    const { user } = context.switchToHttp()
      .getRequest();
    return this.scopeFactory.createFor(user);
  }

}

@WithLoggingContext('AuthorizedScopeFactory')
@Injectable()
export class AuthorizedScopeFactory extends LoggingContextService {
  constructor(
    reflector: Reflector,
    logger: LoggerService
  ) {
    super(
      reflector,
      logger
    );
  }

  createFor(user: User) {
    const {
      can,
      cannot,
      build
    } = new AbilityBuilder<ScopeAbility>(Ability as AbilityClass<ScopeAbility>);

    if (user.isAdmin) {
      can(Action.Manage, 'all'); // read-write access to everything
    } else {
      can(Action.Read, 'all'); // read-only access to everything
    }

    can(Action.Update, Node, { id: '1' });
    cannot(Action.Delete, Node, { id: '100' });

    return build({
      detectSubjectType: (item) =>
        item.constructor as ExtractSubjectType<Subjects>,
    });
  }
}
