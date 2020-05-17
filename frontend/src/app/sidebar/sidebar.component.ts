import { Component, OnInit } from '@angular/core';
import { Routes } from '@angular/router';
import { DashboardComponent } from 'app/pages/dashboard/dashboard.component';


export interface RouteInfo {
    path: string;
    title: string;
    icon: string;
    // class: string;
}

export const ROUTES: RouteInfo[] = [

    { path: '/dashboard', title: 'Top Stories', icon: 'nc-planet' },
    { path: '/sports', title: 'Sports', icon: 'nc-trophy' },
    { path: '/health', title: 'Health', icon: 'nc-briefcase-24' },
    { path: '/buisness', title: 'Buisness', icon: 'nc-bank' },
    { path: '/technology', title: 'Technology', icon: 'nc-spaceship' },
    { path: '/global', title: 'Global', icon: 'nc-spaceship' },

];

@Component({
    moduleId: module.id,
    selector: 'sidebar-cmp',
    templateUrl: 'sidebar.component.html',
})

export class SidebarComponent implements OnInit {
    public menuItems: any[];
    ngOnInit() {
        this.menuItems = ROUTES.filter(menuItem => menuItem);
    }
}
