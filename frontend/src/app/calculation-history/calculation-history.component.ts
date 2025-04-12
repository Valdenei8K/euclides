import { Component, inject, OnDestroy, OnInit, PLATFORM_ID } from '@angular/core';
import { CalculatorService } from '../services/calculator.service';
import { Processamento } from '../models/Processamento';
import { CommonModule, isPlatformBrowser } from '@angular/common';

@Component({
  selector: 'app-calculation-history',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './calculation-history.component.html',
  styleUrl: './calculation-history.component.css'
})
export class CalculationHistoryComponent implements OnInit, OnDestroy { 
  processList:Processamento[] = [];
  constructor(private calculatorService: CalculatorService){
    
  } 
  intervalId: any;
  private platformId = inject(PLATFORM_ID);

  ngOnInit(): void {
  
    if (isPlatformBrowser(this.platformId)) {
      this.intervalId = setInterval(() => {
        this.loadProcessHistory();
      }, 1000);
    }
  }

  ngOnDestroy(): void {
    if (this.intervalId) {
      clearInterval(this.intervalId);
    }
  }

  public loadProcessHistory(){
    
    this.calculatorService.getProcessNumbers().subscribe(
      (response)=>{
      this.processList = response 

    },(error)=>{
      console.log('deu erro')
      console.log(error)
    })
  }

}
