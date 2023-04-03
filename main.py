import private
import commands
from telegram.ext import (Updater,CommandHandler,MessageHandler,Filters,CallbackQueryHandler,InlineQueryHandler)
from telegram import InlineQueryResultArticle, InputTextMessageContent
from random import getrandbits


def main():
    token = ''
    updater = Updater(token,use_context=True)
    dp = updater.dispatcher

    #comandos
    dp.add_handler(CommandHandler('help', commands.cmd_help))
    dp.add_handler(CommandHandler('rolld6',commands.cmd_roll_d6))
    dp.add_handler(CommandHandler('chiste', commands.cmd_chiste))
    dp.add_handler(CommandHandler('flag', commands.cmd_get_flag))
    dp.add_handler(CommandHandler('meme', commands.cmd_get_fun))
    dp.add_handler(CommandHandler('jugarroll', commands.cmd_jugar_roll))
    dp.add_handler(CommandHandler('millonario', commands.cmd_millonario))
    dp.add_handler(CallbackQueryHandler(commands.keyboard_callback))
    dp.add_handler(CommandHandler('dado',commands.cmd_roll_dice))

    dp.add_handler(InlineQueryHandler(commands.inline))



    dp.add_handler(MessageHandler(Filters.text, commands.message_handler))



    #iniciar el bot
    updater.start_polling()

    #El bot esta escuchando
    updater.idle()

if __name__ == '__main__':
    print(f'El bot está listo')
    main()