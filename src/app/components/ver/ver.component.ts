import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Video } from 'src/app/video';
import { VideoServService } from 'src/app/video-serv.service';

@Component({
  selector: 'app-ver',
  templateUrl: './ver.component.html',
  styleUrls: ['./ver.component.css']
})
export class VerComponent implements OnInit{

  id:number;
  video: Video;
  

  constructor(private route:ActivatedRoute, private videoserv: VideoServService){}

  ngOnInit(): void {
      this.id = this.route.snapshot.params['id'];
      this.video = new Video();
      this.videoserv.obtenerporId(this.id).subscribe(dato => {
        this.video = dato;
      });
  }

}
