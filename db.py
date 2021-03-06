import sqlite3
import os

def connector():
    if os.path.isfile("airport.db"):
        connection = sqlite3.connect("airport.db")
        return connection
    connection = sqlite3.connect("airport.db")
    curs = cursor(connection)
    curs.execute(''' CREATE TABLE "flights" (
	"number"	TEXT NOT NULL,
	"direction"	TEXT NOT NULL,
	"all_seats"	INTEGER NOT NULL,
	"free_seats"	INTEGER NOT NULL,
	"date"	TEXT NOT NULL,
	PRIMARY KEY("number")
    ) ''')

    curs.execute(''' CREATE TABLE "passenger" (
	"surname"	TEXT NOT NULL,
	"number"	TEXT NOT NULL,
	"class"	TEXT NOT NULL,
	"baggage"	REAL NOT NULL,
	"cost"	REAL NOT NULL
    ) ''')

    connection.commit()
    
    return connection

def cursor(connection):
    crsr = connection.cursor()
    return crsr

def insert_flight(data):
    connection = connector()
    curs = cursor(connection)

    curs.execute("SELECT number FROM flights WHERE number = '{}'".format(data[0]))

    rows = curs.fetchall()
    if len(rows) == 0:
        curs.execute("INSERT INTO flights (number, direction, all_seats, free_seats, date) VALUES (?, ?, ?, ?, ?);", 
        (data[0], data[1], data[2], data[3], data[4]))

        connection.commit()
        connection.close()
        return 0
    else:
        return -1

def insert_passenger(data):
    connection = connector()
    curs = cursor(connection)

    curs.execute("INSERT INTO passenger (surname, number, class, baggage, cost) VALUES (?, ?, ?, ?, ?);", 
    (data[0], data[1], data[2], data[3], data[4]))

    connection.commit()
    connection.close()

def select_free_seats(number):
    connection = connector()
    curs = cursor(connection)

    curs.execute("SELECT free_seats FROM flights WHERE number = '{}'".format(number))
    rows = curs.fetchall()
    connection.close()
    if len(rows) != 0:
        return rows[0][0]
    else:
        return -1

def all_baggage_cost(number):
    connection = connector()
    curs = cursor(connection)

    sum = 0
    curs.execute("SELECT number FROM flights WHERE number = '{}'".format(number))
    rows = curs.fetchall()
    if len(rows) == 0:
        return -1

    curs.execute("SELECT baggage FROM passenger WHERE number = '{}'".format(number))
    rows = curs.fetchall()
    connection.close()
    if len(rows) != 0:
        for row in rows:
            sum += row[0]
        return sum
    else:
        return 0

def get_flight_info_by_surname(surname):
    connection = connector()
    curs = cursor(connection)

    curs.execute("SELECT number FROM passenger WHERE surname = '{}'".format(surname))
    rows = curs.fetchall()
    connection.close()

    result = []
    if len(rows) == 0:
        return -1

    connection = connector()
    curs = cursor(connection)

    for row in rows:
        curs.execute("SELECT * FROM flights WHERE number = '{}' AND date != '0'".format(row[0]))
        rows_data = curs.fetchall()
        if len(rows_data) != 0:
            result.append(rows_data)
    connection.close()

    if len(result) != 0:
        return result
    return -1

def get_short_flight_info_by_direction(direction):
    connection = connector()
    curs = cursor(connection)

    result = []

    curs.execute("SELECT number,date FROM flights WHERE direction = '{}'".format(direction))
    rows = curs.fetchall()
    connection.close()
    if len(rows) == 0:
        return -1

    connection = connector()
    curs = cursor(connection)
    for row in rows:
        result.append(row[0])
        result.append(row[1])
        curs.execute("SELECT surname FROM passenger WHERE number = '{}' ORDER BY surname ASC".format(row[0]))
        passengers = curs.fetchall()
        result.append(passengers)
    connection.close()

    return result


def get_flight_info_by_direction(direction):
    connection = connector()
    curs = cursor(connection)

    curs.execute("SELECT * FROM flights WHERE direction = '{}'".format(direction))

    rows = curs.fetchall()

    connection.close()

    if len(rows) == 0:
        return -1
    else:
        return rows

def get_flight_info_by_date(date):
    connection = connector()
    curs = cursor(connection)

    curs.execute("SELECT * FROM flights WHERE date = '{}'".format(date))

    rows = curs.fetchall()

    connection.close()

    if len(rows) == 0:
        return -1
    else:
        return rows

def get_flight_info_by_number(number):
    connection = connector()
    curs = cursor(connection)

    curs.execute("SELECT * FROM flights WHERE number = '{}' AND date != '0'".format(number))

    rows = curs.fetchall()

    connection.close()

    if len(rows) == 0:
        return -1
    else:
        return rows

def get_all_flight_numbers():
    connection = connector()
    curs = cursor(connection)

    curs.execute("SELECT number FROM flights")
    rows = curs.fetchall()
    connection.close()

    result = []
    for row in rows:
        result.append(row[0])

    return result

def decrement_free_seats(number):
    connection = connector()
    curs = cursor(connection)

    curs.execute("SELECT free_seats FROM flights WHERE number='{}'".format(number))

    rows = curs.fetchall()
    new_free_seats = rows[0][0] - 1
    curs.execute("UPDATE flights SET free_seats={} WHERE number = '{}'".format(new_free_seats,number))

    connection.commit()
    connection.close()