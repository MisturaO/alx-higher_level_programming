#!/usr/bin/python3
"""This script script prints the first State object from the
database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    path_to_db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                 argv[1], argv[2], argv[3])

    engine = create_engine(path_to_db)
    Session = sessionmaker(bind=engine)
    session = Session()

    if session.query(State) is None:
        print('Nothing')
    else:
        instance = session.query(State).first()
        print("{}: {}".format(instance.id, instance.name))
