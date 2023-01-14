import os
import random

import requests

TOKEN = '5972375728:AAHGXbdkAqdmIGGbOul6Ds4BrJQMqOISRRY'


def tel_parse_message(message):
    print("message:", message)
    try:
        chat_id = message['message']['chat']['id']
        txt = message['message']['text']
        print("chat_id-->", chat_id)
        print("txt-->", txt)

        return chat_id, txt
    except:
        print("NO text found-->>")


def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    print(url)
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    r = requests.post(url, json=payload)

    return r


def tel_send_image(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    files = os.listdir("market/images")
    random_int = random.randint(o, len(files) - 1)

    payload = {
        'chat_id': chat_id,
        'photo': "https://raw.githubusercontent.com/fbsamples/original-coast-clothing/main/public/styles/male-work.jpg",
        'caption': "This is a sample image"
    }

    r = requests.post(url, json=payload)
    return r
