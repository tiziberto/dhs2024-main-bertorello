from enum import Enum
from typing import Union 

class TipoDatoFunc(Enum):
    VOID = "void"
    INT = 'int'
    FLOAT = 'float'
    BOOLEAN = 'bool' 
    DOUBLE = 'double'
    CHAR = 'char'

class ID():
    def __init__(self, nombre, tipoDato, declarado = False, inicializado = False, usado = False):
        self.nombre = nombre
        self.tipoDato = TipoDatoFunc(tipoDato)
        self.declarado = declarado
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
    def __init__(self, nombre, tipoDato, declarado, inicializado, usado):
        super()._init_(nombre, tipoDato, declarado, inicializado, usado)

    def marcar_declarada (self):
        marcar_declarada = True

    def marcar_inicializada (self):
        marcar_inicializada = True

    def marcar_usada (self):
        marcar_usada = True