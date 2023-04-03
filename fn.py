import random

from telegram import InlineQueryResultArticle, InputTextMessageContent


def roll_d6():
    return random.randint(1, 6)

def chiste():
     chistes = ["¿Que le dice un bolardo a otro? Bolardo voy, bolardo vengo, vengo...",
                "¿Que le dice un jardinero a otro? Seamos felices mientras podamos",
                "¿Como se llama el hermano vegano de Bruce Lee? Broco Lee",
                "¿Que hace un tupper en un bosque? Tupperdío"]
     chiste_aleatorio = random.choice(chistes)
     return chiste_aleatorio

def get_url_flag(country:str) -> str:
    base_url = "https://countryflagsapi.com/png/"
    return base_url + country

def choose_meme() ->str:
    memes = [
        "https://i.pinimg.com/236x/fa/79/51/fa795192f0378c9ccf95e1a8547f7611.jpg",
        "https://static.eldiario.es/clip/cfad379c-f641-4a31-b0e9-0e35e2190146_twitter-aspect-ratio_default_0.jpg"

    ]
    meme_aleatorio = random.choice(memes)
    return meme_aleatorio


def get_tirada(texto:str) -> str:
    tipos_dados = texto.split('-')
    datos = [x.partition('d') for x in tipos_dados]
    datos = [roll_generic(int(x[2]), int(x[0])) for x in datos]
    return ';'.join(datos)

def roll_generic(dado:str, n_veces:int) -> str:
    tiradas = ','.join([str(random.randint(1, dado)) for x in range(n_veces)])
    return f'd{dado}({tiradas})'



