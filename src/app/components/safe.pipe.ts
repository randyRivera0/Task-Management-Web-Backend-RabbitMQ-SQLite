import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'safe'
})
export class SafePipe implements PipeTransform {

  transform( videourl:string ):any{
    return this.sanitizeurl(videourl);
  }

  private sanitizeurl(videourl:string):any{
    return videourl.replace(/^(http(s)?:\/\/)?(www\.)?/, '//');
  }

}
