import requests

num = input('О каком числе рассказать вам факт?\n\t')

url = 'http://numbersapi.com/' + num

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print('Неверный запрос!')
