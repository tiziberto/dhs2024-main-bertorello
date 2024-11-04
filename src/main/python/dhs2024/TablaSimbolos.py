from Contexto import Contexto
from ID import ID

class TablaSimbolos(object):
    __instance= None
    contextos = []

    def __new__(cls):
        if TablaSimbolos.__instance is None:
            TablaSimbolos.__instance = object.__new__(cls)
        return TablaSimbolos.__instance

    def __init__(self):
        contextoGlobal = Contexto ()
        self.contextos.append(contextoGlobal) 

    def addContexto(self, contexto):
        self.contextos.append(contexto)

    def delContexto(self):
        self.contextos.pop()

    def addIdentificador(self, nombre, tipodeDato):
        contexto=self.contextos[-1]
        id=ID(nombre,tipodeDato,True,False,False)
        contexto.tabla.update({nombre:id})



    def buscarLocal(self, nombre):
        print("PRUEBA BUSCAR LOCAL")
        resultadodeBusqueda = self.contextos[-1].traerVariable(nombre)
        if (resultadodeBusqueda) == None:
            print("No hay resultados")
            return 1
        else: 
            return resultadodeBusqueda

    def buscarGlobal(self, nombre):
        print("PRUEBA BUSCAR GLOBAL")
        if (self.contextos[0].traerVariable(nombre)) == None:
            print("No hay resultados")
            return None
        else: 
            resultado = self.contextos[0].traerVariable(nombre)
            print("Hay resultados")
            return resultado