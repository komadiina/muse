import {Component, NgIterable} from '@angular/core';
import {NgForOf} from '@angular/common';
import {navbarItems} from '../../config/navbarItems';

@Component({
  selector: 'app-navbar',
  imports: [
    NgForOf
  ],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {
  navbarItems: Array<any>;

  constructor() {
    this.navbarItems = navbarItems
  }

  redirect(link: string) {
    window.location.assign(link);
  }
}
