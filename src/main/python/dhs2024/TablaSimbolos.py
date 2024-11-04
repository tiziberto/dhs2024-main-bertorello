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
        #print("PRUEBA BUSCAR LOCAL")
        resultadodeBusqueda = self.contextos[-1].traerVariable(nombre)
        if resultadodeBusqueda == None:
            #print("No hay resultados")
            return None
        else: 
            return resultadodeBusqueda

    def buscarGlobal(self, nombre):
        #print("PRUEBA BUSCAR GLOBAL")
        resultadodeBusqueda = self.contextos[0].traerVariable(nombre)
        if resultadodeBusqueda == None:
            #print("No hay resultados")
            return None
        else: 
            #print("Hay resultados")
            return resultadodeBusqueda
        
    def controlarVarUsadas (self):
        noUsadas = []
        noInicializadas = []

        contexto = self.contextos[-1]
        for nombre, id in contexto.tabla.items():
            print('VAR: '+nombre+'\tUsado: '+str(id.usado)+'\tInicializado: '+str(id.inicializado))
            if id.usado == False:
                noUsadas.append(nombre)
            if id.inicializado == False:
                noInicializadas.append(nombre)
        
        print('---------VARIABLES NO USADAS:---------')
        for i in noUsadas:
            print(i+'\n')
        print('---------VARIABLES NO INICIALIZADAS:---------')
        for i in noInicializadas:
            print(i+'\n')
        

        