import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import logging

# Настройка логирования для отладки
logging.basicConfig(level=logging.INFO)

# Твой токен
TOKEN = '8423068213:AAE84M_f112TJ0WwwQ2A26SBVF2C9b77Rvk'
bot = telebot.TeleBot(TOKEN)

# Команда /start - показывает меню
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Купить накрутку", callback_data='buy'))
    markup.add(InlineKeyboardButton("Цены", callback_data='prices'))
    markup.add(InlineKeyboardButton("Поддержка", callback_data='support'))
    
    bot.send_message(message.chat.id, "Привет! Я бот для накрутки в соцсетях. Выбери опцию:", reply_markup=markup)

# Обработка кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'buy':
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Instagram лайки - 100 шт / 50 руб", callback_data='ig_likes'))
        markup.add(InlineKeyboardButton("VK подписчики - 200 шт / 100 руб", callback_data='vk_subs'))
        
        bot.answer_callback_query(call.id, "Выбери услугу:")
        bot.send_message(call.message.chat.id, "Что накрутить?", reply_markup=markup)
    
    elif call.data == 'prices':
        bot.answer_callback_query(call.id, "Список цен:")
        bot.send_message(call.message.chat.id, "Цены:\n- Instagram лайки: 50 руб за 100\n- VK подписчики: 100 руб за 200")
    
    elif call.data == 'support':
        bot.answer_callback_query(call.id, "Связь с поддержкой:")
        bot.send_message(call.message.chat.id, "Напиши @weshrell для вопросов")
    
    elif call.data == 'ig_likes':
        bot.answer_callback_query(call.id, "Заказ принят!")
        bot.send_message(call.message.chat.id, "Отправь ссылку на пост и переведи 50 руб на Qiwi: +1234567890. После оплаты напиши /paid")  # Замени номер
    
    elif call.data == 'vk_subs':
        bot.answer_callback_query(call.id, "Заказ принят!")
        bot.send_message(call.message.chat.id, "Отправь ссылку на страницу и переведи 100 руб на Qiwi: +1234567890. После оплаты напиши /paid")  # Замени номер

# Команда для подтверждения оплаты
@bot.message_handler(commands=['paid'])
def paid(message):
    bot.send_message(message.chat.id, "Оплата получена! Скоро начнём накрутку!")

# Функция для запуска бота с обработкой ошибок
def start_bot():
    while True:
        try:
            logging.info("Бот запускается...")
            bot.polling(none_stop=True, timeout=30)
        except Exception as e:
            logging.error(f"Ошибка: {e}")
            logging.info(f"Бот перезапускается из-за ошибки. Если это мешает, напиши @weshrell")
            time.sleep(5)  # Ждём 5 секунд перед перезапуском

# Запуск бота
if __name__ == "__main__":
    start_bot()
