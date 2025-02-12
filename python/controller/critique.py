import request.request as req

def add_critique(data):
  print(data, flush=True)
  if(not "texte" in data or data["texte"] == ""):
    return False
  
  if (not "note" in data or data["note"] is None):
      return False
  
  if(not "nom" in data or data["nom"] == ""):
    return False
  
  if(not "prenom" in data or data["prenom"] == ""):
    return False
  
  if(not "attraction_id" in data or data["attraction_id"] is None):
    return False
  
  if("critique_id" in data and data["critique_id"]):
    requete = f"UPDATE critique SET texte='{data['texte']}', note='{data['note']}', nom='{data['nom']}', prenom='{data['prenom']}', attraction_id='{data['attraction_id']}'"
    req.insert_in_db(requete)
    id = data['critique_id']
  else:
    requete = "INSERT INTO critique (texte, note, nom, prenom, attraction_id) VALUES (?, ?, ?, ?, ?);"
    id = req.insert_in_db(requete, (data["texte"], data["note"], data["nom"], data["prenom"], data["attraction_id"]))
  
  return id

def delete_critique(id):
  if(not id):
    return False
  
  req.delete_from_db("DELETE FROM critique WHERE critique_id = ?", (id,))

  return True

def get_all_critique():
  json = req.select_from_db("SELECT * FROM critique")

  return json