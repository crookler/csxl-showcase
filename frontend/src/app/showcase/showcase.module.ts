import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ShowcaseComponent } from './showcase-page/showcase-page.component';
import { ProjectCard } from './widgets/project-card/project-card.widget';
import { MatCardModule } from '@angular/material/card';
import { ShowcaseRoutingModule } from './showcase-routing.module';

@NgModule({
  declarations: [
    //Components
    ShowcaseComponent,

    //Widgets
    ProjectCard
  ],
  imports: [CommonModule, MatCardModule, ShowcaseRoutingModule]
})
export class ShowcaseModule {}
