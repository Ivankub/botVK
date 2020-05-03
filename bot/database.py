import sqlite3

#connect to DataBase
connect = sqlite3.connect('usersDB.sqlite')
#create cursor for connection
cursor = connect.cursor()

# query = """
# CREATE TABLE clicker(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     vk_id TEXT,
#     money INT,
#     click INT,
#     buy_1 INT,
#     buy_2 INT,
#     buy_5 INT
# );
# """
# cursor.execute(query)
# connect.commit()

# query = """
# CREATE TABLE owners(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     owner TEXT,
#     driver_card INT
# );
# """
# cursor.execute(query)
# connect.commit()

# query = """
# CREATE TABLE cars(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     mark TEXT,
#     model TEXT,
#     produced TEXT
# );
# """
# cursor.execute(query)
# connect.commit()


# query = """
# CREATE TABLE info(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     number INT,
#     color TEXT,
#     id_owner INT,
#     id_model INT
# );
# """
# cursor.execute(query)
# connect.commit()


# query = """
# INSERT INTO answer(msg, answ) VALUES
# ('/smile', 'Я могу рассказать рецепты смайликов!\
# \nЧтобы посмотреть список смайликов, которые я знаю, напиши /smile list\
# \nЧтобы узнать рецепт смайлика, отправь его мне (например, 😐)'),
# ('Привет', 'Здравствуй'),
# ('Здарова', 'Здравствуй'),
# ('Здравствуй', 'Здравствуй'),
# ('Hi', 'Здравствуй'),
# ('Прив', 'Здравствуй'),
# ('Hello', 'Здравствуй'),
# ('привет', 'Здравствуй'),
# ('/start', 'Команды: /satrt\
# \n/say - повторяет то, что написано после команды\
# \nПривет - приветствие\
# \nПовтори - то же, что и /say'),
# ('start', 'Команды: /satrt\
# \n/say - повторяет то, что написано после команды\
# \nПривет - приветствие\
# \nПовтори - то же, что и /say'),
# ('Start', 'Команды: /satrt\
# \n/say - повторяет то, что написано после команды\
# \nПривет - приветствие\
# \nПовтори - то же, что и /say');
# """
# cursor.execute(query)

# query = """
# DELETE FROM answer WHERE msg = "🙂"
# """
# cursor.execute(query)

# query = """
# SELECT * FROM answer
# """
# cursor.execute(query)
# result = cursor.fetchall()
# print(result)


# query = """
# DROP TABLE owners
# """
# cursor.execute(query)
# query = """
# DROP TABLE cars
# """
# cursor.execute(query)
# query = """
# DROP TABLE info
# """
# cursor.execute(query)

def add(owner, driver_card, mark, model, produced, number, color):
    query = """
    INSERT INTO owners(owner, driver_card) VALUES
    (
        {0},
        {1}
    );
    """.format(owner, driver_card)
    cursor.execute(query)
    connect.commit()

    query = """
    INSERT INTO cars(mark, model, produced) VALUES
    (
        {0},
        {1},
        {2}
    );
    """.format(mark, model, produced)
    cursor.execute(query)
    connect.commit()

    query = """
    SELECT id FROM owners
    """
    cursor.execute(query)
    id_own = cursor.fetchall()
    lenth_id = len(id_own)
    id_own = lenth_id

    query = """
    INSERT INTO info(number, color, id_owner, id_model) VALUES
    (
        {0},
        {1},
        {2},
        {3}
    );
    """.format(number, color, id_own, id_own)
    cursor.execute(query)
    connect.commit()

def mark_select(mark):
    query = """
    SELECT * FROM cars WHERE mark = {0}
    """.format(mark)
    cursor.execute(query)
    result = cursor.fetchall()

    query = """
    SELECT * FROM info
    """
    cursor.execute(query)
    result1 = cursor.fetchall()

    for i in range(len(result)):
        answer_print = 'id: {0}; mark: {1}; model: {2}; produced country: {3}; color: {4}'.format(result[i][0], result[i][1], result[i][2], result[i][3], result1[result[i][0] - 1][2])
        print(answer_print)

def mark_color_select(mark, color):
    query = """
    SELECT * FROM cars WHERE mark = {0}
    """.format(mark)
    cursor.execute(query)
    result = cursor.fetchall()

    query = """
    SELECT * FROM info WHERE color = {0}
    """.format(color)
    cursor.execute(query)
    result1 = cursor.fetchall()

    for i in range(len(result1)):
        for j in range(len(result)):
            if result[j][0] == result1[i][0]:
                answer_print = 'id: {0}; mark: {1}; model: {2}; produced country: {3}; color: {4}'.format(result[i][0], result[i][1], result[i][2], result[i][3], result1[i][2])
                print(answer_print)

        

mark_select("'Toyota'")

mark_color_select("'Toyota'", "'black'")

# add("'Ivan'", 101, "'Toyota'", "'Bat123'", "'Japan'", 2134, "'red'")
# add("'Karl'", 102, "'Lada'", "'KALINA'", "'Russia'", 3628, "'red'")
# add("'Ben'", 103, "'Mitsubishi'", "'Outlender'", "'Chinese'", 2302, "'red'")
# add("'Greg'", 104, "'Mitsubishi'", "'Good'", "'Chinese'", 4850, "'green'")
# add("'Jimmy'", 105, "'Porsche'", "'Taycan'", "'Germany'", 6543, "'gray'")
# add("'Alex'", 106, "'Toyota'", "'Yota'", "'Japan'", 4324, "'blue'")
# add("'Vasya'", 107, "'Lada'", "'MALINA'", "'Russia'", 3345, "'blue'")
# add("'Petya'", 110, "'Zhiguli'", "'MOS'", "'USSR'", 4544, "'red'")
# add("'Alesha'", 111, "'Toyota'", "'Toto'", "'Japan'", 9898, "'black'")

# query = """
# SELECT * FROM owners
# """
# cursor.execute(query)
# result = cursor.fetchall()
# print(result)

# query = """
# SELECT * FROM cars
# """
# cursor.execute(query)
# result = cursor.fetchall()
# print(result)

# query = """
# SELECT * FROM info
# """
# cursor.execute(query)
# result = cursor.fetchall()
# print(result)

#save
connect.commit()

connect.close()