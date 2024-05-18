import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Tarea } from 'src/app/tarea';
import { VideoServService } from 'src/app/video-serv.service';

@Component({
  selector: 'app-ver',
  templateUrl: './ver.component.html',
  styleUrls: ['./ver.component.css']
})
export class VerComponent implements OnInit{

  id:number;
  tarea: Tarea;

  constructor(private route:ActivatedRoute, private tareaserv: VideoServService){}

  ngOnInit(): void {
      this.id = this.route.snapshot.params['id'];
      this.tarea = new Tarea();
      this.tareaserv.obtenerporId(this.id).subscribe(dato => {
        this.tarea = dato;
      });
  }

}
