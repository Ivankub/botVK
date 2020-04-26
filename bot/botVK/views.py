from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
import json
import vk
import random

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
        userID = body["object"]["message"]["from_id"]
        userInfo = vkAPI.users.get(user_ids = userID, v=5.103)[0]
        message = body["object"]["message"]["text"]
        if message == "Привет" or message == "Прив" or message == "привет" or message == "hello" or message == "Hello" or message == "Здарова":
            answ = random.randint(1, 100)
            if answ >= 1 and answ <= 25:
                answer = "Здравствуй, "+userInfo["first_name"]
            elif answ >= 26 and answ <= 50:
                answer = "Привет, "+userInfo["first_name"]
            elif answ >= 51 and answ <= 75:
                answer = "Hello, "+userInfo["first_name"]
            elif answ >= 76 and answ <= 100:
                answer = "Hi, "+userInfo["first_name"]
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        elif message == '/smile':
            answer = 'Я могу рассказать рецепты смайликов!\
                \nЧтобы посмотреть список смайликов, которые я знаю, напиши /smile list\
                \nЧтобы узнать рецепт смайлика, отправь его мне (например, 😐)'
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        elif message == '/smile list':
            answer = 'Все смайлики, которые я знаю:\
                \n😐\
                \n🙂\
                \n🙃\
                \n😊\
                \n😄\
                \n😁\
                \n😃\
                \n😂\
                \n🤣'
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
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
        elif message == "start" or message == "/start" or message == "Start" or message == "/Start":
            answ = random.randint(1, 100)
            if answ >= 1 and answ <= 50:
                answer = "Вы начали работу с ботом"
            elif answ >= 51 and answ <= 100:
                answer = "Начало вашей работы с ботом"
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
            answer = "Команды: /satrt\
                \n/say - повторяет то, что написано после команды\
                \nПривет - приветствие\
                \nПовтори - то же, что и /say"
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        elif message == '':
            answer = 'I am not understand'
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        elif message == '😶':
            answer = 'У этого смайлика нет рецепта!'
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        elif message == '😐':
            answer = 'Рецепт смайлика: 😶+➖'
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        elif message == '🙂':
            answer = 'Рецепт смайлика: 😶+(")"+🔃)'
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
        elif message == '🙃':
            answer = 'Рецепт смайлика: 🙂+🔃'
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
        else:
            answer = 'Что такое "'+message+'"?'
            admin_answer = '⚠UNKNOWN  "'+message+'"  ⚠'
            vkAPI.messages.send(user_id=userID, message = answer, random_id = random.randint(1, 999999999999999), v=5.103)
            vkAPI.messages.send(user_id=432949478, message = admin_answer, random_id = random.randint(1, 999999999999999), v=5.103)
    return HttpResponse("ok")