import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TasktakenComponent } from './tasktaken.component';

describe('TasktakenComponent', () => {
  let component: TasktakenComponent;
  let fixture: ComponentFixture<TasktakenComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TasktakenComponent]
    });
    fixture = TestBed.createComponent(TasktakenComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
