import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  signupUsers :any[] = [];
  signupObj:any = {
    username: '',
    password: '',
    role: ''
  };
  loginObj: any = {
    username: '',
    password: ''
  };

  constructor(private router: Router){}

  ngOnInit(): void {
    const localdata = localStorage.getItem('signupUsers');
    if(localdata != null){
      this.signupUsers = JSON.parse(localdata);
    }
      
  }

  onSignUp(){

    this.signupUsers.push(this.signupObj);
    localStorage.setItem('signupUsers', JSON.stringify(this.signupUsers));
    this.signupObj = {
      username:'',
      password:'',
      role:''
    };

  }

  onLogin(){
    const isUserExist = this.signupUsers.find( m => m.username == this.loginObj.username && m.password == this.loginObj.password);
    if ( isUserExist != undefined ){
      alert('login succes');
      this.router.navigate(['/inicio']);
    } else {
      alert('wrong credentials');
    }
  }

  

}
