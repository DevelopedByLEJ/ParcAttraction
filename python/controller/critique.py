import request.request as req

def add_critique(data):
  print(data, flush=True)
  if(not "objet" in data or data["objet"] == ""):
    return False
  
  if(not "description" in data or data["description"] == ""):
    return False
  
  if("critique_id" in data and data["critique_id"]):
    requete = f"UPDATE critique SET objet='{data['objet']}', description='{data['description']}'"
    req.insert_in_db(requete)
    id = data['critique_id']
  else:
    requete = "INSERT INTO critique (objet, description) VALUES (?, ?);"
    id = req.insert_in_db(requete, (data["objet"], data["description"]))
  
  return id

def delete_critique(id):
  if(not id):
    return False
  
  req.delete_from_db("DELETE FROM critique WHERE critique_id = ?", (id,))

  return True