import requests
import time
import random
from api_example import get_gif
import os


API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
API_DOGS_URL = 'https://random.dog/woof.json'
BOT_TOKEN = '6960720511:AAGPu5eBGU3CTR_0qfpd2ktgH8dLCeY5RzE'

# Укажите путь к файлу, который вы хотите отправить
file_path = r'gif_file.gif'

url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendDocument'

text_list = []

h_file_path = "history.txt"

if not os.path.exists(h_file_path):
    with open(h_file_path, "w", encoding='utf-8') as file:
        file.write("")

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        text_list.append(line.strip())

random.shuffle(text_list)
n = len(text_list)

offset = -2
counter = 0
chat_id: int
index = 0
my_id = '1376696765'

cat_response: requests.Response
cat_link: str
ERROR_TEXT = 'Здесь должна была быть картинка с котиком или собачкой:('

# requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id=515209018&text=Я соскучился! Ты тут?\n'
#              f'Теперь я умею отвечать на вопросы!')

while True:
    TEXT = text_list[index % n] + ('\n\nС тобой так интересно! \nНапиши еще что-нибудь...\n\n'
                                   'Я умею отвечать на вопросы, только не забудь поставить "?"\n\n'
                                   'А еще я умею отправлять фото КОТИКОВ и СОБАЧЕК, просто попроси!')
    # print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            # print(result)
            offset = result['update_id']
            chat_id = result['message']['from']['id']

            try:
                message = result['message']['text'].lower()
                user_name = result['message']['from']['first_name']
                text_input = f'\n{counter + 1}. От {user_name} с id {chat_id} пришло сообщение: {message}'
                print(text_input)
                if str(chat_id) != my_id:
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={my_id}&text={text_input}')
            except KeyError:
                continue
            with open(h_file_path, 'a', encoding='utf-8') as file:
                file.write(text_input)
            if 'кот' in message or 'кош' in message:
                cat_response = requests.get(API_CATS_URL)
                if cat_response.status_code == 200:
                    answer = cat_link = cat_response.json()[0]['url']
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
                else:
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
                    answer = ERROR_TEXT
            elif any(['соба' in message, 'пес' in message, 'пёс' in message]):
                dog_response = requests.get(API_DOGS_URL)
                if dog_response.status_code == 200:
                    answer = dog_link = dog_response.json()['url']
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={dog_link}')
                else:
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
                    answer = ERROR_TEXT
            elif '?' in message:
                get_gif()
                answer = ERROR_TEXT = files = {'document': open(file_path, 'rb')}
                data = {'chat_id': chat_id}
                requests.post(url, files=files, data=data)
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
                answer = TEXT
                index += 1
            text_output = f'\n{counter+1}. Отправлен ответ:\n{answer}'
            print(text_output)
            if str(chat_id) != my_id:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={my_id}&text={text_output}')
            with open(h_file_path, 'a', encoding='utf-8') as file:
                file.write(text_output)
            counter += 1

    time.sleep(1)

