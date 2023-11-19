#!/usr/bin/python3
"""  script that lists all State objects from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# code should not execute
if __name__ == '__main__':

    # create sqlalchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # session configuration
    session = sessionmaker(bind=engine)
    # create a session
    session = session()
    Base.metadata.create_all(engine)

    s_tate = session.query(State).order_by(State.id).all()
    for state in s_tate:
        print("{}: {}".format(state.id, state.name))
    session.close()
