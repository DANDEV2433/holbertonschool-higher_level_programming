#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username,
        password,
        database_name
    ), pool_pre_ping=True)
    # Création d'une classe de session configurée
    Session = sessionmaker(bind=engine)
    # Création d'une instance de session
    session = Session()
    # Requête pour récupérer tous les objets State et les trier par id
    state = session.query(State).order_by(State.id).first()
    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
