import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AppLayoutModule } from './layout/app.layout.module';

import { UsuarioComponent } from './components/usuario/usuario.component';
import { ClienteComponent } from './components/cliente/cliente.component';
import { RecepcionComponent } from './components/recepcion/recepcion.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { ReporteComponent } from './components/reporte/reporte.component';


import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AutoCompleteModule } from "primeng/autocomplete";
import { CalendarModule } from "primeng/calendar";
import { ChipsModule } from "primeng/chips";
import { DropdownModule } from "primeng/dropdown";
import { InputMaskModule } from "primeng/inputmask";
import { InputNumberModule } from "primeng/inputnumber";
import { CascadeSelectModule } from "primeng/cascadeselect";
import { MultiSelectModule } from "primeng/multiselect";
import { InputTextareaModule } from "primeng/inputtextarea";
import { InputTextModule } from "primeng/inputtext";

import { AvatarModule } from 'primeng/avatar';
import { TableModule } from 'primeng/table';
import { ChartModule } from 'primeng/chart';
import { KnobModule } from 'primeng/knob';
import { BadgeModule } from 'primeng/badge';
import { LayoutService } from './layout/service/app.layout.service';


@NgModule({
  declarations: [
    AppComponent,
    UsuarioComponent,
    ClienteComponent,
    DashboardComponent,
    RecepcionComponent,
    ReporteComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    AppLayoutModule,
    DropdownModule,
    FormsModule,
		AutoCompleteModule,
		CalendarModule,
		ChipsModule,
		InputMaskModule,
		InputNumberModule,
		CascadeSelectModule,
		MultiSelectModule,
		InputTextareaModule,
		InputTextModule,
    AvatarModule,
    TableModule,
    ChartModule,
    KnobModule,
    BadgeModule,
    

  ],
  providers: [LayoutService],
  bootstrap: [AppComponent]
})
export class AppModule { }
