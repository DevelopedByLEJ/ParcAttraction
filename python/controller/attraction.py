import request.request as req

def add_attraction(data):
    print(data, flush=True)
    if (not "nom" in data or data["nom"] == ""):
        return False
    
    if (not "description" in data or data["description"] == ""):
        return False

    if (not "difficulte" in data or data["difficulte"] is None):
        return False

    if (not "visible" in data):
        data["visible"] = True

    if ("attraction_id" in data and data["attraction_id"]):
      requete = f"UPDATE attraction SET nom='{data['nom']}', description='{data['description']}', difficulte={data['difficulte']}, visible={data['visible']} WHERE attraction_id = {data['attraction_id']}"
      req.insert_in_db(requete)
      id = data['attraction_id']
    else:
      requete = "INSERT INTO attraction (nom, description, difficulte, visible) VALUES (?, ?, ?, ?);"
      id = req.insert_in_db(requete, (data["nom"], data["description"], data["difficulte"], data["visible"]))

    return id

def get_all_attraction():
    json = req.select_from_db("SELECT * FROM attraction")
    
    return json

def get_all_visible_attraction():
    json = req.select_from_db("SELECT * FROM attraction WHERE visible = 1")
    
    return json

def get_attraction(id):
    if (not id):
        return False

    json = req.select_from_db("SELECT * FROM attraction WHERE attraction_id = ?", (id,))

    if len(json) > 0:
        return json[0]
    else:
        return []

def delete_attraction(id):
    if (not id):
        return False

    req.delete_from_db("DELETE FROM attraction WHERE attraction_id = ?", (id,))

    return True

def get_all_visible_attraction_with_critique():
    requete = """
    SELECT a.attraction_id, a.nom, a.description, a.difficulte, 
           c.critique_id, c.texte AS critique, c.note, c.nom AS auteur_nom, c.prenom AS auteur_prenom
    FROM attraction a
    LEFT JOIN critique c ON a.attraction_id = c.attraction_id
    WHERE a.visible = 1
    ORDER BY a.attraction_id, c.critique_id;
    """

    result = req.select_from_db(requete)
    
    print("Résultat SQL:", result, flush=True)  # Affiche le format des données

    attractions = {}
    for row in result:
        print("Ligne retournée:", row, flush=True)  # Vérifie la structure des données
        attraction_id = row["attraction_id"]  # Modifier ici (avant: row[0])
        
        if attraction_id not in attractions:
            attractions[attraction_id] = {
                "attraction_id": attraction_id,
                "nom": row["nom"],
                "description": row["description"],
                "difficulte": row["difficulte"],
                "critiques": []
            }
        if row["critique_id"] is not None:
            attractions[attraction_id]["critiques"].append({
                "critique_id": row["critique_id"],
                "texte": row["critique"],
                "note": row["note"],
                "auteur": f"{row['auteur_nom']} {row['auteur_prenom']}"
            })

    return list(attractions.values())