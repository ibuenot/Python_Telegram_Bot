class Pregunta:
    def __init__(self,texto:str, opciones: list, respuesta:int):
        self.texto = texto
        self.opciones = opciones
        self.respuesta = respuesta

    def responder(self, respuesta_usuario:int,) ->str:
        msg = f'Has fallado, la respuesta correcta era {self.respuesta}'
        if respuesta_usuario == self.respuesta:
            msg = 'Has acertado'
        return msg