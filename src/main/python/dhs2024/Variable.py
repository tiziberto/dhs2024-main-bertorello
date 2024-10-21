from ID import ID, TipoDatoVar

class Variable(ID):
    def __init__(self, nombre, tipoDato, inicializado, usado):
        super().__init__(nombre, tipoDato, inicializado, usado)

    def marcar_inicializada (self):
        marcar_inicializada = True

    
    def marcar_usada (self):
        marcar_usada = True