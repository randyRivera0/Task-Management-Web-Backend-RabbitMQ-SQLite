import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { VideoServService } from 'src/app/video-serv.service';
import {MatTableDataSource} from '@angular/material/table';
import {MatFormFieldModule} from '@angular/material/form-field';
import { Tarea } from 'src/app/tarea';

@Component({
  selector: 'app-lista-videos',
  templateUrl: './lista-videos.component.html',
  styleUrls: ['./lista-videos.component.css']
})
export class ListaVideosComponent implements OnInit {

  // estadosSlideToggle: { [key: number]: boolean } = {};
  tareas: Tarea[];

  
  constructor(private tareaserv: VideoServService,  private router: Router){}
  filterTarea:'';
  ngOnInit(): void {
    // this.cargarEstadosSlideToggle();

    this.obtenertareas();

  }
//   guardarEstadosSlideToggle(): void {
//     localStorage.setItem('estadosSlideToggle', JSON.stringify(this.estadosSlideToggle));
// }

//   cargarEstadosSlideToggle(): void {
//     const estados = JSON.parse(localStorage.getItem('estadosSlideToggle') || '{}');
//     this.videos.forEach(video => {
//         this.estadosSlideToggle[video.id] = estados[video.id] || false;
//     });
// }


  actualizar(id:number){
    this.router.navigate(['actualizar', id]);
  }

  eliminar(id:number){
    this.tareaserv.eliminar(id).subscribe(dato => {
      console.log(dato);
      this.obtenertareas();
    })
  }

  private obtenertareas(){
    this.tareaserv.obtenertareas().subscribe(dato => {

      this.tareas = dato;

    });
  }

  ver(id:number){
    this.router.navigate(['ver', id]);
  }


  // swichear(index: number, cambio: boolean){
  //   console.log(index);
  //   this.videoserv.swichear(index, cambio);
  // }

  // getSlideToggleState(index: number): boolean {
  //   const estadoGuardado = window.localStorage.getItem(`slideToggleState${index}`);
  //   return estadoGuardado ? JSON.parse(estadoGuardado) : false;
  // }


}
