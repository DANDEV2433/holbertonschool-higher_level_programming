#!/usr/bin/python3
"""
script that lists all the State objects in the hbtn_0e_6_usa database
"""
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    # Récupérer les arguments de ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Créer le moteur de base de données avec le port spécifié
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username,
        password,
        database_name
    ), pool_pre_ping=True)
    # Créer une session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête sur les objets State et les afficher
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))

    # Fermer la session
    session.close()
