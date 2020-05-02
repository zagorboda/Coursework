import sqlite3

def connector():
    connection = sqlite3.connect("airport.db")
    return connection

def cursor(connection):
    crsr = connection.cursor()
    return crsr

def insert_flight(data, curs):
    curs.execute("INSERT INTO flights (number, direction, all_seats, free_seats, date, class) VALUES (?, ?, ?, ?, ?, ?);", 
    (data[0], data[1], data[2], data[3], data[4], data[5]))

def insert_passenger(data, curs):
    curs.execute("INSERT INTO passenger (surname, number, class, baggage, cost) VALUES (?, ?, ?, ?, ?);", 
    (data[0], data[1], data[2], data[3], data[4]))

def select_free_seats(number, curs):
    curs.execute("SELECT free_seats FROM flights where number = {}".format(number))
    rows = crsr.fetchall()
    if len(rows) != 0:
        print("Number of free seats for {} flight is {}".format(number,rows[0][0]))
    else:
        print("Flight {} doesn't found. Make shure you enter correct number".format(number))

# подключение к базе данных

# курсор
connection = connector()
crsr = cursor(connection)
# команда SQL для создания таблицы в базе данных

# команда SQL для вставки данных в таблицу

# sql_command = "INSERT INTO table1 VALUES ('abc', 34);"

# crsr.execute(sql_command)

# crsr.execute("SELECT * FROM test WHERE surname = 'link'")

# crsr.execute("SELECT * FROM flights")

# crsr.execute("UPDATE test SET surname = 'TEST', age = 45 WHERE name = 'TOM'")

# crsr.execute("INSERT INTO flights (surname, name, age) VALUES (?, ?, ?);", ("Howking", "Steve", 50))

# crsr.execute("INSERT INTO flights (number, direction, all_seats, free_seats, date) VALUES (?, ?, ?, ?, ?);", 
# ("TT1216", "New-York|Tokyo", 340, 230, "25.05.2020"))

# crsr.execute("DELETE FROM test WHERE id = 5")

# data = ["1234", "New-York|Tokyo", 340, 230, "25.05.2020", "economy"]

# insert_flight(data)

number = 112
select_free_seats(number, crsr)

# for row in rows:
#     print(row)
#     print("Flight from", row[0].split('|')[0] , "to", row[0].split('|')[1])

# Сохранить изменения в файлах. Никогда не пропускай это.

# Если мы пропустим это, ничего не будет сохранено в базе данных.

connection.commit()

# закрыть соединение

connection.close()