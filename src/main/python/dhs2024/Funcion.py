from enum import Enum
from ID import ID, TipoDatoFunc

class Funcion(ID):
    def __init__(self, nombre, tipoDato, inicializado, usado):
        super().__init__(nombre, tipoDato, inicializado, usado)
       
    def agregar_argumento(self, argumento: ID):
        self.argumentos.append(argumento)

    def obtener_argumento(self):
        return self.argumentos