import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DashempleadoComponent } from './dashempleado.component';

describe('DashempleadoComponent', () => {
  let component: DashempleadoComponent;
  let fixture: ComponentFixture<DashempleadoComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DashempleadoComponent]
    });
    fixture = TestBed.createComponent(DashempleadoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
