import logging
import wikipedia
import requests
from aiogram import Bot, Dispatcher, types, executor


# TOKENni yozing
API_TOKEN = ""

wikipedia.set_lang("uz")
# AIogram bot obyekti yaratish va Dispatcher(uqituvchi) yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Yangi foydalanuvchi kiritilganingizda Salom berish
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! Wikipedia botiga xush kelibsiz!")


# Wikipedia dan ma'lumot olish
@dp.message_handler()
async def sendWiki(message: types.Message):
        try:
        	respond = wikipedia.summary(message.text)
        	await message.answer(respond)
        except:
        	await message.answer("bu mavzuga oid maqola topilmadi boshqa narsa kiritib koʻring")
        

if __name__ == '__main__':
    # loglarni ko'rsatish
    logging.basicConfig(level=logging.INFO)
    # Botni ishga tushurish
    print('Bot ishga tushirildi!')
    executor.start_polling(dp, skip_updates=True)
