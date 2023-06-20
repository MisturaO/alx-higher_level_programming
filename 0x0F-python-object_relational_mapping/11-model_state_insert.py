#!/usr/bin/python3
"""A script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
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

    new_state_obj = State(name='Louisiana')
    session.add(new_state_obj)
    session.commit()
    print(new_state_obj.id)
