#!/usr/bin/python3
"""
script that lists all the State objects in the hbtn_0e_6_usa database
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
# créer un moteur de base de données
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
    sys.argv[1],
    sys.argv[2],
    sys.argv[3]
    ),
    pool_pre_ping=True)
# Création de toutes les tables
# définies par les sous-classes de Base (si elles n'existent pas déjà)
Base.metadata.create_all(engine)
# Création d'une classe de session configurée
Session = sessionmaker(bind=engine)
# Création d'une instance de session
session = Session()
# Requête pour récupérer tous les objets State et les trier par id
states = session.query(State).order_by(State.id).all()

for State in states:
    print('{}: {}'.format(State.id, State.name))

session.close()
