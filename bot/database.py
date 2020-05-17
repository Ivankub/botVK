import sqlite3

#connect to DataBase
connect = sqlite3.connect('usersDB.sqlite')
#create cursor for connection
cursor = connect.cursor()

# query = """
# CREATE TABLE clicker_1(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     vk_id TEXT,
#     last_time INT,
#     sec INT,
#     buy_01 INT,
#     buy_02 INT,
#     buy_05 INT
# );
# """
# cursor.execute(query)
# connect.commit()

# query = """
# CREATE TABLE hellownwess(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     txt TEXT
# );
# """
# cursor.execute(query)
# connect.commit()

# query = """
# CREATE TABLE hellownwess_answ(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     answ_txt TEXT
# );
# """
# cursor.execute(query)
# connect.commit()


# query = """
# CREATE TABLE byenwess(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     txt TEXT
# );
# """
# cursor.execute(query)
# connect.commit()

# query = """
# CREATE TABLE byenwess_answ(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     answ_txt TEXT
# );
# """
# cursor.execute(query)
# connect.commit()


# query = """
# CREATE TABLE animals(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     txt TEXT
# );
# """
# cursor.execute(query)
# connect.commit()

# query = """
# CREATE TABLE animals_answ(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     answ_txt TEXT
# );
# """
# cursor.execute(query)
# connect.commit()


# query = """
# CREATE TABLE phrases(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     txt TEXT
# );
# """
# cursor.execute(query)
# connect.commit()

# query = """
# CREATE TABLE phrases_answ(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     answ_txt TEXT
# );
# """
# cursor.execute(query)
# connect.commit()

# query = """
# CREATE TABLE bad_phrases(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     txt TEXT
# );
# """
# cursor.execute(query)
# connect.commit()

# query = """
# CREATE TABLE bad_phrases_answ(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     answ_txt TEXT
# );
# """
# cursor.execute(query)
# connect.commit()

# ////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////
# query = """
# DROP TABLE Groups
# """
# cursor.execute(query)
# query = """
# DROP TABLE Users
# """
# cursor.execute(query)

# query = """
# CREATE TABLE Groups(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     groupName TEXT
# );
# """
# cursor.execute(query)
# connect.commit()

# query = """
# CREATE TABLE Users(
#     id INTEGER PRIMARY KEY,
#     groupId INTEGER,
#     id_vk TEXT,
#     FOREIGN KEY (groupId) REFERENCES Groups(id)
# );
# """
# cursor.execute(query)
# connect.commit()

# ////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////

# query = """
# DROP TABLE clicker
# """
# cursor.execute(query)

# query = """
# CREATE TABLE clicker(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     vk_id TEXT,
#     money INT,
#     big_money INT,
#     click INT,
#     sec INT,
#     buy_1 BIGINT,
#     buy_2 BIGINT,
#     buy_5 BIGINT,
#     buy_25 BIGINT,
#     buy_100 BIGINT,
#     buy_500 BIGINT,
#     buy_01 BIGINT,
#     buy_02 BIGINT,
#     buy_05 BIGINT,
#     buy_025 BIGINT,
#     buy_0100 BIGINT,
#     buy_0500 BIGINT,
#     last_time INT
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
# CREATE TABLE answer(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     msg TEXT,
#     answ TEXT
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

def get(table_name, cols = "*"):
    db = sqlite3.connect('db.sqlite')
    cur = db.cursor()

    query = """
        SELECT {1} FROM {0}
        """.format(table_name,  cols if cols=="*" else "({0})".format(",".join(cols)))

    cur.execute(query)
    colNames = list(map(lambda x: x[0], cur.description))

    result = []

    for i in cur.fetchall():
        result.append(dict(zip(colNames, i)))
    db.close()

    return result
        

# mark_select("'Toyota'")

# mark_color_select("'Toyota'", "'black'")

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

query = """
SELECT * FROM Users
"""
cursor.execute(query)
result = cursor.fetchall()
print(result)

# query = """
# UPDATE clicker SET money = {0} WHERE vk_id = "{1}";
# """.format(999999999, "509539783")
# cursor.execute(query)

# query = """
# UPDATE clicker SET big_money = {0} WHERE vk_id = "{1}";
# """.format(0, "432949478")
# cursor.execute(query)
#save
connect.commit()

connect.close()