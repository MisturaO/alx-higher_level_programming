#!/usr/bin/python3
"""A script that lists all states with a name starting with 'N'"""

import MySQLdb
from sys import argv

"""so my code can only be executed when it's script is run
directly and not execute when imported into another module"""
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user="bukola",
                         db="hbtn_0e_0_usa", port=3306, passwd="bukola1091")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name\
                Like 'N%' ORDER BY states.id ASC")
    N_name = cur.fetchall()

    for names in N_name:
        print(names)
