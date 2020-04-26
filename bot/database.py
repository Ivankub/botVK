import sqlite3

#connect to DataBase
connect = sqlite3.connect('usersDB.sqlite')
#create cursor for connection
cursor = connect.cursor()

# query = """
# CREATE TABLE cars_two(
#     id INT PRIMARY KEY,
#     mark TEXT,
#     color TEXT,
#     number INT
# );
# """
# cursor.execute(query)

# query = """
# INSERT INTO cars_two(id, mark, color, number) VALUES
# (0, 'marka1', 'red', 121213),
# (1, 'marka2', 'green', 133452),
# (2, 'marka2', 'gray', 123432),
# (3, 'marka3', 'blue', 124543),
# (4, 'marka1', 'black', 324543);
# """
# cursor.execute(query)

# query = """
# SELECT * FROM cars_two
# """
# cursor.execute(query)

result = cursor.fetchall()
print(result)
#save
connect.commit()

connect.close()