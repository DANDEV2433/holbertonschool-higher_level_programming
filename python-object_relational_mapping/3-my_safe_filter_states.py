#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host='localhost',
        user=mysql_username,
        password=mysql_password,
        database=database_name,
        port=3306
    )

    # Création d'un objet curseur
    cursor = db.cursor()
    # Exécuter la requête SQL
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"

    cursor.execute(query, (state_name_searched + '%',))

    # Récupérer tous les résultats de la requête
    states = cursor.fetchall()

    # Afficher chaque état
    for state in states:
        print(state)
    # Fermer le curseur et la connexion
    cursor.close()
    db.close()
