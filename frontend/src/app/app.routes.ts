import { Routes } from '@angular/router';
import {PlayComponent} from '../pages/play/play.component';
import {AppComponent} from './app.component';
import {AboutComponent} from '../pages/about/about.component';
import {ApiDocsComponent} from '../pages/api-docs/api-docs.component';
import {HelpPageComponent} from '../pages/help-page/help-page.component';
import {LoginComponent} from '../pages/login/login.component';
import {RegisterComponent} from '../pages/register/register.component';
import {HomeComponent} from '../pages/home/home.component';

export const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    title: 'Home'
  },
  {
    path: 'play',
    component: PlayComponent,
    title: 'Play'
  },
  {
    path: 'about',
    component: AboutComponent,
    title: 'About'
  },
  {
    path: 'api-docs',
    component: ApiDocsComponent,
    title: 'API Documentation'
  },
  {
    path: 'help',
    component: HelpPageComponent,
    title: 'Help'
  },
  {
    path: 'login',
    component: LoginComponent,
    title: 'Login',
  },
  {
    path: 'register',
    component: RegisterComponent,
    title: 'Register',
  }
];
