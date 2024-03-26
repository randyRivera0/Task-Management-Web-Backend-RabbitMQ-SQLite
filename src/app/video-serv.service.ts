import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Video } from './video';

@Injectable({
  providedIn: 'root'
})
export class VideoServService {

  //url obtiene el listado de todos los videos en el backend
  private baseURL ="http://localhost:8090/videos";

  constructor(private httpClient: HttpClient) { }

  //con esto obtengo los empleados  
  obtenervideos():Observable<Video[]>{
    return this.httpClient.get<Video[]>(`${this.baseURL}/obtener`);
  }

  obtenerporId(id: number): Observable<Video>{
    return this.httpClient.get<Video>(`${this.baseURL}/obtener/${id}`);
  } 


  //esto metodo sirve para registrar un video nuevo
  agregarvideo(video: Video): Observable<Object>{

    return this.httpClient.post(`${this.baseURL}/agregar`, video);

  }

  actualizar(id:number, video:Video) : Observable<Object>{
    return this.httpClient.put(`${this.baseURL}/modificar/${id}`,video);
  }

  eliminar(id:number): Observable<Object>{
    return this.httpClient.delete(`${this.baseURL}/borrar/${id}`);
  }
  
}
