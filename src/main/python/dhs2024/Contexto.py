from ID import Funcion, Variable, TipoDatoFuncion, TipoDatoVariable, ID

class Contexto():
    #funcion1 = Funcion('func' , TipoDatoFuncion.INT.name, True , True, [1,2,3])
    #print(funcion1._getattribute_('argumentos'))
    tabla = dict()

    def __init__(self):
        self.tabla = dict()  #para iniciar la taabla como diccionario vacio

    def __init__(self, nombre: str, id: ID): 
         self.tabla[nombre] = id 

    def obtener_id(self, nombre: str) -> ID:
        return self.tabla.get(nombre)   #si tiene id nos lo devuelve, sino deberia devolver NONE (probarlo bien)