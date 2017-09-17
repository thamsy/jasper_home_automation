from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler
from telegram.ext import Filters
import telegram
import logging
import secret
import commands

logger = logging.getLogger(__name__)

updater = Updater(token=secret.bot_token)
dispatcher = updater.dispatcher

### Helper ###

def auth(update):

    if (update.message != None and update.message.chat_id != secret.user_id) or \
            (update.callback_query != None and update.callback_query.from_user.id != secret.user_id):
        logger.warn("Invalid user access: " + str(update.message.chat_id))
        return False

    return True

### Main methods ###

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Welcome!")


def youtube(bot, update):
    logger.debug(youtube.__name__ + " reached")
    if not auth(update):
        return
    args = update.message.text
    video_title = commands.play_youtube(args)
    bot.send_message(chat_id=update.message.chat_id, text="Playing: " + video_title)

def music_controls(bot, update):
    logger.debug(music_controls.__name__ + " reached")
    if not auth(update):
        return

    play_button = telegram.InlineKeyboardButton("Play", callback_data="play")
    pause_button = telegram.InlineKeyboardButton("Pause", callback_data="pause")
    vol0_button = telegram.InlineKeyboardButton("Vol 0%", callback_data="vol0")
    vol25_button = telegram.InlineKeyboardButton("25%", callback_data="vol25")
    vol50_button = telegram.InlineKeyboardButton("50%", callback_data="vol50")
    vol75_button = telegram.InlineKeyboardButton("75%", callback_data="vol75")
    vol100_button = telegram.InlineKeyboardButton("100%", callback_data="vol100")
    inline_keyboard = [[play_button, pause_button], [vol0_button, vol25_button, vol50_button, vol75_button, vol100_button]]
    inline_keyboard_markup = telegram.InlineKeyboardMarkup(inline_keyboard)
    bot.send_message(chat_id=update.message.chat_id, text="Music Controls",
                     reply_markup=inline_keyboard_markup)

def music_controller(bot, update):
    logger.debug(music_controller.__name__ + " reached")
    if not auth(update):
        return

    control = update.callback_query.data
    if control == "play":
        commands.resume()
    elif control == "pause":
        commands.pause()
    elif control == "vol0":
        commands.vol(0)
    elif control == "vol25":
        commands.vol(25)
    elif control == "vol50":
        commands.vol(50)
    elif control == "vol75":
        commands.vol(75)
    elif control == "vol100":
        commands.vol(100)
    else:
        logging.warn("Call back handler not implemented")

    bot.answerCallbackQuery(callback_query_id=update.callback_query.id, text=update.callback_query.data)






start_handler = CommandHandler('start', start)
youtube_handler = MessageHandler(Filters.text, youtube)
music_controls_handler = CommandHandler('music_controls', music_controls)
music_controller_handler = CallbackQueryHandler(music_controller)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(youtube_handler)
dispatcher.add_handler(music_controls_handler)
dispatcher.add_handler(music_controller_handler)


# bot.send_message(chat_id=update.message.chat_id, text="Remove Reply Keyboard", reply_markup=telegram.ReplyKeyboardRemove())