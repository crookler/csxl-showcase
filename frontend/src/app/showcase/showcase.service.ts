/* eslint-disable prettier/prettier */
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Project, ProjectResponse } from './project.model';
import { Observable, ReplaySubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ShowcaseService {

  private projects: ReplaySubject<Project[]> = new ReplaySubject(1);
 projects$: Observable<Project[]> = this.projects.asObservable();

  constructor(protected http: HttpClient) {
    this.projects.next;
  }

  //returns all projects in the database (I think)
  getProjects(): Observable<Project[]> {
    return this.http.get<Project[]>('/api/showcase');
    
  }
    
  /*
  this.http
      .get<TimerResponse[]>('/api/productivity')
      .pipe(this.mapTimerResponseListToDataList)
      .subscribe((timers) => this.timers.next(timers));


      getProjects(): Observable<Project[]> {
    return this.http.get<Project[]>('/api/showcase');
  }
  
  */

  getProject(id: number): Observable<Project> {
    return this.http.get<Project>('/api/showcase/' + id);
  }

  createProject(showcase: Project): Observable<Project> {
    return this.http.post<Project>('api/showcase', showcase);
  }

  updateProject(showcase: Project): Observable<Project> {
    return this.http.put<Project>('api/showcase', showcase);
  }

  deleteProject(id: number): Observable<Project> {
    return this.http.delete<Project>('/api/showcase/' + id);
  }

  
  //timerData is the frontend one

}
