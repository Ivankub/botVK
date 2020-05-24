from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
import json
import vk
import random
import sqlite3
import database

session = vk.Session(access_token="796c20604eaa3e72ca38cb6e3644fcd94bf9adab8ff5612316c591755f1d33492e7445c21acb8307f204c")
vkAPI = vk.API(session)



# Подтверждение сервера
@csrf_exempt
def bot(request):
    body = json.loads(request.body)
    print(body)
    if body == { "type": "confirmation", "group_id": 194135901 }:
        return HttpResponse('98359f85')
    if body["type"] == "message_new":
        answer_is_ok = 0
        change_func = 0

        userID = body["object"]["message"]["from_id"]
        userInfo = vkAPI.users.get(user_ids = userID, v=5.103)[0]
        time = body["object"]["message"]["date"]
        message = body["object"]["message"]["text"]
        if "payload" in body["object"]["message"]:
            payload = body["object"]["message"]["payload"]

        connect = sqlite3.connect('usersDB.sqlite')
        cursor = connect.cursor()
        query = """
        SELECT msg FROM answer
        """
        cursor.execute(query)
        msg = cursor.fetchall()

        query = """
        SELECT answ FROM answer
        """
        cursor.execute(query)
        answer = cursor.fetchall()

        query = """
        SELECT id FROM answer
        """
        cursor.execute(query)
        id_answer = cursor.fetchall()
        for i in range (0, len(msg)):
            if (message in msg[i]) and change_func != 1 and id_answer[i][0] != 12:
                vkAPI.messages.send(user_id=userID, message = answer[i], random_id = random.randint(1, 999999999999999), v=5.103)
                answer_is_ok = 1
            elif (message in msg[i]) and change_func != 1 and id_answer[i][0] == 12:
                if message == '' and body["object"]["message"]["attachments"][0]["type"] == "sticker":
                    answer = 'I am not understand stickers'
                    vkAPI.messages.send(user_id=userID, message = answer, attachment = "photo134203947_457242274", random_id = random.randint(1, 999999999999999), v=5.103)
                    answer_is_ok = 1
                else:
                    vkAPI.messages.send(user_id=userID, message = answer[i], random_id = random.randint(1, 999999999999999), v=5.103)
                    answer_is_ok = 1
        
        connect.commit()
        connect.close()


        # if message == "Привет" or message == "Прив" or message == "привет" or message == "hello" or message == "Hello" or message == "Здарова":
        #     answ = random.randint(1, 100)
        #     if answ >= 1 and answ <= 25:
        #         answer = "Здравствуй, "+userInfo["first_name"]
        #     elif answ >= 26 and answ <= 50:
        #         answer = "Привет, "+userInfo["first_name"]
        #     elif answ >= 51 and answ <= 75:
        #         answer = "Hello, "+userInfo["first_name"]
        #     elif answ >= 76 and answ <= 100:
        #         answer = "Hi, "+userInfo["first_name"]
        #     vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        # if message == '/smile':
        #     answer = 'Я могу рассказать рецепты смайликов!\
        #         \nЧтобы посмотреть список смайликов, которые я знаю, напиши /smile list\
        #         \nЧтобы узнать рецепт смайлика, отправь его мне (например, 😐)'
        #     vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        # if message == '/smile list':
        #     answer = 'Все смайлики, которые я знаю:\
        #         \n😐\
        #         \n🙂\
        #         \n🙃\
        #         \n😊\
        #         \n😄\
        #         \n😁\
        #         \n😃\
        #         \n😂\
        #         \n🤣'
        #     vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        if "payload" in body["object"]["message"]:
            if payload == """{"command":"start"}""" and answer_is_ok == 0:
                answer_is_ok = 1
                answer = "Вы начали работу с ботом"
                vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
                answer = "Команды: /satrt\
                    \n/say - повторяет то, что написано после команды\
                    \nПривет - приветствие\
                    \nПовтори - то же, что и /say"
                # vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
                attachments = ""
                keyboard = ""
                vkAPI.messages.send(user_id=userID, message = answer, attachment = attachments, random_id = random.randint(1, 999999999999999), v=5.103)
                # send_answer(userID, answer, attachments, keyboard)
                id_user = userID
                keyBoardStart(id_user)
            if payload == """{"command":"Admin"}""" and answer_is_ok == 0:
                answer_is_ok = 1
                connect = sqlite3.connect('usersDB.sqlite')
                cursor = connect.cursor()
                
                query = """
                DELETE FROM Users WHERE id_vk = {0}
                """.format(str(userID))
                cursor.execute(query)
                connect.commit()

                query = """
                INSERT INTO Users(groupId, id_vk) VALUES
                (
                    {0},
                    '{1}'
                );
                """.format(2, str(userID))
                cursor.execute(query)
                connect.commit()

                answer = "Вы выбрали Admin!"
                vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
                
                connect.close
            
            elif payload == """{"command":"Moder"}""" and answer_is_ok == 0:
                answer_is_ok = 1
                answer = "Вы выбрали Moder!"
                vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
                connect = sqlite3.connect('usersDB.sqlite')
                cursor = connect.cursor()

                query = """
                DELETE FROM Users WHERE id_vk = {0}
                """.format(str(userID))
                cursor.execute(query)
                connect.commit()

                query = """
                INSERT INTO Users(groupId, id_vk) VALUES
                (
                    {0},
                    '{1}'
                );
                """.format(1, str(userID))
                
                cursor.execute(query)
                connect.commit()
                connect.close
            
            elif payload == """{"command":"Usual"}""" and answer_is_ok == 0:
                answer_is_ok = 1
                answer = "Вы выбрали Usual!"
                vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
                connect = sqlite3.connect('usersDB.sqlite')
                cursor = connect.cursor()

                query = """
                DELETE FROM Users WHERE id_vk = {0}
                """.format(str(userID))
                cursor.execute(query)
                connect.commit()
                
                query = """
                INSERT INTO Users(groupId, id_vk) VALUES
                (
                    {0},
                    '{1}'
                );
                """.format(3, str(userID))
                cursor.execute(query)
                connect.commit()
                connect.close
            


        if message == "/changeMe":
            answer_is_ok = 1
            answer = "Вы в меню изменения"
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
            id_user = userID
            keyBoardStart(id_user)

        elif (len(message) >= 7 and (message[0:7] == "Повтори" or message[0:7] == "повтори" or message[0:9] == "Повтори '" or message[0:9] == 'Повтори "' or message[0:14] == "Привет повтори" or message[0:15] == "Привет, повтори")) or message[0:3] == "say" or message[0:4] == "/say":
            leng = len(message)
            answer = message[7:leng]
            if message[0:14] == "Привет повтори":
                answer = message[14:leng]
            elif message[0:15] == "Привет, повтори":
                answer = message[15:leng]
            elif message[0:9] == "Повтори '" or message[0:9] == 'Повтори "':
                answer = message[9:leng]
            elif message[0:3] == "say" or message[0:4] == "/say":
                answer = message[4:leng]
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        elif message == '😊':
            answer = 'Рецепт смайлика: 🙂+^^'
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        elif message == '😄':
            answer = 'Рецепт смайлика: 😊+(👄+⬆️)'
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        elif message == '😁':
            answer = 'Рецепт смайлика: 😄+👄'
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        elif message == '😃':
            answer = 'Рецепт смайлика: 😄+••'
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        elif message == '😂':
            answer = 'Рецепт смайлика: 😄+💧💧'
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        elif message == '🤣':
            answer = 'Рецепт смайлика: 😂+⤴️'
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        elif message == '/show_DB' and userID==432949478:
            connect = sqlite3.connect('usersDB.sqlite')
            cursor = connect.cursor()
            query = """
            SELECT msg FROM answer
            """
            cursor.execute(query)
            msg = cursor.fetchall()

            query = """
            SELECT id FROM answer
            """
            cursor.execute(query)
            id_msg = cursor.fetchall()

            query = """
            SELECT answ FROM answer
            """
            cursor.execute(query)
            answ = cursor.fetchall()
            answer = 'struckture:\n ////////id//////// \n\nmessage \n\nanswer\n'
            for i in range (0, len(msg)):
                answer = '{0}\n////////{3}////////\n\n{1}\n\n {2}\n'.format(answer, msg[i][0], answ[i][0], id_msg[i][0])
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        elif message[0:4] == '/add' and userID==432949478:
            connect = sqlite3.connect('usersDB.sqlite')
            cursor = connect.cursor()
            query = """
            SELECT msg FROM answer
            """
            cursor.execute(query)
            msg = cursor.fetchall()

            query = """
            SELECT answ FROM answer
            """
            cursor.execute(query)
            answer = cursor.fetchall()
            no_ok = 1*(-1)
            for i in range (0, len(msg)):
                if message.split("#")[1] == msg[i][0]:
                    no_ok = i
            if no_ok == -1:
                print(no_ok)
                query = """
                INSERT INTO answer(msg, answ) VALUES
                ('{0}', '{1}')
                """.format(message.split("#")[1],message.split("#")[2])
                cursor.execute(query)
                connect.commit()
                answer = "New command: {0} \nand answer for it: {1}".format(message.split("#")[1], message.split("#")[2])
                vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
            else:
                change_func = 1
                answer = "Command: {0} is already exists! \nWould you like to change answer for it from {1} to {2}? (y/n)+#+{3}\nFUNK NOT AVAILABLE!".format(message.split("#")[1], answer[no_ok][0], message.split("#")[2], message)
                vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
            connect.close()
        # elif message.split("#")[0] == "y":
        #     connect = sqlite3.connect('usersDB.sqlite')
        #     cursor = connect.cursor()
        #     query = """
        #       UPDATE answer SET answ = {0} WHERE msg == {1}
        #     """.format(message.split("#")[3],message.split("#")[2])
        #     cursor.execute(query)
        #     connect.commit()
        #     answer = "OK"
        #     vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        # elif message == "/start clicker":
        #     connect = sqlite3.connect('usersDB.sqlite')
        #     cursor = connect.cursor()
        #     query = """
        #         SELECT vk_id FROM clicker
        #     """
        #     cursor.execute(query)
            
        #     idies = cursor.fetchall()
        #     already_start = 0
        #     for i in range(len(idies)):
        #         if int(userID) == int(idies[i][0]):
        #             already_start = 1
        #     if already_start == 0:
        #         id_user = str(userID)
        #         query = """
        #         INSERT INTO clicker(name, vk_id, money, big_money, click, sec, buy_1, buy_2, buy_5, buy_25, buy_100, buy_500, buy_01, buy_02, buy_05, buy_025, buy_0100, buy_0500, last_time) VALUES
        #         (
        #             "{0}",
        #             "{1}",
        #             {2},
        #             {3},
        #             {4},
        #             {5},
        #             {6},
        #             {7},
        #             {8},
        #             {9},
        #             {10},
        #             {11},
        #             {12},
        #             {13},
        #             {14},
        #             {15},
        #             {16},
        #             {17},
        #             {18}
        #         );
        #         """.format(userInfo["first_name"], id_user, 0, 0, 1, 0, 10, 60, 200, 1200, 5000, 30000, 15, 80, 500, 2300, 8000, 50000, time)
        #         cursor.execute(query)

        #         query = """
        #         SELECT * FROM clicker WHERE vk_id = {0}
        #         """.format(userID)
        #         cursor.execute(query)
        #         information = cursor.fetchall()
        #         money_var = information[0][3]
        #         big_money_var = information[0][4]
        #         money_per_click = information[0][5]
        #         money_per_sec = information[0][6]

        #         answer = "You start your carier!\n money: {0}\n money per click: {1}\n money per second: {2}".format((int(money_var)+int(big_money_var)), money_per_click, money_per_sec)
        #         vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        #     else:
        #         query = """
        #         SELECT * FROM clicker WHERE vk_id = {0}
        #         """.format(userID)
        #         cursor.execute(query)
        #         information = cursor.fetchall()
        #         money_var = information[0][3]
        #         big_money_var = information[0][4]
        #         money_per_click = information[0][5]
        #         money_per_sec = information[0][6]

        #         answer = "You start your carier!\n money: {0}\n money per click: {1}\n money per second: {2}".format((int(money_var)+int(big_money_var)*1000000000), money_per_click, money_per_sec)
        #         vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)

        #     connect.commit()
        #     connect.close()
        # #////////////////////////CLICK///////////////////
        # elif message == "click" or message == "Click":
        #     connect = sqlite3.connect('usersDB.sqlite')
        #     cursor = connect.cursor()
        #     query = """
        #         SELECT vk_id FROM clicker
        #     """
        #     cursor.execute(query)
            
        #     idies = cursor.fetchall()
        #     already_start = 0

        #     for i in range(len(idies)):
        #         if int(userID) == int(idies[i][0]):
        #             already_start = 1

        #     if already_start == 1:
        #         query = """
        #         SELECT * FROM clicker WHERE vk_id = {0}
        #         """.format(userID)
        #         cursor.execute(query)
        #         information = cursor.fetchall()
        #         money_var = information[0][3]
        #         big_money_var = information[0][4]
        #         money_per_click = information[0][5]
        #         money_per_sec = information[0][6]

        #         new_money = int(money_var)+int(money_per_click)
        #         new_money_1 = int(big_money_var)
                
        #         if new_money >= 1000000000:
        #             print(new_money)
        #             print(new_money_1)
        #             new_money_1 = 0
        #             new_money_1 = new_money//1000000000
        #             new_money = new_money%1000000000

        #         query = """
        #             UPDATE clicker SET money = {0} WHERE vk_id = "{1}";
        #         """.format(new_money, str(userID))
        #         cursor.execute(query)

        #         query = """
        #             UPDATE clicker SET big_money = {0} WHERE vk_id = "{1}";
        #         """.format(new_money_1, str(userID))
        #         cursor.execute(query)

        #         query = """
        #             SELECT * FROM clicker WHERE vk_id = {0}
        #         """.format(userID)
        #         cursor.execute(query)
        #         information = cursor.fetchall()
        #         money_var = information[0][3]
        #         big_money_var = information[0][4]
        #         money_per_click = information[0][5]
        #         money_per_sec = information[0][6]

        #         answer = "Money: {0}\n money per click: {1}\n money per sec: {2}".format((int(money_var)+int(big_money_var)*1000000000), money_per_click, money_per_sec)
        #         vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        #     else:
        #         answer = "You have not your carier! Type /start clicker"
        #         vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
            
        #     connect.commit()
        #     connect.close()
        # #////////////////////////BUY///////////////////
        # elif message == "/shop":
        #     connect = sqlite3.connect('usersDB.sqlite')
        #     cursor = connect.cursor()
        #     query = """
        #         SELECT vk_id FROM clicker
        #     """
        #     cursor.execute(query)
            
        #     idies = cursor.fetchall()
        #     already_start = 0

        #     for i in range(len(idies)):
        #         if int(userID) == int(idies[i][0]):
        #             already_start = 1

        #     if already_start == 1:
        #         query = """
        #         SELECT * FROM clicker WHERE vk_id = {0}
        #         """.format(userID)
        #         cursor.execute(query)
        #         information = cursor.fetchall()
        #         money_var = information[0][3]
        #         big_money_var = information[0][4]
        #         money_per_click = information[0][5]
        #         money_per_sec = information[0][6]

        #         buy_1 = information[0][7]
        #         buy_2 = information[0][8]
        #         buy_5 = information[0][9]
        #         buy_25 = information[0][10]
        #         buy_100 = information[0][11]
        #         buy_500 = information[0][12]

        #         buy_01 = information[0][13]
        #         buy_02 = information[0][14]
        #         buy_05 = information[0][15]
        #         buy_025 = information[0][16]
        #         buy_0100 = information[0][17]
        #         buy_0500 = information[0][18]

        #         answer = "Money: {0}\n money per click: {1} \n money per sec: {2}\n\n 1_speed: {3}\n 2_speed: {4}\n 5_speed:{5}\n 25_speed: {6}\n 100_speed: {7}\n 500_speed:{8} \n\n 01_speed: {9}\n 02_speed: {10}\n 05_speed:{11}\n 025_speed: {12}\n 0100_speed: {13}\n 0500_speed:{14}".format((int(money_var)+int(big_money_var)*1000000000), money_per_click, money_per_sec, buy_1, buy_2, buy_5, buy_25, buy_100, buy_500, buy_01, buy_02, buy_05, buy_025, buy_0100, buy_0500)
        #         vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        #     else:
        #         answer = "You have not your carier! Type /start clicker"
        #         vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)

        #     connect.commit()
        #     connect.close()
        # elif message[0:4] == "/buy":
        #     connect = sqlite3.connect('usersDB.sqlite')
        #     cursor = connect.cursor()
        #     query = """
        #         SELECT vk_id FROM clicker
        #     """
        #     cursor.execute(query)
            
        #     idies = cursor.fetchall()
        #     already_start = 0

        #     for i in range(len(idies)):
        #         if int(userID) == int(idies[i][0]):
        #             already_start = 1

        #     if already_start == 1:
        #         query = """
        #             SELECT * FROM clicker WHERE vk_id = {0}
        #         """.format(userID)
        #         cursor.execute(query)
        #         information = cursor.fetchall()
        #         money_var = information[0][3]
        #         big_money_var = information[0][4]
        #         money_per_click = information[0][5]
        #         money_per_sec = information[0][6]

        #         buy_1 = information[0][7]
        #         buy_2 = information[0][8]
        #         buy_5 = information[0][9]
        #         buy_25 = information[0][10]
        #         buy_100 = information[0][11]
        #         buy_500 = information[0][12]

        #         buy_01 = information[0][13]
        #         buy_02 = information[0][14]
        #         buy_05 = information[0][15]
        #         buy_025 = information[0][16]
        #         buy_0100 = information[0][17]
        #         buy_0500 = information[0][18]

        #         cena = 0
        #         new_buy = 0
        #         now_buy = ""
        #         new_money_per_click = int(money_per_click)
        #         new_money_per_sec = int(money_per_sec)


        #         if message.split("_")[1] == "1":
        #             cena = buy_1
        #             new_buy = int(round(1.2*buy_1))
        #             now_buy = "buy_1"
        #             new_money_per_click = new_money_per_click + 1
        #         elif message.split("_")[1] == "2":
        #             cena = buy_2
        #             new_buy = int(round(1.2*buy_2))
        #             now_buy = "buy_2"
        #             new_money_per_click = new_money_per_click + 2
        #         elif message.split("_")[1] == "5":
        #             cena = buy_5
        #             new_buy = int(round(1.2*buy_5))
        #             now_buy = "buy_5"
        #             new_money_per_click = new_money_per_click + 5
        #         elif message.split("_")[1] == "25":
        #             cena = buy_25
        #             new_buy = int(round(1.2*buy_25))
        #             now_buy = "buy_25"
        #             new_money_per_click = new_money_per_click + 25
        #         elif message.split("_")[1] == "100":
        #             cena = buy_100
        #             new_buy = int(round(1.2*buy_100))
        #             now_buy = "buy_100"
        #             new_money_per_click = new_money_per_click + 100
        #         elif message.split("_")[1] == "500":
        #             cena = buy_500
        #             new_buy = int(round(1.2*buy_500))
        #             now_buy = "buy_500"
        #             new_money_per_click = new_money_per_click + 500
                
        #         if message.split("_")[1] == "01":
        #             cena = buy_01
        #             new_buy = int(round(1.2*buy_01))
        #             now_buy = "buy_01"
        #             new_money_per_sec = new_money_per_sec + 1
        #         elif message.split("_")[1] == "02":
        #             cena = buy_02
        #             new_buy = int(round(1.2*buy_02))
        #             now_buy = "buy_02"
        #             new_money_per_sec = new_money_per_sec + 2
        #         elif message.split("_")[1] == "05":
        #             cena = buy_05
        #             new_buy = int(round(round(1.2*buy_05)))
        #             now_buy = "buy_05"
        #             new_money_per_sec = new_money_per_sec + 5
        #         elif message.split("_")[1] == "025":
        #             cena = buy_025
        #             new_buy = int(round(1.2*buy_025))
        #             now_buy = "buy_025"
        #             new_money_per_sec = new_money_per_sec + 25
        #         elif message.split("_")[1] == "0100":
        #             cena = buy_0100
        #             new_buy = int(round(1.2*buy_0100))
        #             now_buy = "buy_0100"
        #             new_money_per_sec = new_money_per_sec + 100
        #         # elif message.split("_")[1] == "0500":
        #         #     cena = buy_0500
        #         #     new_buy = int(round(1.2*buy_0500))
        #         #     now_buy = "buy_0500"
        #         #     new_money_per_sec = new_money_per_sec + 500

        #         if (int(money_var)+int(big_money_var*1000000000)) >= int(cena):
        #             new_money = int(money_var)+int(big_money_var*1000000000)-int(cena)
        #             new_money_1 = int(big_money_var)
        #             if new_money >= 1000000000:
        #                 new_money_1 = 0
        #                 new_money_1 = new_money//1000000000
        #                 new_money = new_money%1000000000
        #             query = """
        #                 UPDATE clicker SET money = {0} WHERE vk_id = "{1}";
        #             """.format(new_money, str(userID))
        #             cursor.execute(query)
        #             query = """
        #                 UPDATE clicker SET big_money = {0} WHERE vk_id = "{1}";
        #             """.format(new_money_1, str(userID))
        #             cursor.execute(query)

        #             if now_buy == "buy_1" or now_buy == "buy_2" or now_buy == "buy_5" or now_buy == "buy_25" or now_buy == "buy_100" or now_buy == "buy_500":
        #                 query = """
        #                     UPDATE clicker SET click = {0} WHERE vk_id = "{1}";
        #                 """.format(new_money_per_click, str(userID))
        #                 cursor.execute(query)
        #             elif now_buy == "buy_01" or now_buy == "buy_02" or now_buy == "buy_05" or now_buy == "buy_025" or now_buy == "buy_0100" or now_buy == "buy_0500":
        #                 query = """
        #                     UPDATE clicker SET sec = {0} WHERE vk_id = "{1}";
        #                 """.format(new_money_per_sec, str(userID))
        #                 cursor.execute(query)

        #             query = """
        #                 UPDATE clicker SET {0} = {1} WHERE vk_id = "{2}";
        #             """.format(now_buy, new_buy, str(userID))
        #             cursor.execute(query)

        #             query = """
        #                 SELECT * FROM clicker WHERE vk_id = {0}
        #             """.format(userID)
        #             cursor.execute(query)
        #             information = cursor.fetchall()
        #             money_var = information[0][3]
        #             big_money_var = information[0][4]
        #             money_per_click = information[0][5]
        #             money_per_sec = information[0][6]

        #             buy_1 = information[0][7]
        #             buy_2 = information[0][8]
        #             buy_5 = information[0][9]
        #             buy_25 = information[0][10]
        #             buy_100 = information[0][11]
        #             buy_500 = information[0][12]

        #             buy_01 = information[0][13]
        #             buy_02 = information[0][14]
        #             buy_05 = information[0][15]
        #             buy_025 = information[0][16]
        #             buy_0100 = information[0][17]
        #             buy_0500 = information[0][18]

        #             answer = "You succesfuly buy speed! \n Money: {0}\n money per click: {1} \n money per sec: {2}\n\n 1_speed: {3}\n 2_speed: {4}\n 5_speed:{5}\n 25_speed: {6}\n 100_speed: {7}\n 500_speed:{8} \n\n 01_speed: {9}\n 02_speed: {10}\n 05_speed:{11}\n 025_speed: {12}\n 0100_speed: {13}\n 0500_speed:{14}".format((int(money_var)+int(big_money_var)*1000000000), money_per_click, money_per_sec, buy_1, buy_2, buy_5, buy_25, buy_100, buy_500, buy_01, buy_02, buy_05, buy_025, buy_0100, buy_0500)
        #             vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        #         else:
        #             query = """
        #                 SELECT * FROM clicker WHERE vk_id = {0}
        #             """.format(userID)
        #             cursor.execute(query)
        #             information = cursor.fetchall()
        #             print()
        #             print(information)
        #             print()
        #             money_var = information[0][3]
        #             big_money_var = information[0][4]
        #             money_per_click = information[0][5]
        #             money_per_sec = information[0][6]

        #             answer = "You have not enough money!\n money: {0}".format(int(money_var)+int(big_money_var*1000000000))
        #             vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        #     else:
        #         answer = "You have not your carier! Type /start clicker"
        #         vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
            
        #     connect.commit()
        #     connect.close()
        # elif message == "time":
        #     answer = "asdsad: {0}".format(time)
        #     vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        elif answer_is_ok == 0:
            # answer = 'Что такое "'+message+'"?\n Если хочешь научить меня этому слову, то напиши сообщение такого типа:\n/teach_НужноеСлово_Категория_Ответ \nКатегории: \n  Приветствия\n  Прощания\n  Оскорбления\n  Животные\n  Фразы'
            answer = 'Что такое "'+message+'"?'
            admin_answer = '⚠UNKNOWN  "'+message+'"  ⚠'
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
            vkAPI.messages.send(user_id=432949478, message = admin_answer, random_id = random.randint(1, 999999999999999), v=5.103)
