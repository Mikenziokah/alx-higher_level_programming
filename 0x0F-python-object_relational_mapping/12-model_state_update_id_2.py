#!/usr/bin/python3
""" script that changes the name of a State object
from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

# code should not execute
if __name__ == '__main__':

    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # configure session
    session = sessionmaker(bind=engine)
    # create session
    session = session()
    Base.metadata.create_all(engine)

    state_update = session.query(State).filter_by(id='2').first()
    state_update.name = "New Mexico"
    # commit and close session
    session.commit()
    session.close()
