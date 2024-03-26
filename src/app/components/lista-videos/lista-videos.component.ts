import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Video } from 'src/app/video';
import { VideoServService } from 'src/app/video-serv.service';
import {MatTableDataSource} from '@angular/material/table';
import {MatFormFieldModule} from '@angular/material/form-field';

@Component({
  selector: 'app-lista-videos',
  templateUrl: './lista-videos.component.html',
  styleUrls: ['./lista-videos.component.css']
})
export class ListaVideosComponent implements OnInit {

  videos: Video[];
  
  constructor(private videoserv: VideoServService,  private router: Router){}
  filterVideo:'';
  ngOnInit(): void {

    this.obtenervideos();

  }

  actualizar(id:number){
    this.router.navigate(['actualizar', id]);
  }

  eliminar(id:number){
    this.videoserv.eliminar(id).subscribe(dato => {
      console.log(dato);
      this.obtenervideos();
    })
  }

  private obtenervideos(){
    this.videoserv.obtenervideos().subscribe(dato => {

      this.videos = dato;

    });
  }

  ver(id:number){
    this.router.navigate(['ver', id]);
  }




}
