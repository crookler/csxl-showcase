/* eslint-disable prettier/prettier */
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Project } from './projects/project.model';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ShowcaseService {

  constructor(protected http: HttpClient) { 
    
  }

//returns all projects in the database (I think)
  getProjects(): Observable<Project[]>{
    return this.http.get<Project[]>('/api/showcase');
  } 
}
