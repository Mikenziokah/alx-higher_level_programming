#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

# code should not be excuted
if __name__ == '__main__':

    # make connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.excute("SELECT *FROM states")

    rows = cur.fetchall()
    for x in rows:
        print(x)

        # clear the process
        cur.close()
        db.close()
