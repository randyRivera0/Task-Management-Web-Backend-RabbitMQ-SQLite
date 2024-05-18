import { Component, OnInit } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { VideoServService } from 'src/app/video-serv.service';
import { FormBuilder, Validators } from '@angular/forms';
import { Tarea } from 'src/app/tarea';

@Component({
  selector : 'app-actualizar',
  templateUrl: './actualizar.component.html',
  styleUrls: ['./actualizar.component.css']
})
export class ActualizarComponent implements OnInit{
  form : FormGroup;

  id:number;
  title:string;
  tarea:Tarea = new Tarea();

  constructor(private tareaserv: VideoServService, private router: Router, private route:ActivatedRoute, private fb: FormBuilder){
    
  }


  ngOnInit(): void {

    this.id = this.route.snapshot.params['id'];
    this.tareaserv.obtenerporId(this.id).subscribe(dato =>{
      this.tarea = dato;
    }, error => console.log(error));
  }

  irAlalista(){
    this.router.navigate(['/obtener']);
  }

  onSubmit(){
    this.tareaserv.actualizar(this.id, this.tarea).subscribe( dato =>{
      this.irAlalista();
    }, error => console.log(error));
  }

}
