import random
import numexpr
from telegram import (ParseMode, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton,
                      InlineQueryResultArticle, InputTextMessageContent)
import fn
import threading
from bd_preguntas import preguntas
from html import escape
from uuid import uuid4

p = random.choice(preguntas)

def keyboard_callback(update,context):
    respuesta_usuario = update.callback_query.data
    msg = p.responder(int(respuesta_usuario))
    chat_id = update.callback_query.message.chat_id
    context.bot.send_message(chat_id, msg)

def cmd_roll_d6(update,context):
    result = fn.roll_d6()
    context.bot.send_message(update.message.chat_id, str(result))


def cmd_chiste(update,context):
    result = fn.chiste()
    context.bot.send_message(update.message.chat_id, str(result))


def cmd_get_flag(update,context):
    url = fn.get_url_flag(context.args[0])
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id,url)

def cmd_get_fun(update,context):
    meme_url = fn.choose_meme()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id,meme_url)

def cmd_jugar_roll(update,context):
    chat_id = update.message.chat_id
    respuesta = fn.get_tirada(context.args[0])
    context.bot.send_message(chat_id,respuesta)

def cmd_help(update,context):
    msg = """
    Los comandos del bot son:
    <b>rolld6</b> ---> Lanza un dado
    <b>flag X </b> ---> Muestra la bandera del país X
    <b>jugarroll</b> ---> Lanza un dado para jugar rol
    """
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id,msg, parse_mode='HTML')


def message_handler(update,context):
    msg = update.message.text

    if msg[0] == '=':
        cuenta = msg[1:]
        resultado = str(numexpr.evaluate(cuenta))
        update.message.reply_text(resultado)
    elif msg in ["d4","d6","d8","d10","d12","d20","d50","d100"]:
        n = msg[1:]

    else:
        update.message.reply_text(msg)

def cmd_roll_dice(update,context):
    teclado = [
        ["d4","d6"],
        ["d8","d10","d12"],
        ["d20","d50","d100"],
    ]
    teclado_telegram = ReplyKeyboardMarkup(
        teclado,
        one_time_keyboard=True,
        resize_keyboard=True
    )

    update.message.reply_text("Elige un dado", reply_markup=teclado_telegram)


def cmd_millonario(update,context):
    p = random.choice(preguntas)
    teclado = [
        [p.opciones[0], p.opciones[1]],
        [p.opciones[2], p.opciones[3]],

    ]

    teclado2 = [
        [
            InlineKeyboardButton(p.opciones[0],callback_data='0'),
            InlineKeyboardButton(p.opciones[1], callback_data='1'),
        ],
        [
            InlineKeyboardButton(p.opciones[2], callback_data='2'),
            InlineKeyboardButton(p.opciones[3], callback_data='3')
        ]
    ]

    teclado_telegram = InlineKeyboardMarkup(
        teclado2,
        one_time_keyboard=True,
        resize_keyboard=True

    )

    update.message.reply_text(p.texto, reply_markup=teclado_telegram)


def inline(update,context):
    query = update.inline_query.query
    if query == "":
        return

    bienvenida_inline = 'Bienvenido ' + query
    busqueda_inline = 'https://www.google.es'
    help = """
        Los comandos del bot son:
        <b>/rolld6</b> ---> Lanza un dado
        <b>/flag X </b> ---> Muestra la bandera del país X
        <b>/jugarroll</b> ---> Lanza un dado para jugar rol
        """
    chiste_inline = fn.chiste()

    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Ayuda del bot",
            input_message_content=InputTextMessageContent(help,parse_mode=ParseMode.HTML),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Bienvenida",
            input_message_content=InputTextMessageContent(bienvenida_inline),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Chiste",
            input_message_content=InputTextMessageContent(chiste_inline),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Buscar en Google",
            input_message_content=InputTextMessageContent(busqueda_inline),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Mayusculas",
            input_message_content=InputTextMessageContent(query.upper()),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Negrita",
            input_message_content=InputTextMessageContent(
                f"<b>{escape(query)}</b>", parse_mode=ParseMode.HTML
            ),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Italica",
            input_message_content=InputTextMessageContent(
                f"<i>{escape(query)}</i>", parse_mode=ParseMode.HTML
            ),
        )

    ]

    update.inline_query.answer(results)

