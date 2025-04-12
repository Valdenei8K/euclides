import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { CalculatorService } from '../../services/calculator.service';

@Component({
  selector: 'app-number-form',
  standalone: true,
  templateUrl: './number-form.component.html',
  styleUrls: ['./number-form.component.css'],
  imports: [CommonModule, ReactiveFormsModule] 
})
export class NumberFormComponent {
  form: FormGroup;
  status: string = '';

  constructor(private fb: FormBuilder, private calculatorService: CalculatorService) {
    this.form = this.fb.group({
      num1: [null, Validators.required],
      num2: [null, Validators.required],
      num3: [null, Validators.required]
    });
  }

  submit() {
    const numbers = [this.form.get('num1')?.value, this.form.get('num2')?.value, this.form.get('num3')?.value]
    this.calculatorService.processNumbers(numbers).subscribe(
      (response)=>{
        console.log(response)
        this.form.reset()
  
    },
    (error)=>{
      console.log(error)
    }
  )
    
  }
}
