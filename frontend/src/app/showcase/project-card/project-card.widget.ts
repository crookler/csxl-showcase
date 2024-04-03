import { Component, Input } from '@angular/core';
import { Profile } from '/workspace/frontend/src/app/profile/profile.service';
import { Project } from '../projects/project.model';

@Component({
  selector: 'project-card',
  templateUrl: './project-card.widget.html',
  styleUrls: ['./project-card.widget.css']
})
export class ProjectCardComponent {
  @Input() project!: Project;
  /** The profile of the currently signed in user */
  @Input() profile?: Profile;
  /** @deprecated Stores the permission values for a profile */
  @Input() profilePermissions!: Map<number, number>;

  /**
   * Determines whether or not the tooltip on the card is disabled
   * @param element: The HTML element
   * @returns {boolean}
   *
   */
  constructor() {}
}