#//////////////////////////////////////////////////////////TIME IS
        connect = sqlite3.connect('usersDB.sqlite')
        cursor = connect.cursor()
        query = """
            SELECT vk_id FROM clicker
        """
        cursor.execute(query)
            
        idies = cursor.fetchall()
        already_start = 0

        query = """
            SELECT * FROM clicker WHERE vk_id = {0}
        """.format(userID)
        cursor.execute(query)
        information = cursor.fetchall()

        for i in range(len(idies)):
            if int(userID) == int(idies[i][0]):
                already_start = 1
            
        if already_start == 1:
            money_var = information[0][3]
            big_money_var = information[0][4]
            money_per_click = information[0][5]
            money_per_sec = information[0][6]
            last_time = information[0][19]
            past_time = int(time) - int(last_time)

            new_money = int(money_var) + (int(money_per_sec)*int(past_time))
            new_money_1 = int(big_money_var)
            if new_money >= 1000000000:
                new_money_1 = 0
                new_money_1 = new_money//1000000000
                new_money = new_money%1000000000
                    
            query = """
                UPDATE clicker SET money = {0} WHERE vk_id = "{1}";
            """.format(new_money, str(userID))
            cursor.execute(query)

            query = """
                UPDATE clicker SET big_money = {0} WHERE vk_id = "{1}";
            """.format(new_money_1, str(userID))
            cursor.execute(query)

            query = """
                UPDATE clicker SET last_time = {0} WHERE vk_id = "{1}";
            """.format(int(time), str(userID))
            cursor.execute(query)
            # answer = "{0}".format(information)
            # vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
            connect.commit()
            connect.close()
        
    # def keyBoardStart(request, userID):
    #     answ = "Привет! Выбери группу!"
    #     keyboard = json.dumps({
    #         "one_time": True,
    #         "buttons":[[
    #             {
    #                 "action":{
    #                     "type":"text",
    #                     "label":"Admin",
    #                     "payload":"""{"command":"Admin"}"""
    #                 },
    #                 "color":"negative"
    #             },
    #         ]]
    #     })
    #     send_answer(userID, answ, "", "")
    return HttpResponse("ok")

