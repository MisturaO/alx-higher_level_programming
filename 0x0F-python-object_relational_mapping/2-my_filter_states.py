#!/usr/bin/python3
"""
This script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where argument matches the value in
row 'name' of the table.
"""
import MySQLdb
from sys import argv


"""This script runs only if it is run directly as
a script and not imported into another module"""
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states\
    WHERE NAME LIKE '{}'\
    ORDER BY states.id ASC".format(argv[4]))

    rows = cur.fetchall()

    for row in rows:
        # if argv[4] == row[1]:
        print(row)
