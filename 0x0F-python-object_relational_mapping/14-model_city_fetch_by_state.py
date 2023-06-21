#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa
    Prints table columns wherePrints table columns where
    'State.id is linked with City.state_id'
"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    objs = session.query(State.name, City.id, City.name).filter(
                         State.id == City.state_id)
    for obj in objs:
        print("{}: ({}) {}".format(obj[0], obj[1], obj[2]))

    session.close()