def keyBoardStart(userID):
    answ = "Привет! Выбери группу!"
    keyboard = json.dumps({
        "one_time": True,
        "buttons":[[
            {
                "action":{
                    "type":"text",
                    "label":"Admin",
                    "payload":"""{"command":"Admin"}"""
                },
                "color":"negative"
            },
            {
                "action":{
                    "type":"text",
                    "label":"Moder",
                    "payload":"""{"command":"Moder"}"""
                },
                "color":"positive"
            },
            {
                "action":{
                    "type":"text",
                    "label":"Usual",
                    "payload":"""{"command":"Usual"}"""
                },
                "color":"primary"
            },
        ]]
    })
    send_answer(userID, answ, "", keyboard)
def keyBoardChange(userID):
    answ = "Выбери группу!"
    keyboard = json.dumps({
        "one_time": True,
        "buttons":[[
            {
                "action":{
                    "type":"text",
                    "label":"Admin",
                    "payload":"""{"command":"AdminC"}"""
                },
                "color":"negative"
            },
            {
                "action":{
                    "type":"text",
                    "label":"Moder",
                    "payload":"""{"command":"ModerC"}"""
                },
                "color":"positive"
            },
            {
                "action":{
                    "type":"text",
                    "label":"Usual",
                    "payload":"""{"command":"UsualC"}"""
                },
                "color":"primary"
            },
        ]]
    })
    send_answer(userID, answ, "", keyboard)
