import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ShowcaseComponent } from './showcase-page/showcase-page.component';
import { RouterModule, Routes } from '@angular/router';
import { ShowcaseEditorComponent } from './showcase-editor/showcase-editor.component';
import { ProjectPageComponent } from './project-page/project-page.component';

const routes: Routes = [
  ShowcaseComponent.Route,
  ShowcaseEditorComponent.Route,
  ProjectPageComponent.Route
];

@NgModule({
  declarations: [],
  imports: [CommonModule, RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ShowcaseRoutingModule {}
