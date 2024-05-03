/* eslint-disable prettier/prettier */
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ShowcaseComponent } from './showcase-page/showcase-page.component';
import { ProjectCard } from './widgets/project-card/project-card.widget';

import { ShowcaseRoutingModule } from './showcase-routing.module';
import { ShowcaseEditorComponent } from './showcase-editor/showcase-editor.component';
import { MatTableModule } from '@angular/material/table';
import { MatSelectModule } from '@angular/material/select';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { SharedModule } from '../shared/shared.module';

import { DatePipe, NgForOf } from '@angular/common';
import { LayoutModule } from '@angular/cdk/layout';

/* Material UI Dependencies */
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatDialogModule } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatListModule } from '@angular/material/list';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatSliderModule } from '@angular/material/slider';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { MatTabsModule } from '@angular/material/tabs';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTooltipModule } from '@angular/material/tooltip';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { ProjectPageComponent } from './project-page/project-page.component';

@NgModule({
  declarations: [
    //Components
    ShowcaseComponent,
    ShowcaseEditorComponent,

    //Widgets
    ProjectCard,
    ProjectPageComponent
  ],
  imports: [
    CommonModule,

    ShowcaseRoutingModule,
    MatButtonModule,
    MatCardModule,
    MatDialogModule,
    MatFormFieldModule,
    MatIconModule,
    MatInputModule,
    MatListModule,
    MatProgressBarModule,
    MatSidenavModule,
    MatSliderModule,
    MatSnackBarModule,
    MatTabsModule,
    MatToolbarModule,
    MatTooltipModule,
    MatCheckboxModule,
    FormsModule,
    ReactiveFormsModule
  ],
  exports: [ProjectCard, ProjectPageComponent]
})
export class ShowcaseModule {}
