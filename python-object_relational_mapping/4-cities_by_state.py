#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

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
    cursor.execute("""
                    SELECT cities.id, cities.name, states.name
                    FROM cities
                    JOIN states ON cities.state_id = states.id
                    ORDER BY cities.id ASC;
    """)

    # Récupérer tous les résultats de la requête
    cities = cursor.fetchall()

    # Afficher chaque state_id, city, state
    for city in cities:
        print(city)
    # Fermer le curseur et la connexion
    cursor.close()
    db.close()
