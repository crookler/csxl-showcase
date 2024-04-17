/* eslint-disable prettier/prettier */
import { Component, Input } from '@angular/core';
import { Profile } from '/workspace/frontend/src/app/profile/profile.service';
import { Project } from '../../project.model';
import { Router } from '@angular/router';
import { ShowcaseService } from '../../showcase.service';

@Component({
  selector: 'project-card',
  templateUrl: './project-card.widget.html',
  styleUrls: ['./project-card.widget.css']
})
export class ProjectCard {
  /**the project being displayed */
  @Input() project!: Project;
  /** The profile of the currently signed in user */
  @Input() profile!: Profile;
  /** @deprecated Stores the permission values for a profile */
  @Input() profilePermissions!: Map<number, number>;

  /**
   * Determines whether or not the tooltip on the card is disabled
   * @param element: The HTML element
   * @returns {boolean}
   *
   */
  constructor(private router: Router,private showcaseService: ShowcaseService) {}

editProject(){
    this.router.navigate(['/showcase', this.project.id, 'edit']);
    
  }

  deleteProject(){
    this.showcaseService.deleteProject(this.project.id as number).subscribe(() => {
     window.location.reload();
    
  });
  
  
}
}


