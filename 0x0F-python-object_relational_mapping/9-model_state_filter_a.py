#!/usr/bin/python3
"""script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa"""

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

    s_tate = session.query(State).filter(State.name.like('%a%'))\
                                 .order_by(State.id).all()
    for state in s_tate:
        print("{}: {}".format(state.id, state.name))
    session.close()