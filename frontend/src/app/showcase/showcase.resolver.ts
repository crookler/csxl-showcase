import { inject } from '@angular/core';
import { ResolveFn } from '@angular/router';
import { Project } from './project.model';
import { ShowcaseService } from './showcase.service';
import { catchError, map, of } from 'rxjs';

/** This resolver injects the list of projects into the showcase component. */
export const showcaseResolver: ResolveFn<Project[] | undefined> = (
  route,
  state
) => {
  return inject(ShowcaseService).getProjects();
};
