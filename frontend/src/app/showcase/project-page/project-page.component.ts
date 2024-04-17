import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { isAuthenticated } from 'src/app/gate/gate.guard';
import { profileResolver } from 'src/app/profile/profile.resolver';
import { showcaseResolver } from '../showcase.resolver';

@Component({
  selector: 'app-project-page',
  templateUrl: './project-page.component.html',
  styleUrls: ['./project-page.component.css']
})
export class ProjectPageComponent {
  public static Route: Route = {
    path: 'project', //full prefix specified in app routing module
    component: ProjectPageComponent,
    title: 'Showcase',
    canActivate: [isAuthenticated]
  };
}
