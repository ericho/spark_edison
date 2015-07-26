import mysql.connector
from datetime import datetime
import random
import time

DB_USER = "root"
PASSWORD = "edison123"
DB_NAME = "edison"
DB_SERVER = "localhost"

class MySQLConnector(object):
    """ A connector to MySQL database """

    def __init__(self):
        self.meas_insert = ("INSERT INTO meas (node_id, date, mea, type_mea) "
                            "VALUES (%s, %s, %s, %s)")

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(user=DB_USER, 
                                               password=PASSWORD, 
                                               host=DB_SERVER, 
                                               database=DB_NAME)
        except mysql.connector.Error as err:
            print "Failed to connect"
            print err

    def disconnect(self):
        cnx.close()

    def insert_data(self, insert_stmt, values):
        cursor = self.cnx.cursor()
        try:
            cursor.execute(insert_stmt, values);
            self.cnx.commit()
        except Exception as e:
            print "Failed to insert data"
            print e
        cursor.close()


if __name__ == "__main__":
    conn = MySQLConnector()
    try:
        conn.connect()
    except Exception as e:
        print "Unable to connect to server"
        print e

    # Generating random numbers;

    for i in range(0, 1000):
        val = random.randint(10, 40)
        type_data = random.randint(1, 2)
        values = (1, datetime.now(), float(val), type_data)
        print "Inserting : {0}:".format(values)
        conn.insert_data(conn.meas_insert, values)
        time.sleep(0.3)

