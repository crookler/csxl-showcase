/* eslint-disable prettier/prettier */
import { Component } from '@angular/core';
import { isAuthenticated } from '../../gate/gate.guard';
import { profileResolver } from '../../profile/profile.resolver';
import { Route } from '@angular/router';
import { Project } from '../projects/project.model';
import { ShowcaseService } from '../showcase.service';

@Component({
  selector: 'app-showcase',
  templateUrl: './showcase-page.component.html',
  styleUrls: ['./showcase-page.component.css']
})
export class ShowcaseComponent {
  public static Route: Route = {
    path: 'showcase',
    component: ShowcaseComponent,
    title: 'Showcase',
    canActivate: [isAuthenticated],
    resolve: { profile: profileResolver }
  };

  projects: Project[] = [
    {
      id: 1,
      name: 'Project 1',
      thumbnail: 'path/to/thumbnail1.jpg',
      short_description: 'Short description of Project 1',
      long_description: 'Long description of Project 1',
      website: 'https://project1.com',
      email: 'contact@project1.com',
      author: 'Author Name',
      linked_in: 'https://linkedin.com/in/author',
      heel_life: 'HeelLife link',
      public: true,
      slug: 'project-1',
      shorthand: 'P1'
    },
    {
      id: 2,
      name: 'Project 2',
      thumbnail: 'path/to/thumbnail2.jpg',
      short_description: 'A revolutionary approach to reducing water waste.',
      long_description:
        'This project aims to innovate in the field of water conservation with new technology that could drastically reduce water waste in agricultural and urban areas.',
      website: 'http://waterconservationproject.com',
      email: 'info@waterconservationproject.com',
      author: 'Jane Doe',
      linked_in: 'http://linkedin.com/in/janedoe',
      heel_life: 'http://heellife.unc.edu/organization/water-conservation',
      public: true,
      slug: 'water-conservation',
      shorthand: 'WC'
    },
    {
      id: 3,
      name: 'Project 3',
      thumbnail: 'path/to/thumbnail3.jpg',
      short_description: 'Enhancing urban areas with sustainable green spaces.',
      long_description:
        'Urban Green Spaces is dedicated to creating sustainable, accessible green spaces in urban environments, improving air quality and providing peaceful retreats for city dwellers.',
      website: 'http://urbangreenspaces.com',
      email: 'contact@urbangreenspaces.com',
      author: 'Carlos Smith',
      linked_in: 'http://linkedin.com/in/carlossmith',
      heel_life: 'http://heellife.unc.edu/organization/urban-green-spaces',
      public: true,
      slug: 'urban-green-spaces',
      shorthand: 'UGS'
    },
    {
      id: 4,
      name: 'Project 4',
      thumbnail: 'path/to/thumbnail4.jpg',
      short_description: 'Making renewable energy accessible and affordable.',
      long_description:
        'This initiative focuses on developing and implementing affordable renewable energy solutions for communities worldwide, especially in underprivileged areas.',
      website: 'http://renewableenergyforall.com',
      email: 'support@renewableenergyforall.com',
      author: 'Emily Tran',
      linked_in: 'http://linkedin.com/in/emilytran',
      heel_life: 'http://heellife.unc.edu/organization/renewable-energy',
      public: true,
      slug: 'renewable-energy',
      shorthand: 'REA'
    }
  ];

  constructor(public showcaseService: ShowcaseService) {
    this.showcaseService.getProjects();
  }
}
