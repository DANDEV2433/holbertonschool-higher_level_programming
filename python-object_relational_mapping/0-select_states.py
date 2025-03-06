#!/usr/bin/env python3
"""
lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connexion à la base de données MySQL
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name)

    # Création d'un objet curseur
    cursor = db.cursor()

    # Exécuter la requête SQL
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupérer tous les résultats de la requête
    states = cursor.fetchall()

    # Afficher chaque état
    for state in states:
        print(state)

    # Fermer le curseur et la connexion
    cursor.close()
    db.close()
