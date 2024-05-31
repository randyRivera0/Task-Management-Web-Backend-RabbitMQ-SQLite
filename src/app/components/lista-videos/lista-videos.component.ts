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

  // progresssSlideToggle: { [key: number]: boolean } = {};
  tareas: Tarea[];

  
  constructor(private tareaserv: VideoServService,  private router: Router){}
  filterTarea:'';
  ngOnInit(): void {
    // this.cargarprogresssSlideToggle();

    this.obtenertareas();

  }
//   guardarprogresssSlideToggle(): void {
//     localStorage.setItem('progresssSlideToggle', JSON.stringify(this.progresssSlideToggle));
// }

//   cargarprogresssSlideToggle(): void {
//     const progresss = JSON.parse(localStorage.getItem('progresssSlideToggle') || '{}');
//     this.videos.forEach(video => {
//         this.progresssSlideToggle[video.id] = progresss[video.id] || false;
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
  //   const progressGuardado = window.localStorage.getItem(`slideToggleState${index}`);
  //   return progressGuardado ? JSON.parse(progressGuardado) : false;
  // }


}
