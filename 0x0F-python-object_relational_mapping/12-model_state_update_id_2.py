#!/usr/bin/python3
"""
This script changes the name of a State
object from the database hbtn_0e_6_usa:
    Change the name of the State where id = 2 to New
"""

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

    change_name = session.query(State)\
        .filter(State.id == 2).first()
    change_name.name = 'New Mexico'
    session.commit()
