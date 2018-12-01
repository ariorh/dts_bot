import requests
import misc
import json

token = misc.token

URL = 'https://api.telegram.org/bot' + token + '/'

# https://api.telegram.org/bot603534449:AAF2sJwpHOGZ4K09TkH4UB29CDq9XhQE7PY/sendmessage?chat_id=166525525&text=test

def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()

def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']
    #print(message_text)
    message = {'chat_id': chat_id,
               'text': message_text}
    return message

def send_message(chat_id, text='wait...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    #print(url)
    requests.get(url)


def main():
    #d = get_updates()

    #with open('updates.json', 'w') as file:
    #    json.dump(d, file, indent=2, ensure_ascii=False)
    answer = get_message()
    chat_id = answer['chat_id']
    text = answer['text']
    send_message(chat_id, 'text')


if __name__ == '__main__':
    main()
