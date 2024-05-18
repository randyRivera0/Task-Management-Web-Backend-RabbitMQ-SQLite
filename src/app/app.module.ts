import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { ListaVideosComponent } from './components/lista-videos/lista-videos.component';
import { HttpClientModule } from '@angular/common/http';
import { AgregarvidComponent } from './components/agregarvid/agregarvid.component'
import { FormsModule } from '@angular/forms';
import { ActualizarComponent } from './components/actualizar/actualizar.component';
import { VerComponent } from './components/ver/ver.component';
import { SafePipe } from './components/safe.pipe';
import {MatFormFieldModule} from '@angular/material/form-field';
import { FilterPipe } from './filter.pipe';
import { LoginComponent } from './components/login/login.component';
import { InicioComponent } from './components/inicio/inicio.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import {MatToolbarModule} from '@angular/material/toolbar';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [
    AppComponent,
    ListaVideosComponent,
    AgregarvidComponent,
    ActualizarComponent,
    VerComponent,
    SafePipe,
    FilterPipe,
    LoginComponent,
    InicioComponent,
    NavbarComponent,
    
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatSlideToggleModule,
    HttpClientModule,
    FormsModule,
    MatFormFieldModule,
    MatToolbarModule,
    RouterModule
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
