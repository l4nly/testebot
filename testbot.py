import os
from telegram.ext import Updater, MessageHandler, Filters


def handle_media(update, context):
    message = "ta pago"
    update.message.reply_text(message)


if __name__ == '__main__':
    updater = Updater(token=os.environ['5921944522:AAFPEk-0oCuNNEdH8vgc54uqxremCjEO1TM'], use_context=True)
    dispatcher = updater.dispatcher
    media_handler = MessageHandler(Filters.media, handle_media)
    dispatcher.add_handler(media_handler)
    updater.start_polling()
    updater.idle()
