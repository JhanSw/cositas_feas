import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  title = 'ceni';
  consulta = '';
  resultado: any;

  constructor(private apiService: ApiService) {}

  realizarConsulta() {
    this.apiService.realizarConsulta(this.consulta).subscribe((res) => {
      this.resultado = res;
    });
  }

}