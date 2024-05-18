import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Tarea } from 'src/app/tarea';
import { VideoServService } from 'src/app/video-serv.service';

@Component({
  selector: 'app-agregarvid',
  templateUrl: './agregarvid.component.html',
  styleUrls: ['./agregarvid.component.css']
})
export class AgregarvidComponent implements OnInit {

  tarea: Tarea = new Tarea();

  constructor(private tareaServ : VideoServService, private router:Router){}

  ngOnInit(): void {

    console.log(this.tarea);
      
  }
  //hola 

  guardartarea(){
    this.tareaServ.agregartarea(this.tarea).subscribe(dato => {
      console.log(dato);
      this.irAlalista();

    }, error => console.log(error));
  }

  irAlalista(){
    this.router.navigate(['/obtener']);
  }
  onSubmit(){

    this.guardartarea();
    
  }

}
