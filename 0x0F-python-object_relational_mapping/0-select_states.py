#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

"""So my code can only be executed when it's script is run 
directly and not execute when imported into another module"""
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                            port=3306, passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states")
    row = cur.fetchall()

    for state in row:
        print(state)
