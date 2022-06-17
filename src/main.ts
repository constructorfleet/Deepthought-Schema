import { NestFactory } from '@nestjs/core';
import { AppModule } from './app/app.module';
import { LoggerService } from './app/logging/log.service';
import { ConfigService } from '@nestjs/config';
import { DeepthoughtConfiguration } from './app/config';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  const logger = await app.resolve(LoggerService);
  const configService = await app.resolve(ConfigService<DeepthoughtConfiguration>);
  logger.error(configService.getOrThrow<string>(
      'schema.directory',
      {
        infer: true
      }
    ));
  await app.init()
}

(async () => await bootstrap())();
