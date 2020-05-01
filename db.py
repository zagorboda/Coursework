import sqlite3

# подключение к базе данных

connection = sqlite3.connect("testlite.db")

# курсор

crsr = connection.cursor()

# команда SQL для создания таблицы в базе данных

# команда SQL для вставки данных в таблицу

# sql_command = "INSERT INTO table1 VALUES ('abc', 34);"

# crsr.execute(sql_command)

crsr.execute("SELECT name FROM table1")

rows = crsr.fetchall()

for row in rows:
    print(row[0])

# Сохранить изменения в файлах. Никогда не пропускай это.

# Если мы пропустим это, ничего не будет сохранено в базе данных.

connection.commit()

# закрыть соединение

connection.close()