def send_answer(id_user, answer, attachments, keyboard):
    vkAPI.messages.send(user_id=id_user, message = answer, attachment = attachments, keyboard = keyboard, random_id = random.randint(1, 999999999999999), v=5.103)

lg = {
    "success": False,
    "Groups": database.get("Groups"),
    "Users": database.get("Users")
}

def login(request):
    global lg
    print(request.GET)

    if ("login" and "password") in request.GET:
        if "admin" in request.GET["login"] and "0000" in request.GET["password"]:
            lg["success"] = True

    if ("type" and "text") in request.GET:
        lg = {
            "success": False,
            "Groups": database.get("Groups"),
            "Users": database.get("Users")
        }
        for i in range (0, len(lg["Users"])):
            print(lg["Users"][i]["groupId"])
            if "Admin" == request.GET["type"]:
                if lg["Users"][i]["groupId"] == 2:
                    print("Admin")
                    vkAPI.messages.send(user_id=lg["Users"][i]["id_vk"], message = request.GET["text"], random_id = random.randint(1, 999999999999999), v=5.103)
            elif "Moder" == request.GET["type"]:
                if lg["Users"][i]["groupId"] == 1:
                    print("Moder")
                    vkAPI.messages.send(user_id=lg["Users"][i]["id_vk"], message = request.GET["text"], random_id = random.randint(1, 999999999999999), v=5.103)
            elif "Usual" == request.GET["type"]:
                if lg["Users"][i]["groupId"] == 3:
                    print("Usual")
                    vkAPI.messages.send(user_id=lg["Users"][i]["id_vk"], message = request.GET["text"], random_id = random.randint(1, 999999999999999), v=5.103)
        
    if ("id_u" and "text_u") in request.GET:
        for i in range(0, len(lg["Users"])):
            if int(lg["Users"][i]["id_vk"]) == int(request.GET["id_u"]):
                vkAPI.messages.send(user_id=lg["Users"][i]["id_vk"], message = request.GET["text_u"], random_id = random.randint(1, 999999999999999), v=5.103)

    return render(request, "login.html", lg)