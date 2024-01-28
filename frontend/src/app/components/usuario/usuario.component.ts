import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-usuario',
  templateUrl: './usuario.component.html',
  styleUrls: ['./usuario.component.css']
})
export class UsuarioComponent implements OnInit {
dropdownItems: any[]|undefined;
selectedState: any;

usuario: any = {}; 
tiposCargo = [
  { label: 'Administrador', value: 'admin' },
  { label: 'Usuario Normal', value: 'normal' },
  // Agrega más tipos de cargo según tus necesidades
];
tiposDocumento = [
  { label: 'Tarjeta de Identidad', value: 'tarjetaIdentidad' },
  { label: 'Cédula', value: 'cedula' },
  { label: 'Cédula de Extranjería', value: 'cedulaExtranjeria' },
];

registrarUsuario() {
  console.log(this.usuario);
  // agregar la lógica para enviar los datos al servidor, etc.
}

  constructor() { }

  ngOnInit() {
  }

}
