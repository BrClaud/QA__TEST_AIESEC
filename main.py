from aiogram import Bot, Dispatcher, types, filters
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
import asyncio
import logging
from keyboards import kb_questions

logging.basicConfig(level=logging.INFO)

bot = Bot("bot_token")
dp = Dispatcher()

number_of_questions = 0


@dp.message(filters.CommandStart())  # так же работает на команду /start
async def cmd_start(message: types.Message):
    with open("questions.txt", 'r', encoding='utf-8') as file:  # читает вопросы
        a = file.read().split('\n')
    strs = ''
    for i in range(len(a)):
        strs += f'{i + 1}) {a[i]}\n'

    await message.answer(
        text=f'приветствую\nздесь ты можешь узнать про интересующие тебя вопросы\n{strs}',
        reply_markup=kb_questions.get_kb_questions()
    )


@dp.callback_query(filters.Text(startswith="callback_"))  # принимает колбеки по нужному вопросу
async def answers(callback: types.CallbackQuery):
    with open('answers.txt', 'r', encoding='utf-8') as file: # читает ответы к вопросам
        strs = file.read().split('\n')
    await callback.message.answer(f'ответ на вопрос {int(callback.data[-1])}: \n{strs[int(callback.data[-1])-1]}') #
    # берем последную цифру колбека и по ней определяем на какой вопрос мы отвечаем
    await callback.answer()

# todo было бы неплохо перенести все на взаимодействие с базой данных или на работу с api google table, но так как
#  это тестовое задание это не уместно

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    with open("questions.txt", 'r', encoding='utf-8') as file:
        a = file.read().split('\n')
        number_of_questions = len(a)
    asyncio.run(main())
