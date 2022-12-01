import telebot
from telebot import types

bot = telebot.TeleBot("5481244048:AAExLObyLVAMFoYg-tew8OcJ5Ggz_IpEaNA")


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Жанр аниме(o^ ^o)")
    item2 = types.KeyboardButton("Количество серий(づ◡﹏◡)づ")
    item3 = types.KeyboardButton("Онгоинг/неважно(^.~)")

    markup.add(item1, item2, item3, )

    mess = f'Привет, {message.from_user.first_name} , я помогу выбрать аниме которое тебе точно понравится ∩^ω^∩'
    bot.send_message(message.chat.id, mess.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=["text"])  # создаем обработчик событий
def bot_message(message):
    if message.chat.type == "private":
        if message.text == "Жанр аниме(o^ ^o)":  # делаем подменю
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Боевик")
            item2 = types.KeyboardButton("Драма")
            item3 = types.KeyboardButton("Детектив")
            item4 = types.KeyboardButton("Ужасы")
            item5 = types.KeyboardButton("Комедия")
            item6 = types.KeyboardButton("Повседневность")
            item7 = types.KeyboardButton("Романтика")
            item8 = types.KeyboardButton("Спокон")
            item9 = types.KeyboardButton("Приключения")
            item10 = types.KeyboardButton("Фэнтези")
            item11 = types.KeyboardButton("Психология")
            item12 = types.KeyboardButton("Этти")
            item13 = types.KeyboardButton("Экшен")
            back = types.KeyboardButton("Меню")

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, back)
            bot.send_message(message.chat.id, "Жанр аниме(o^ ^o)", reply_markup=markup)
        elif message.text == "Количество серийづ◡﹏◡)づ":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("12")
            item2 = types.KeyboardButton("24")
            item3 = types.KeyboardButton("24+")
            item4 = types.KeyboardButton("Полнометражное")
            item5 = types.KeyboardButton("Онгоинг/неважно(^.~)")
            item6 = types.KeyboardButton("Жанр аниме(o^ ^o)")
            back = types.KeyboardButton("Меню")
            markup.add(item1, item2, item3, item4, item5, item6, back)
            bot.send_message(message.chat.id, "Количество серийづ◡﹏◡)づ", reply_markup=markup)
        elif message.text == "Онгоинг/неважно(^.~)":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Онгоинг")
            item2 = types.KeyboardButton("Неважно")
            back = types.KeyboardButton("Назад")
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, "Онгоинг/неважно(^.~)", reply_markup=markup)
        elif 'Меню' in message.text:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Жанр аниме(o^ ^o)")
            item2 = types.KeyboardButton("Количество серийづ◡﹏◡)づ")
            item3 = types.KeyboardButton("Онгоинг/неважно(^.~)")

            markup.add(item1, item2, item3, )

            mess = f'Меню:'
            bot.send_message(message.chat.id, mess.format(message.from_user), reply_markup=markup)


bot.polling(none_stop=True)
