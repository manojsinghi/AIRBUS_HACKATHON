import MySQLdb
import os
import warnings
import sys

warnings.filterwarnings('ignore')


def connection(data):
    db = MySQLdb.connect("localhost", "root", "ayushpatidar@04", "airbus")
    print("DB conencted")

    cur = db.cursor()

    try:
        sql = "SHOW TABLES LIKE 'AIRLINE_DATA'"
        cur.execute(sql)

        rs = cur.fetchone()
        print(rs)

        if rs:
            print("table is already there")
            sql = """INSERT INTO AIRLINE_DATA(AIRLINE_NAME, MSN, HARNESS_LENGTH, GROSS_WEIGHT,
                   ATMOSPHERIC_PRESSURE, ROOM_TEMPERATURE, AIRPORT,
                   FUEL_CAPACITY_ON_LEFT, FUEL_CAPACITY_ON_RIGHT, FUEL_QUANTITY_ON_LEFT,
                   FUEL_QUANTITY_ON_RIGHT, FLIGHT_NUMBER)
               VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            cur.execute(sql, data)
            db.commit()

        else:
            sql ="""CREATE TABLE AIRLINE_DATA(AIRLINE_NAME VARCHAR(100) NOT NULL, MSN INT NOT NULL, HARNESS_LENGTH INT NOT NULL, GROSS_WEIGHT FLOAT NOT NULL, ATMOSPHERIC_PRESSURE FLOAT NOT NULL,
            ROOM_TEMPERATURE FLOAT NOT NULL, AIRPORT VARCHAR(100) NOT NULL, FUEL_CAPACITY_ON_LEFT FLOAT NOT NULL,
             FUEL_CAPACITY_ON_RIGHT FLOAT NOT NULL, FUEL_QUANTITY_ON_LEFT FLOAT NOT NULL, FUEL_QUANTITY_ON_RIGHT FLOAT NOT NULL, FLIGHT_NUMBER INT NOT NULL, PRIMARY KEY(MSN))"""

            cur.execute(sql)
            print("table created")
            db.commit()

            sql = """INSERT INTO AIRLINE_DATA(AIRLINE_NAME, MSN, HARNESS_LENGTH, GROSS_WEIGHT,
                               ATMOSPHERIC_PRESSURE, ROOM_TEMPERATURE, AIRPORT,
                               FUEL_CAPACITY_ON_LEFT, FUEL_CAPACITY_ON_RIGHT, FUEL_QUANTITY_ON_LEFT,
                               FUEL_QUANTITY_ON_RIGHT, FLIGHT_NUMBER)
                           VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            cur.execute(sql, data)
            db.commit()

            print("results added")




    except Exception as e:
        print("error while creating table", e)


    db.close()