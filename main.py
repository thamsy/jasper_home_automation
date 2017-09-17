import telegram_bot
import logging

logging.basicConfig(level=logging.INFO)
telegram_bot.updater.start_polling()