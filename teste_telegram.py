from telegram import Bot

# Token e ID fixos (apenas para teste rápido)
TOKEN = "7682503896:AAH8AniMCJHIs8s-mfeE23TWqArmiXto_FU"
CHAT_ID = "5845175811"

bot = Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text="🚀 Teste de envio de mensagem com sucesso!")
