import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-recepcion',
  templateUrl: './recepcion.component.html',
  styleUrls: ['./recepcion.component.css']
})
export class RecepcionComponent implements OnInit {

  recepcion: any = {};
  showSuccessMessage: boolean | undefined;

  selectedAnalisisEnsayo: any;
  selectedAnalista: any;
  selectedEquipo: any;
  selectedEmpleado: any;
  selectedMuestraPreparacion: any;

  analisisEnsayoOptions = [
    { label: 'Análisis de Suelo', value: 'analisisSuelo' },
    { label: 'Ensayo de Agua', value: 'ensayoAgua' },
    // Agrega más opciones según sea necesario
  ];

  analistaOptions = [
    { label: 'Juan Pérez', value: 'juanPerez' },
    { label: 'María Gómez', value: 'mariaGomez' },
    // Agrega más opciones según sea necesario
  ];

  equipoOptions = [
    { label: 'Equipo de Laboratorio 1', value: 'equipoLab1' },
    { label: 'Equipo de Laboratorio 2', value: 'equipoLab2' },
    // Agrega más opciones según sea necesario
  ];

  empleadoOptions = [
    { label: 'Carlos Rodríguez', value: 'carlosRodriguez' },
    { label: 'Laura Martínez', value: 'lauraMartinez' },
    // Agrega más opciones según sea necesario
  ];

  muestraPreparacionOptions = [
    { label: 'Preparación de Muestra 1', value: 'preparacionMuestra1' },
    { label: 'Preparación de Muestra 2', value: 'preparacionMuestra2' },
    // Agrega más opciones según sea necesario
  ];

  datosCliente: any = {
    cliente: '',
    nit: '',
    direccion: '',
    telefono: '',
    consecutivo: '',
    solicitante: '',
    cargo: '',
    municipio: ''
  };
  
  clientes: any[] = [
    { label: 'Lola', value: 'Cliente1', nit: '12345', direccion: 'Dirección1', telefono: '1111111', municipio: 'Municipio1' },
    { label: 'Lina', value: 'Cliente2', nit: '67890', direccion: 'Dirección2', telefono: '2222222', municipio: 'Municipio2' }
    // Agrega más clientes según sea necesario
  ];

  solicitantes: any[] = [
    { label: 'Solicitante1', value: 'Solicitante1', cargo: 'Cargo1', municipio: 'Municipio1' },
    { label: 'Solicitante2', value: 'Solicitante2', cargo: 'Cargo2', municipio: 'Municipio2' }
    // Agrega más solicitantes según sea necesario
  ];

  seleccionadoSi: any;
  seleccionadoNo: any;
  motivoRechazo: any;
  respuestaClienteComentario: any;

  cargarDatosCliente(event: any) {
    const clienteSeleccionado = this.clientes.find(c => c.value === event.value);
    
    if (clienteSeleccionado) {
      this.datosCliente.nit = clienteSeleccionado.nit;
      this.datosCliente.direccion = clienteSeleccionado.direccion;
      this.datosCliente.telefono = clienteSeleccionado.telefono;
      this.datosCliente.municipio = clienteSeleccionado.municipio;
      console.log('Datos del cliente cargados:', this.datosCliente);
    } else {
      console.log('Cliente no encontrado para el valor seleccionado:', event.value);
    }
  }  
  
  cargarDatosSolicitante() {
    const solicitanteSeleccionado = this.solicitantes.find(s => s.value === this.datosCliente.solicitante);
    
    if (solicitanteSeleccionado) {
      this.datosCliente.cargo = solicitanteSeleccionado.cargo;
      this.datosCliente.municipio = solicitanteSeleccionado.municipio;
      console.log('Datos del solicitante cargados:', this.datosCliente);
    } else {
      console.log('Solicitante no encontrado para el valor seleccionado:', this.datosCliente.solicitante);
    }
  }
  
  registrarRecepcion() {
    // Lógica para registrar la recepción
    console.log('Recepción registrada:', this.recepcion);
    this.showSuccessMessage = true; // Esto podría desencadenar algún mensaje en tu interfaz
  }

  constructor() {}

  ngOnInit() {}

}
