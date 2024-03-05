from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
import os


# with open('token.txt', 'r') as file:
#     token = file.read().strip()
#
# with open('allowed_id.txt', 'r') as file:
#     allowed_id = file.readlines()
#
# allowed_id = [int(an_id) for an_id in allowed_id]

allowed_id = [1376696765]
token = '6960720511:AAGPu5eBGU3CTR_0qfpd2ktgH8dLCeY5RzE'

bot = Bot(token)
dp = Dispatcher()
global_vars = {}


@dp.message(lambda x: x.text == '?')
async def status(message: Message):
    await bot.send_message(chat_id=1376696765, text=f'я в игре\nТекущая директория: {os.getcwd()}')


@dp.message(F.content_type == 'photo')
async def save_photo(message: Message):
    try:
        desktop_path = os.path.expanduser("~/Desktop")
        destination = os.path.join(desktop_path, 'img.png') if message.caption is None else message.caption
        image = message.photo[-1]
        image_id = image.file_id
        img = await bot.get_file(image_id)
        img_path = img.file_path
        await bot.download_file(img_path, destination)
        await message.answer('Файл сохранен как: ' + destination)
    except Exception as e:
        await message.answer(f'Произошла ошибка: {e}')


@dp.message(lambda x: x.document)
async def save_doc(message: Message):
    try:
        desktop_path = os.path.expanduser("~/Desktop")
        doc_name = message.document.file_name
        destination = os.path.join(desktop_path, doc_name) if message.caption is None else message.caption
        doc_id = message.document.file_id
        doc = await bot.get_file(doc_id)
        doc_path = doc.file_path
        await bot.download_file(doc_path, destination)
        await message.answer('Файл сохранен как: ' + destination)
    except Exception as e:
        await message.answer(f'Произошла ошибка: {e}')


@dp.message(lambda x: x.text.startswith('print '))
async def exec_code(message: Message):
    if message.from_user.id in allowed_id:
        answer = ''
        variables = message.text[6::].strip().split()
        try:
            for var in variables:
                answer += str(eval(var)) + '\n'
        except Exception as e:
            answer += f'Произошла ошибка: {e}'

        await message.answer(answer)
    else:
        await message.answer('В доступе отказано... 🔒')


@dp.message(lambda x: x.text)
async def exec_code(message: Message):
    if message.from_user.id in allowed_id:
        code = message.text
        try:
            exec(code, global_vars)
            for var_name, var_value in global_vars.items():
                globals()[var_name] = var_value
        except Exception as e:
            await message.answer(f'Произошла ошибка: {e}')
    else:
        await message.answer('В доступе отказано... 🔒')


if __name__ == '__main__':
    dp.run_polling(bot)
