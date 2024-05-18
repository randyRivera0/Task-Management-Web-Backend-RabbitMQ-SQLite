import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Tarea } from './tarea';


@Injectable({
  providedIn: 'root'
})
export class VideoServService {

  //url obtiene el listado de todos los videos en el backend
  private baseURL ="http://localhost:8090/tareas";

  constructor(private httpClient: HttpClient) { }

  //con esto obtengo los empleados  
  obtenertareas():Observable<Tarea[]>{
    return this.httpClient.get<Tarea[]>(`${this.baseURL}/obtener`);
  }

  obtenerporId(id: number): Observable<Tarea>{
    return this.httpClient.get<Tarea>(`${this.baseURL}/obtener/${id}`);
  } 


  //esto metodo sirve para registrar un video nuevo
  agregartarea(tarea: Tarea): Observable<Object>{

    return this.httpClient.post(`${this.baseURL}/agregar`, tarea);

  }

  actualizar(id:number, tarea:Tarea) : Observable<Object>{
    return this.httpClient.put(`${this.baseURL}/modificar/${id}`,tarea);
  }

  eliminar(id:number): Observable<Object>{
    return this.httpClient.delete(`${this.baseURL}/borrar/${id}`);
  }

//   indiceActual: number | null = null;

// swichear(index:number, cambio: boolean){
//     this.indiceActual = index;
//     window.localStorage.setItem(`slideToggleState${index}`, JSON.stringify(cambio));
//   }

  
}
