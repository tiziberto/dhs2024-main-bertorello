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
    def __init__(self, nombre, tipoDato: Union[TipoDatoVar, TipoDatoFunc], inicializado = False, usado = False):
        self.nombre = nombre
        self.tipoDato = tipoDato
        self.inicializado = inicializado
        self.usado = usado

    def __str__(self):
        return ("ID: "+self.nombre+"\tTipo dato: "+str(self.tipoDato)+"\tInicializado: "+str(self.inicializado)+"\tUsado: "+str(self.usado))
        

class Funcion(ID):
    def __init__(self, nombre, tipoDato: TipoDatoFunc, inicializado, usado,argumentos: list):
        super()._init_(nombre, tipoDato, inicializado, usado)
        self.argumentos = argumentos
       
    def agregar_argumento(self, argumento: ID):
        self.argumentos.append(argumento)

    def obtener_argumento(self):
        return self.argumentos
    

class Variable(ID):
    def __init__(self, nombre, tipoDato: TipoDatoVar, inicializado, usado):
        super()._init_(nombre, tipoDato, inicializado, usado)

    def marcar_inicializada (self):
        marcar_inicializada = True

    
    def marcar_usada (self):
        marcar_usada = True