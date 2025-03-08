#!/usr/bin/python3
"""
script that lists all the State objects in the hbtn_0e_6_usa database
"""
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    ),
        pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()
states = session.query(State).order_by(State.id).all()

for state in states:
    print('{}: {}'.format(state.id, state.name))

session.close()
