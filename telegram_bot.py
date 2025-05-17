# telegram_bot.py
from telegram import Bot
from settings import TOKEN_TELEGRAM, ID_CHAT_TELEGRAM

def enviar_mensagem(texto):
    bot = Bot(token=TOKEN_TELEGRAM)
    bot.send_message(chat_id=ID_CHAT_TELEGRAM, text=texto)
