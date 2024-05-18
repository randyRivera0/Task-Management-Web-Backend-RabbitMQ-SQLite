import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListaVideosComponent } from './components/lista-videos/lista-videos.component';
import { AgregarvidComponent } from './components/agregarvid/agregarvid.component';
import { ActualizarComponent } from './components/actualizar/actualizar.component';
import { VerComponent } from './components/ver/ver.component';
import { LoginComponent } from './components/login/login.component';

const routes: Routes = [
  
  {path: 'login', component: LoginComponent},
  {path : 'obtener', component: ListaVideosComponent},
  {path : '', redirectTo: 'login', pathMatch:'full'},
  {path: 'agregarvid', component: AgregarvidComponent   },
  {path: 'actualizar/:id', component: ActualizarComponent},
  {path: 'ver/:id', component: VerComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
