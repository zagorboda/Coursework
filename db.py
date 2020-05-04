import sqlite3

def connector():
    connection = sqlite3.connect("airport.db")
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
        curs.execute("INSERT INTO flights (number, direction, all_seats, free_seats, date, class) VALUES (?, ?, ?, ?, ?, ?);", 
        (data[0], data[1], data[2], data[3], data[4], data[5]))

        connection.commit()
        connection.close()
    else:
        print("Flight with this ID already exist")

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
    if len(rows) != 0:
        print("Number of free seats for {} flight is {}".format(number,rows[0][0]))
    else:
        print("Flight {} doesn't found. Make shure you enter correct number".format(number))

    connection.close()

def all_bagage_cost(number):
    connection = connector()
    curs = cursor(connection)

    sum = 0
    curs.execute("SELECT baggage FROM passenger WHERE number = '{}'".format(number))

    rows = curs.fetchall()
    for row in rows:
        sum += row[0]

    print("Total cost of baggage on {} flight is {}".format(number, sum))

    connection.close()

def get_flight_info_by_surname(surname):
    connection = connector()
    curs = cursor(connection)

    curs.execute("SELECT number FROM passenger WHERE surname = '{}'".format(surname))

    rows = curs.fetchall()
    print("Passenger {} are registered to this flights".format(surname))
    for row in rows:
        curs.execute("SELECT direction,date FROM flights WHERE number = '{}' AND date != '0'".format(row[0]))
        rows_data = curs.fetchall()
        for data in rows_data:
            print("Flight: {} ; from {} to {} ; date: {}".format(row[0], data[0].split('|')[0], data[0].split('|')[1], data[1]))

    connection.close()
        


# подключение к базе данных

# курсор
connection = connector()
curs = cursor(connection)
# команда SQL для создания таблицы в базе данных

# команда SQL для вставки данных в таблицу

# sql_command = "INSERT INTO table1 VALUES ('abc', 34);"

# curs.execute(sql_command)

# curs.execute("SELECT * FROM test WHERE surname = 'link'")

# curs.execute("SELECT * FROM flights")

# curs.execute("UPDATE test SET surname = 'TEST', age = 45 WHERE name = 'TOM'")

# curs.execute("INSERT INTO flights (surname, name, age) VALUES (?, ?, ?);", ("Howking", "Steve", 50))

# curs.execute("INSERT INTO flights (number, direction, all_seats, free_seats, date) VALUES (?, ?, ?, ?, ?);", 
# ("TT1216", "New-York|Tokyo", 340, 230, "25.05.2020"))

# curs.execute("DELETE FROM test WHERE id = 5")

# data = ["1234", "New-York|Tokyo", 340, 230, "25.05.2020", "economy"]

# insert_flight(data)

# insert_flight(["123456", "New-York|MilaParis", 440, 250, "30.05.2020", "business"])

surname = 'test'

get_flight_info_by_surname(surname)

# curs.execute("SELECT number FROM passenger WHERE surname = 'abc'")

# rows = curs.fetchall()

# for row in rows:
#     print(row[0])

# number = 123
# select_free_seats(number, curs)

# for row in rows:
#     print(row)
#     print("Flight from", row[0].split('|')[0] , "to", row[0].split('|')[1])

# Сохранить изменения в файлах. Никогда не пропускай это.

# Если мы пропустим это, ничего не будет сохранено в базе данных.

connection.commit()

# закрыть соединение

connection.close()