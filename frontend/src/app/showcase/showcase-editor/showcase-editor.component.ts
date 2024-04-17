import { Component, inject } from '@angular/core';

import { MatSnackBar } from '@angular/material/snack-bar';
import {
  ActivatedRoute,
  ActivatedRouteSnapshot,
  CanActivateFn,
  Route,
  Router,
  RouterStateSnapshot
} from '@angular/router';
import { Project } from '../project.model';
import { Profile } from 'src/app/models.module';
import {
  FormBuilder,
  FormControl,
  Validators,
  FormGroup
} from '@angular/forms';
import { ShowcaseService } from '../showcase.service';
import { profileResolver } from 'src/app/profile/profile.resolver';
import { showcaseEditorResolver } from '../showcase.resolver';
import { isAuthenticated } from 'src/app/gate/gate.guard';
import { PermissionService } from 'src/app/permission.service';
import { of } from 'rxjs';
import { ProfileService } from 'src/app/profile/profile.service';

/*
const canActivateEditor: CanActivateFn = (
  route: ActivatedRouteSnapshot,
  state: RouterStateSnapshot
) => {
  let id: string = route.params['id'];
  if (id == '0') {
    return true;
  }
  // Determine if author is the one activating or root
  inject(ProfileService).profile$.;
  inject(ShowcaseService).getProject(Number(id)).pipe();

  if (current_onyen != author_onyen) {
    return inject(PermissionService).check(
      'showcase.update',
      'showcase/' + data.showcase.id
    );
  } else {
    return true;
  }
};
*/

@Component({
  selector: 'app-showcase-editor',
  templateUrl: './showcase-editor.component.html',
  styleUrls: ['./showcase-editor.component.css']
})
export class ShowcaseEditorComponent {
  public static Route: Route = {
    path: ':id/edit',
    component: ShowcaseEditorComponent,
    title: 'Showcase Editor',
    canActivate: [isAuthenticated],
    resolve: { profile: profileResolver, showcase: showcaseEditorResolver }
  };

  // Store the showcase post being edited/created
  public showcase: Project;

  // Store the currently-logged-in user's profile.
  public profile: Profile | null = null;

  // Store showcase slug
  showcase_id: string = '0';

  // Add validators to the form
  title = new FormControl('', [Validators.required]);
  shorthand = new FormControl('', [Validators.required]);
  thumbnail = new FormControl('', [Validators.required]); //holding a url or something? (not sure yet)
  short_description = new FormControl('', [
    Validators.required,
    Validators.maxLength(150)
  ]);
  text_body = new FormControl('', [Validators.maxLength(2000)]);

  // Showcase editor form
  public showcaseForm = this.formBuilder.group({
    title: this.title,
    shorthand: this.shorthand,
    thumbnail: this.thumbnail,
    short_description: this.short_description,
    text_body: this.text_body,
    author: '',
    onyen: '',
    public: false
  });

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    protected formBuilder: FormBuilder,
    protected snackBar: MatSnackBar,
    private showcaseService: ShowcaseService
  ) {
    // Initialize data from resolvers
    const data = this.route.snapshot.data as {
      profile: Profile;
      showcase: Project;
    };
    this.profile = data.profile;
    this.showcase = data.showcase;

    // Add in default values for form (author is hard coded as the currently signed in user)
    this.showcaseForm.setValue({
      title: this.showcase.title,
      shorthand: this.showcase.shorthand,
      thumbnail: this.showcase.thumbnail,
      short_description: this.showcase.short_description,
      text_body: this.showcase.text_body,
      // if author blank assign currently signed in user otherwise use previous author
      author:
        this.showcase.author == ''
          ? this.profile.first_name + ' ' + this.profile.last_name
          : this.showcase.author,
      onyen:
        this.showcase.onyen == '' ? this.profile.onyen : this.showcase.onyen,
      public: true //make all projects public until (if) drafts are implemented
    });

    this.showcase_id = this.route.snapshot.params['id'];
  }

  /** Event handler to handle submitting the showcase update form
   * @returns {void}
   */
  onSubmit(): void {
    if (this.showcaseForm.valid) {
      Object.assign(this.showcase, this.showcaseForm.value);
      // Create new showcase if in new editor
      if (this.showcase_id == '0') {
        this.showcaseService.createProject(this.showcase).subscribe({
          next: (showcase) => this.onSuccess(showcase),
          error: (err) => this.onError(err)
        });
      }
      // Update existing showcase if in /{id}/edit
      else {
        this.showcaseService.updateProject(this.showcase).subscribe({
          next: (showcase) => this.onSuccess(showcase),
          error: (err) => this.onError(err)
        });
      }
    }
  }

  private onSuccess(showcase: Project): void {
    this.router.navigate(['/showcase']);

    let message: string =
      this.showcase_id === '0' ? 'Showcase Created' : 'Showcase Updated';

    this.snackBar.open(message, '', { duration: 2000 });
  }

  /** Opens a snackbar when there is an error updating an organization.
   * @returns {void}
   */
  private onError(err: any): void {
    let message: string =
      this.showcase_id === '0'
        ? 'Error: Showcase Not Created'
        : 'Error: Showcase Not Updated';

    this.snackBar.open(message, '', {
      duration: 2000
    });
  }
}
