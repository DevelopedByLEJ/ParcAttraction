import request.request as req

def add_critique(data):
    print(data, flush=True)

    if "texte" not in data or data["texte"] == "":
        return False

    if "note" not in data or data["note"] is None:
        return False

    if "auteur" not in data or data["auteur"] == "":
        return False

    if "attraction_id" not in data or data["attraction_id"] is None:
        return False

    # Séparer l'auteur en nom et prénom
    auteur_parts = data["auteur"].split(" ", 1)
    nom = auteur_parts[0]
    prenom = auteur_parts[1] if len(auteur_parts) > 1 else ""

    if "critique_id" in data and data["critique_id"]:
        requete = f"UPDATE critique SET texte='{data['texte']}', note='{data['note']}', nom='{nom}', prenom='{prenom}', attraction_id='{data['attraction_id']}'"
        req.insert_in_db(requete)
        id = data['critique_id']
    else:
        requete = "INSERT INTO critique (texte, note, nom, prenom, attraction_id) VALUES (?, ?, ?, ?, ?);"
        id = req.insert_in_db(requete, (data["texte"], data["note"], nom, prenom, data["attraction_id"]))

    return id

def delete_critique(id):
  if(not id):
    return False
  
  req.delete_from_db("DELETE FROM critique WHERE critique_id = ?", (id,))

  return True

def get_all_critique():
  json = req.select_from_db("SELECT * FROM critique")

  return json