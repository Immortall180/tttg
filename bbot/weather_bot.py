import os
import logging

import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from messages import get_message
from temp import get_advice
from weather import WeatherServiceException, WeatherInfo, get_weather_for_city, get_weather_for_location



WEATHER_RETRIEVAL_FAILED_MESSAGE = get_message('weather_for_location_retrieval_failed')


logging.basicConfig(level=logging.INFO)


bot = Bot(token="6425968679:AAHgGMtes4PTi3gRkEMVOHvMuutka0yVGlQ")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(get_message('start'), reply=False)

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply(get_message('help'), reply=False)


@dp.message_handler(content_types=['text'])
async def get_weather_in_city(message: types.Message):

    try:
        weather: WeatherInfo = await get_weather_for_city(message.text)
    except WeatherServiceException:
        await message.reply(WEATHER_RETRIEVAL_FAILED_MESSAGE)
        return

    response = get_message('weather_in_city_message') \
        .format(message.text, weather.status, weather.temperature)+ '\n\n' + \
        get_advice(weather)

    await message.reply(response)


@dp.message_handler()
async def default_response(message: types.Message):
    await message.reply(get_message('general_failure'))





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
