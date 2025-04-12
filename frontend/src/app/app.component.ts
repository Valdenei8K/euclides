import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NumberFormComponent } from './components/number-form/number-form.component';
import { CalculationHistoryComponent } from "./calculation-history/calculation-history.component";




@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, NumberFormComponent, CalculationHistoryComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'challenge';
}
