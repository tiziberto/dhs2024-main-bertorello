from ID import Funcion, Variable, TipoDatoFuncion, TipoDatoVariable, ID

class Contexto():
    #funcion1 = Funcion('func' , TipoDatoFuncion.INT.name, True , True, [1,2,3])
    #print(funcion1._getattribute_('argumentos'))
    tabla = dict()
    def _init_(self, nombre, ID): 
        self.tabla.update({nombre : ID})