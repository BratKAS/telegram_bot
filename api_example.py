import random
import time
import requests
from PIL import Image
from io import BytesIO
import subprocess


def get_gif():

    # question = input('\nЗадайте да/нет вопрос, и вы получите на него ответ от знаменитости!\n\t')

    ans = ['yes', 'no', 'maybe']
    random.shuffle(ans)

    url = 'https://yesno.wtf/api?force=' + ans[0]

    gif_url = requests.get(url).json()['image']

    # print(gif_url)
    response = requests.get(gif_url)

    img = Image.open(BytesIO(response.content))
    # img.show()
    gif_path = 'gif_file.gif'
    img.save(gif_path, save_all=True)
    # chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    # safari_path = '/System/Volumes/Preboot/Cryptexes/App/System/Applications/Safari.app/Contents/MacOS/Safari'
    # inna = '/Applications/IINA.app/Contents/MacOS/IINA'
    # subprocess.Popen([chrome_path, gif_path])
    # time.sleep(2)
