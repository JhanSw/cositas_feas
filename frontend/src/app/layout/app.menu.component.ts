import { Component, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api';
import { LayoutService } from './service/app.layout.service';

@Component({
    selector: 'app-menu',
    templateUrl: './app.menu.component.html'
})
export class AppMenuComponent implements OnInit {

    model: any[] = [];

    constructor(public layoutService: LayoutService) { }

    ngOnInit() {
        this.model = [
            { label: 'Home', icon: 'pi pi-fw pi-home', routerLink: ['']},
            { label: 'Usuario', icon: 'pi pi-fw pi-user', routerLink: ['/usuario'] },
            { label: 'Cliente', icon: 'pi pi-fw pi-user', routerLink: ['/cliente'] },
            { label: 'Recepcion', icon: 'pi pi-fw pi-briefcase', routerLink: ['/recepcion'] },
            { label: 'Reporte', icon: 'pi pi-fw pi-book', routerLink: ['/reporte'] },
            { label: 'Salir', icon: 'pi pi-fw pi-times', routerLink: ['/salir'] }
        ];
    }
}
