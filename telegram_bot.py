# telegram_bot.py
from telegram import Bot

TOKEN_TELEGRAM = "7682503896:AAH8AniMCJHIs8s-mfeE23TWqArmiXto_FU"
ID_CHAT_TELEGRAM = "5845175811"

def enviar_mensagem(texto):
    bot = Bot(token=TOKEN_TELEGRAM)
    bot.send_message(chat_id=ID_CHAT_TELEGRAM, text=texto)
