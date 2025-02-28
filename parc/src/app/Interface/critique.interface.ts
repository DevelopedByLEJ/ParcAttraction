export interface CritiqueInterface {
  critique_id?: number,
  attraction_id: number | null,
  texte: string | null,
  note: number | null,
  auteur: string
}