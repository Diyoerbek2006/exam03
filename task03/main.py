from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from image_bot import ImageBot

TOKEN = "8356084587:AAFdcXzWSWI8gFlofAny1sZzyRm0nXe3sKI"


def main():
    bot = ImageBot(token=TOKEN)

    updater = Updater(bot.token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", bot.handlers.start_command))
    dp.add_handler(CommandHandler("dog", bot.handlers.dog_command))
    dp.add_handler(CommandHandler("cat", bot.handlers.cat_command))
    dp.add_handler(CommandHandler("fox", bot.handlers.fox_command))
    dp.add_handler(CallbackQueryHandler(bot.handlers.button_handler))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
