#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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
                    SELECT cities.name
                    FROM cities
                    JOIN states ON cities.state_id = states.id
                    WHERE states.name = %s
                    ORDER BY cities.id ASC;
    """, (state_name,))

    # Récupérer tous les résultats de la requête
    cities = cursor.fetchall()
    print(", ".join([city[0] for city in cities]))
    # Fermer le curseur et la connexion
    cursor.close()
    db.close()
