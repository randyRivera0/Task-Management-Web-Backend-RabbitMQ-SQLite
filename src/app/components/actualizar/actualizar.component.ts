import { Component, OnInit } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Video } from 'src/app/video';
import { VideoServService } from 'src/app/video-serv.service';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector : 'app-actualizar',
  templateUrl: './actualizar.component.html',
  styleUrls: ['./actualizar.component.css']
})
export class ActualizarComponent implements OnInit{
  form : FormGroup;

  id:number;
  title:string;
  video:Video = new Video();

  constructor(private videoserv: VideoServService, private router: Router, private route:ActivatedRoute, private fb: FormBuilder){
    
  }


  ngOnInit(): void {

    this.id = this.route.snapshot.params['id'];
    this.videoserv.obtenerporId(this.id).subscribe(dato =>{
      this.video = dato;
    }, error => console.log(error));
  }

  irAlalista(){
    this.router.navigate(['/obtener']);
  }

  onSubmit(){
    this.videoserv.actualizar(this.id, this.video).subscribe( dato =>{
      this.irAlalista();
    }, error => console.log(error));
  }

}
