import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Video } from 'src/app/video';
import { VideoServService } from 'src/app/video-serv.service';

@Component({
  selector: 'app-agregarvid',
  templateUrl: './agregarvid.component.html',
  styleUrls: ['./agregarvid.component.css']
})
export class AgregarvidComponent implements OnInit {

  video: Video = new Video();

  constructor(private videoServ : VideoServService, private router:Router){}
  ngOnInit(): void {

    console.log(this.video);
      
  }
  //hola 

  guardarvideo(){
    this.videoServ.agregarvideo(this.video).subscribe(dato => {
      console.log(dato);
      this.irAlalista();

    }, error => console.log(error));
  }

  irAlalista(){
    this.router.navigate(['/obtener']);
  }
  onSubmit(){

    this.guardarvideo();
    
  }

}
