import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'filter'
})
export class FilterPipe implements PipeTransform {

  transform(value: any, ...arg: any): any {
    const resultvid=[];
    for(const video of value){
      if(video.title.indexOf(arg) > -1){
        resultvid.push(video);
      };
    };

    return resultvid;

  }

}
