import { CritiqueInterface } from "./critique.interface"

export interface AttractionInterface {
    attraction_id: number | null,
    nom: string,
    description: string, 
    difficulte: number,
    visible: boolean,
    critiques: CritiqueInterface[]
}