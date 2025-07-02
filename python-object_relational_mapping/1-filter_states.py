#!/usr/bin/python3
'''
liste tous les États dont le nom commence par
un N majuscule à partir de la base de données hbtn_0e_0_usa
'''
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    )
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
