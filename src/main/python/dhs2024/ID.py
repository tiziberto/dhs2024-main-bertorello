from enum import Enum

class TipoDatoFuncion(Enum):
    VOID = "void"
    INT = 'int'
    FLOAT = 'float'
    BOOLEAN = 'bool' 
    DOUBLE = 'double'
    CHAR = 'char'

class TipoDatoVariable(Enum):
    INT = 'int'
    FLOAT = 'float'
    BOOLEAN = 'bool' 
    DOUBLE = 'double'
    CHAR = 'char'

class ID():
    def _init_(self, nombre, tipoDato, inicializado, usado):
        self.nombre = nombre
        self.tipoDato = tipoDato
        self.inicializado = inicializado
        self.usado = usado

class Funcion(ID):
    def _init_(self, nombre, tipoDato: TipoDatoFuncion, inicializado, usado,argumentos: list):
        super()._init_(nombre, tipoDato, inicializado, usado)
        self.argumentos = argumentos

class Variable(ID):
    def _init_(self, nombre, tipoDato: TipoDatoVariable, inicializado, usado):
        super()._init_(nombre, tipoDato, inicializado, usado)