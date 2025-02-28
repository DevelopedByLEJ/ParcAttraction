import { Component } from '@angular/core';
import { AttractionService } from '../Service/attraction.service';
import { CommonModule } from '@angular/common';
import { Observable } from 'rxjs';
import { AttractionInterface } from '../Interface/attraction.interface';
import { MatCardModule } from '@angular/material/card';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';
import { CritiqueInterface } from '../Interface/critique.interface';
import { CritiqueService } from '../Service/critique.service';
import { FormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-accueil',
  standalone: true,
  imports: [
    CommonModule,
    MatCardModule,
    MatListModule,
    MatIconModule,
    FormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule
  ],
  templateUrl: './accueil.component.html',
  styleUrl: './accueil.component.scss'
})
export class AccueilComponent {
  public attractions: Observable<AttractionInterface[]> = this.attractionService.getAllVisibleAttractionCritique();
  public showFormForAttraction: { [key: number]: boolean } = {}; // Permet de stocker l'état du formulaire pour chaque attraction
  public newCritique: CritiqueInterface = {
    texte: '',
    note: null,
    auteur: 'Anonyme',
    attraction_id: null
  };

  constructor(
    public attractionService: AttractionService,
    public critiqueService: CritiqueService
  ) {}

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

  toggleForm(attractionId: number | null) {
    console.log('Attraction ID reçu :', attractionId);  // Pour tester si attractionId est passé correctement
    if (attractionId !== null) {
      this.showFormForAttraction[attractionId] = !this.showFormForAttraction[attractionId];
      if (this.showFormForAttraction[attractionId]) {
        this.newCritique = { texte: '', note: null, auteur: 'Anonyme', attraction_id: attractionId };
        console.log('Formulaire initialisé pour attractionId :', attractionId);
      }
    } else {
      console.error('L\'attractionId est null ou indéfini');
    }
  }

  submitCritique(attractionId: number | null) {
    if (attractionId !== null) {
      this.newCritique.attraction_id = attractionId;
      console.log("Attraction ID avant l'envoi :", attractionId);
      console.log("Données envoyées :", this.newCritique);
  
      this.critiqueService.addCritique(this.newCritique).subscribe(
        response => {
          console.log("Critique ajoutée :", response);
          this.toggleForm(attractionId);
        },
        error => {
          console.error("Erreur lors de l'ajout de la critique :", error);
        }
      );
    } else {
      console.error("attractionId est null ! Impossible d'envoyer la critique.");
    }
  }    
}