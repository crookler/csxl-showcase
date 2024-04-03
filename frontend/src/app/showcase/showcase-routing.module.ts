import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ShowcaseComponent } from './showcase-page/showcase-page.component';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [ShowcaseComponent.Route];

@NgModule({
  declarations: [],
  imports: [CommonModule, RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ShowcaseRoutingModule {}
