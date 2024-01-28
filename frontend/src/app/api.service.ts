import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Registro } from './clientes.model';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:8000/';
  constructor(private http: HttpClient) { }

  realizarConsulta(query: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/consulta?query=${encodeURIComponent(query)}`);

  
  }
  Registro:any
  guardarRegistro(registro: Registro): Observable<any> {
    console.log('entró mmgvo', this.Registro)
    return this.http.post<any>(`${this.apiUrl}api/cliente`, registro);
  }
}
