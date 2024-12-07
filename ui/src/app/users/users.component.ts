import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
    selector: 'app-users',
    standalone: true,
    imports: [],
    templateUrl: './users.component.html',
    styleUrl: './users.component.css'
})
export class UsersComponent {

    constructor(private http: HttpClient) {
        this.http.post('http://localhost:8000/register/', 
                       {
                           username: 'John Doe',
                           password: 'password',
                       }
                      ).subscribe((data) => {
                          console.log(data);
                      });
    }
}
