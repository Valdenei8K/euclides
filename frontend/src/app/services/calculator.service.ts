import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import { Processamento } from '../models/Processamento';

@Injectable({
  providedIn: 'root'
})
export class CalculatorService {
  private apiUrl = `${environment.API_URL}`;
  constructor(private http: HttpClient) { }
  
  public processNumbers(numeros: Number[]): Observable<Processamento> {
    const payload = {numeros};
    return this.http.post<Processamento>(`${this.apiUrl}processar/`, payload);
  }

  public getProcessNumbers(limit=10): Observable<Processamento[]> {
    
    return this.http.get<Processamento[]>(`${this.apiUrl}listar/?limit=${limit}`);
  }
}
