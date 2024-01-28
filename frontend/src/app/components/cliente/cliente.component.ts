import { Component } from '@angular/core';
import { ApiService } from '../../api.service';
import { Registro } from '../../clientes.model';

@Component({
  selector: 'app-cliente',
  templateUrl: './cliente.component.html',
  styleUrls: ['./cliente.component.css']
})
export class ClienteComponent {
  
  nuevoRegistro: Registro = {
    cliente: '',
    nit: '',
    solicitante: '',
    cargo: '',
    direccion: '',
    municipio: '',
    telefono: '',
    fax: '',
    consecutivo: '',
    observaciones: ''
  };

  showSuccessMessage = false;

  constructor(private apiService: ApiService) {}

  guardarRegistro() {
    this.apiService.guardarRegistro(this.nuevoRegistro).subscribe(
      (res) => {
        console.log('Registro guardado con éxito:', res);
        // Realiza acciones adicionales aquí si es necesario
        this.showSuccessMessage = true;
      },
      (error) => {
        console.error('Error al guardar el registro:', error);
        // Manejo de errores aquí si es necesario
      }
    );
  }
}

