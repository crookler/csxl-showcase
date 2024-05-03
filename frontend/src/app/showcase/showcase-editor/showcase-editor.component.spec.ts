import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ShowcaseEditorComponent } from './showcase-editor.component';

describe('CreatorComponent', () => {
  let component: ShowcaseEditorComponent;
  let fixture: ComponentFixture<ShowcaseEditorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ShowcaseEditorComponent]
    }).compileComponents();

    fixture = TestBed.createComponent(ShowcaseEditorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
