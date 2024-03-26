import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AgregarvidComponent } from './agregarvid.component';

describe('AgregarvidComponent', () => {
  let component: AgregarvidComponent;
  let fixture: ComponentFixture<AgregarvidComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AgregarvidComponent]
    });
    fixture = TestBed.createComponent(AgregarvidComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
