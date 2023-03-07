from pyrogram import Client, filters
from os import environ
from dotenv import load_dotenv
from os.path import join, dirname
import datetime
from pykeyboard import ReplyKeyboard, ReplyButton
from config import sockdata



load_dotenv(join(dirname(__file__), '.env'))
botTG = Client('weather_bot', api_id=environ.get('API_ID'), api_hash=environ.get('API_HASH'), bot_token=environ.get('TOKENTG'))



start_msg = """ Вот что я умею: """
params = {
    'test2': -1001651474042,
    'test': -1001789873317
}

locale = ReplyKeyboard(row_width=3)
locale.add(ReplyButton('Русский'), ReplyButton('English'))

main_menu = ReplyKeyboard(resize_keyboard=True, row_width=3)
main_menu.add(ReplyButton('Прогноз на сегодня'), ReplyButton('Прогноз на 3 дня'),
            ReplyButton('Прогноз на завтра, затмения'), ReplyButton('Настройки групп и каналов'),
            ReplyButton('Настройки'))

back_button = ReplyKeyboard(row_width=3)
back_button.add(ReplyButton('Назад'))



class Database_conn:
    self.connection = pymysql.connect(**sockdata)
    self.cursor = self.connection.cursor()
    




@botTG.on_message(filters.regex("start"))
async def send_keyboard(client, message):
    with botTG:
        await message.reply(text="Выберите язык", reply_markup=locale)



@botTG.on_message(filters.regex("Русский"))
async def ru_lang(client, message):
    with botTG:
        ru_text = message.text
        await message.reply("Для какого города написать прогноз?")



@botTG.on_message(filters.regex("English"))
async def eng_lang(client, message):
    with botTG:
        eng_text = message.text
        await message.reply("For which city to write the forecast?")




@botTG.on_message(filters.regex("Назад"))
async def eng_lang(client, message):
    with botTG:
        await message.reply(text="For which city to write the forecast?", reply_markup=back_button)




@botTG.on_message()
async def choose_city(client, message):

    chosen_city = message.text
    with botTG:
        await message.reply(text='Вот что я умею:', reply_markup=main_menu)




botTG.run()