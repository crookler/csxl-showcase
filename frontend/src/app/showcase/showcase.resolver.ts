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

export const showcaseEditorResolver: ResolveFn<Project | undefined> = (
  route,
  state
) => {
  // If a showcase is being created, return blank project
  if (route.params['id'] == '0') {
    return {
      id: null,
      title: '',
      shorthand: '',
      thumbnail: '',
      short_description: '',
      text_body: '',
      author: '',
      onyen: '',
      public: false
    };
  }

  // If editing, return the selected organization if it exists
  return inject(ShowcaseService)
    .getProject(Number(route.params['id']))
    .pipe(
      catchError((error) => {
        console.log(error);
        return of(undefined);
      })
    );
};
