import { Component } from '@angular/core';
import { AttractionService } from '../Service/attraction.service';
import { CommonModule } from '@angular/common';
import { Observable } from 'rxjs';
import { AttractionInterface } from '../Interface/attraction.interface';
import { MatCardModule } from '@angular/material/card';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-accueil',
  standalone: true,
  imports: [CommonModule, MatCardModule, MatListModule, MatIconModule],
  templateUrl: './accueil.component.html',
  styleUrl: './accueil.component.scss'
})
export class AccueilComponent {

  constructor(public attractionService: AttractionService)
  {}
  
  public attractions: Observable<AttractionInterface[]> = this.attractionService.getAllVisibleAttractionCritique();

  getStarRating(note: number): string[] {
    const stars = [];
    for (let i = 1; i <= 5; i++) {
      if (i <= note) {
        stars.push('star'); // Étoile pleine
      } else {
        stars.push('star_border'); // Étoile vide
      }
    }
    return stars;
  }
}