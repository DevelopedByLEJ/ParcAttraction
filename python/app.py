from flask import Flask, jsonify, request
from flask_cors import CORS

import mariadb
import request.request as req
import controller.auth.auth as user
import controller.attraction as attraction
import controller.critique as critique

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

# Attraction
@app.post('/attraction')
def addAttraction():
    print("okok", flush=True)
    # Fonction vérif token
    #checkToken = user.check_token(request)
    #if (checkToken != True):
        #return checkToken

    json = request.get_json()
    retour = attraction.add_attraction(json)
    if (retour):
        return jsonify({"message": "Element ajouté.", "result": retour}), 200
    return jsonify({"message": "Erreur lors de l'ajout.", "result": retour}), 500

@app.get('/attraction')
def getAllAttraction():
    result = attraction.get_all_attraction()
    return result, 200

@app.get('/attraction/visible')
def getAllVisibleAttraction():
    result = attraction.get_all_visible_attraction()
    return result, 200

@app.get('/attraction/<int:index>')
def getAttraction(index):
    result = attraction.get_attraction(index)
    return result, 200

@app.delete('/attraction/<int:index>')
def deleteAttraction(index):

    # Fonction vérif token
    checkToken = user.check_token(request)
    if (checkToken != True):
        return checkToken

    json = request.get_json()
    
    if (attraction.delete_attraction(index)):
        return "Element supprimé.", 200
    return jsonify({"message": "Erreur lors de la suppression."}), 500

@app.post('/login')
def login():
    json = request.get_json()

    if (not 'name' in json or not 'password' in json):
        result = jsonify({'messages': ["Nom ou/et mot de passe incorrect"]})
        return result, 400
    
    cur, conn = req.get_db_connection()
    requete = f"SELECT * FROM users WHERE name = '{json['name']}' AND password = '{json['password']}';"
    cur.execute(requete)
    records = cur.fetchall()
    conn.close()

    result = jsonify({"token": user.encode_auth_token(list(records[0])[0]), "name": json['name']})
    return result, 200

#Test Connexion DB
@app.get('/test-db')
def test_db():
    try:
        conn = mariadb.connect(
            user="mysqlusr",
            password="mysqlpwd",
            host="database",
            port=3306,
            database="parc"
        )
        cur = conn.cursor()
        cur.execute("SELECT 1")  # Juste un test
        return {"message": "Connexion OK"}, 200
    except mariadb.Error as e:
        return {"error": str(e)}, 500

#Critique
@app.post('/critique')
def addCritique():
    print("okok", flush=True)

    json = request.get_json()
    print("Données reçues :", json, flush=True)  # Vérifie ce qui arrive

    if not json:
        return jsonify({"message": "Erreur : Aucune donnée reçue."}), 400
    
    if "attraction_id" not in json or json['attraction_id'] is None:
        return jsonify({"message": "Erreur : attraction_id est requis."}), 400

    retour = critique.add_critique(json)
    if retour:
        return jsonify({"message": "Element ajouté.", "result": retour}), 200
    return jsonify({"message": "Erreur lors de l'ajout.", "result": retour}), 500


@app.delete('/critique/<int:index>')
def deleteCritique(index):

    # Fonction vérif token
    #checkToken = user.check_token(request)
    #if (checkToken != True):
        #return checkToken
    
    if (critique.delete_critique(index)):
        return "Element supprimé.", 200
    return jsonify({"message": "Erreur lors de la suppression."}), 500

@app.get('/critique')
def getAllCritique():
    result = critique.get_all_critique()
    return result, 200

@app.get('/attraction/visible/critique')
def getAttractionCritique():
    result = attraction.get_all_visible_attraction_with_critique()
    return result, 200