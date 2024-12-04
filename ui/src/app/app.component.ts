import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { Workout, WorkoutsCodegenService } from './api';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
      RouterOutlet,
      HomeComponent,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
    constructor(
        private service: WorkoutsCodegenService,
    ) {
        this.service.workoutsList()
            .subscribe((response: Workout[]): void => {
                console.log(response);
            });
    }
}
