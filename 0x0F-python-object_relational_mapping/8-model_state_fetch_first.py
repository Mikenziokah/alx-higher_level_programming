#!/usr/bin/python3
""" script that prints the first State object from
the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

# code should not execute
if __name__ == '__main__':

    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create session
    session = sessionmaker()
    session = session(bind=engine)

    Base.metadata.create_all(engine)
    s_tate = session.query(State).order_by(State.id).first()

    if s_tate:
        print("{}: {}".format(s_tate.id, s_tate.name))
    else:
        print("Nothing")
    session.close()
