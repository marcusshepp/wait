export * from './api.service';
import { ApiCodegenService } from './api.service';
export * from './login.service';
import { LoginCodegenService } from './login.service';
export * from './register.service';
import { RegisterCodegenService } from './register.service';
export const APIS = [ApiCodegenService, LoginCodegenService, RegisterCodegenService];
