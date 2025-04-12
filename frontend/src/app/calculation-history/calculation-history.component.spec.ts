import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CalculationHistoryComponent } from './calculation-history.component';

describe('CalculationHistoryComponent', () => {
  let component: CalculationHistoryComponent;
  let fixture: ComponentFixture<CalculationHistoryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CalculationHistoryComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CalculationHistoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
