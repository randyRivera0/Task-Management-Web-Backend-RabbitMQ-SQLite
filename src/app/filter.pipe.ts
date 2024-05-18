import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'filter'
})
export class FilterPipe implements PipeTransform {

  transform(value: any, ...arg: any): any {
    const resulttar=[];
    for(const tarea of value){
      if(tarea.title.indexOf(arg) > -1){
        resulttar.push(tarea);
      };
    };

    return resulttar;

  }

}
