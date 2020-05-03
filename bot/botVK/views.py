from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
import json
import vk
import random
import sqlite3

session = vk.Session(access_token="")
vkAPI = vk.API(session)



# Подтверждение сервера
@csrf_exempt
def bot(request):
    body = json.loads(request.body)
    print(body)
    if body == { "type": "confirmation", "group_id": 194135901 }:
        return HttpResponse('17651b81')
    if body["type"] == "message_new":
        answer_is_ok = 0
        change_func = 0

        userID = body["object"]["message"]["from_id"]
        userInfo = vkAPI.users.get(user_ids = userID, v=5.103)[0]
        message = body["object"]["message"]["text"]

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
            if (message in msg[i]) and change_func != 1 and id_answer[i][0] != 32:
                vkAPI.messages.send(user_id=userID, message = answer[i], random_id = random.randint(1, 999999999999999), v=5.103)
                answer_is_ok = 1
            elif (message in msg[i]) and change_func != 1 and id_answer[i][0] == 32:
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
        if (len(message) >= 7 and (message[0:7] == "Повтори" or message[0:7] == "повтори" or message[0:9] == "Повтори '" or message[0:9] == 'Повтори "' or message[0:14] == "Привет повтори" or message[0:15] == "Привет, повтори")) or message[0:3] == "say" or message[0:4] == "/say":
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
        # elif message == "start" or message == "/start" or message == "Start" or message == "/Start":
            # connect = sqlite3.connect('usersDB.sqlite')
            # cursor = connect.cursor()
            # query = """
            # SELECT msg FROM answer
            # """
            # cursor.execute(query)
            # answer = cursor.fetchall()
            # vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
            # connect.commit()
            # connect.close()
            # answ = random.randint(1, 100)
            # if answ >= 1 and answ <= 50:
            #     answer = "Вы начали работу с ботом"
            # elif answ >= 51 and answ <= 100:
            #     answer = "Начало вашей работы с ботом"
            # vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
            # answer = "Команды: /satrt\
            #     \n/say - повторяет то, что написано после команды\
            #     \nПривет - приветствие\
            #     \nПовтори - то же, что и /say"
            
        # elif message == '' and body["object"]["message"]["attachments"][0]["type"] == "sticker":
        #     answer = 'I am not understand stickers'
        #     vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        # elif message == '😶':
        #     answer = 'У этого смайлика нет рецепта!'
        #     vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        # elif message == '😐':
        #     answer = 'Рецепт смайлика: 😶+➖'
        #     vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        # elif message == '🙂':
        #     answer = 'Рецепт смайлика: 😶+(")"+🔃)'
        #     vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        # elif message == '🙃':
        #     answer = 'Рецепт смайлика: 🙂+🔃'
        #     vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
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
        # elif expression:
        #     pass
        elif answer_is_ok == 0:
            answer = 'Что такое "'+message+'"?'
            admin_answer = '⚠UNKNOWN  "'+message+'"  ⚠'
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
            vkAPI.messages.send(user_id=432949478, message = admin_answer, random_id = random.randint(1, 999999999999999), v=5.103)
    return HttpResponse("ok")