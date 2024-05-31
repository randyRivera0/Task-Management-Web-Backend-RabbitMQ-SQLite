import { Component, OnInit } from '@angular/core';
import { Route, Router } from '@angular/router';
import { Tarea } from 'src/app/tarea';
import { VideoServService } from 'src/app/video-serv.service';

@Component({
  selector: 'app-dashempleado',
  templateUrl: './dashempleado.component.html',
  styleUrls: ['./dashempleado.component.css']
})
export class DashempleadoComponent  implements OnInit{

  tareas: Tarea[];

  filterTarea:'';

  constructor( private tareaserv: VideoServService, private router: Router ) { }

  ngOnInit(): void {
    this.obtenertareas();
      
  }

  private obtenertareas(){
    this.tareaserv.obtenertareas().subscribe(dato => {

      this.tareas = dato;

    });
  }

}
