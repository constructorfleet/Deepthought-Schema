import { NestFactory } from '@nestjs/core';
import { AppModule } from './app/app.module';
import { LoggerService } from './app/logging/log.service';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  const logger = await app.resolve(LoggerService);

  await app.init()
}

(async () => await bootstrap())();
