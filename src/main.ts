import { NestFactory } from '@nestjs/core';
import { AppModule } from './app/app.module';
import { LoggerService } from './logging/log.service';
import { ConfigService } from '@nestjs/config';
import { DeepthoughtConfiguration } from './app/config';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  const logger = await app.resolve(LoggerService);
  const configService = await app.resolve(ConfigService<DeepthoughtConfiguration>);
  logger.error(configService.getOrThrow<string>(
      'graphql.typeDirectory',
      {
        infer: true
      }
    ));
  await app.listen(3000, async () => {});
}

(async () => await bootstrap())();
