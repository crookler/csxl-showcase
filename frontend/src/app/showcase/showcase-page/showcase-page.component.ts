/* eslint-disable prettier/prettier */
import { Component } from '@angular/core';
import { isAuthenticated } from '../../gate/gate.guard';
import { profileResolver } from '../../profile/profile.resolver';
import { Route } from '@angular/router';
import { Project } from '../project.model';
import { showcaseResolver } from '../showcase.resolver';
import { ActivatedRoute } from '@angular/router';
import { Profile } from 'src/app/profile/profile.service';

@Component({
  selector: 'app-showcase',
  templateUrl: './showcase-page.component.html',
  styleUrls: ['./showcase-page.component.css']
})
export class ShowcaseComponent {
  public static Route: Route = {
    path: '', //full prefix specified in app routing module
    component: ShowcaseComponent,
    title: 'Showcase',
    canActivate: [isAuthenticated],
    resolve: { profile: profileResolver, projects: showcaseResolver },

  };

  public projects: Project[];
  public profile: Profile;

  constructor(private route: ActivatedRoute) {
    const data = this.route.snapshot.data as {
      profile: Profile;
      projects: Project[];
    };
    this.profile = data.profile;
    this.projects = data.projects;
  }
}
