import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ShowcaseComponent } from './showcase-page/showcase-page.component';
import { MatCardModule } from '@angular/material/card';

@NgModule({
  declarations: [ShowcaseComponent],
  imports: [CommonModule, MatCardModule]
})
export class ShowcaseModule {}
