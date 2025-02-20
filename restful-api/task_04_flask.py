#!/usr/bin/python3
"""
 Develop a Simple API using Python with Flask
"""
# Flask pour créer l'application web
from flask import Flask
# jsonify pour convertir les dictionnaires Python en JSON
from flask import jsonify
# request pour traiter les requêtes HTTP
from flask import request

# # une instance de l'application Flask
app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_users():
    # retourne une liste de tous les noms d'utilisateur
    # en extrayant les clés du dictionnaire users sous forme JSON
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    # extrait les données JSON de la requête HTTP reçue
    data = request.get_json()
    # récupère la valeur associée à la clé "username"
    # dans l'objet JSON extrait.
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = data
    # ajoute l'entrée pour username
    # dans le dictionnaire users avec les données JSON extraites.
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
