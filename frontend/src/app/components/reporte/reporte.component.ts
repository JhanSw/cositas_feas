import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';


@Component({
  selector: 'app-reporte',
  templateUrl: './reporte.component.html',
  styleUrls: ['./reporte.component.css']
})
export class ReporteComponent implements OnInit {
  usuario: string = '';
  contrasena: string = '';
  showSuccessMessage: boolean = false;
  showErrorMessage: boolean = false;

  iniciarSesion(): void {
    const autenticacionExitosa = true;
    console.log('Iniciando sesión...');
    
    if (autenticacionExitosa) {
      this.router.navigate(['']);
      console.log('redirige...');

    }
  }

  constructor(private router: Router) {}

  ngOnInit() {
  }

}

