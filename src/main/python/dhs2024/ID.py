from enum import Enum
from typing import Union 

class TipoDatoFunc(Enum):
    VOID = "void"
    INT = 'int'
    FLOAT = 'float'
    BOOLEAN = 'bool' 
    DOUBLE = 'double'
    CHAR = 'char'

class TipoDatoVar(Enum):
    INT = 'int'
    FLOAT = 'float'
    BOOLEAN = 'bool' 
    DOUBLE = 'double'
    CHAR = 'char'

class ID():
    def __init__(self, nombre, tipoDato: Union[TipoDatoVar, TipoDatoFunc], inicializado, usado):
        self.nombre = nombre
        self.tipoDato = tipoDato
        self.inicializado = inicializado
        self.usado = usado

class Funcion(ID):
    def __init__(self, nombre, tipoDato: TipoDatoFunc, inicializado, usado,argumentos: list):
        super()._init_(nombre, tipoDato, inicializado, usado)
        self.argumentos = argumentos

class Variable(ID):
    def __init__(self, nombre, tipoDato: TipoDatoVar, inicializado, usado):
        super()._init_(nombre, tipoDato, inicializado, usado)