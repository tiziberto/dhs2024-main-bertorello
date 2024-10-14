from Contexto import Contexto

class TablaSimbolos():
    def __init__(self):
        self.contextos = list()
        self.contexto = Contexto ('global', None)
        self.contextos.append(self.contexto) 


tabla = TablaSimbolos
print(tabla.__getattribute__('contexto').__getattribute__('tabla'))

# def delContexto():