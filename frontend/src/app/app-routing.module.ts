import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppLayoutComponent } from './layout/app.layout.component';
import { UsuarioComponent } from './components/usuario/usuario.component';
import { ClienteComponent } from './components/cliente/cliente.component';
import { RecepcionComponent } from './components/recepcion/recepcion.component';
import { AppComponent } from './app.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { ReporteComponent } from './components/reporte/reporte.component';

const routes: Routes = [
  { path: '', component: AppLayoutComponent, 
    children: [
    { path: '',data: { breadcrumb: 'Inicio' }, component: DashboardComponent},
    { path: 'usuario',data: { breadcrumb: 'Registro de Usuarios' }, component: UsuarioComponent  },
    { path: 'cliente',data: { breadcrumb: 'Registro de Clientes' }, component: ClienteComponent },
    { path: 'recepcion',data: { breadcrumb: 'Recepcion de Muestras' }, component: RecepcionComponent},
    { path: 'reporte',data: { breadcrumb: 'Lista de Reportes' }, component: ReporteComponent},
    { path: 'salir',data: { breadcrumb: 'Salidaxd' }, component: AppComponent}
  ]},

];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
