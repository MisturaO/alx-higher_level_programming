#!/usr/bin/python3
"""This script prints the State object with the name
passed as argument from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


if __name__ == "__main__":
    path_to_db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'\
                  .format(argv[1], argv[2], argv[3])

    engine = create_engine(path_to_db, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    row = session.query(State).filter(State.name == argv[4]).first()
    if row is None:
        print("Not found")
    else:
        print(row.id)
