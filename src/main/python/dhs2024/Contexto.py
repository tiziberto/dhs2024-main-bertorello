from ID import Funcion, Variable, TipoDatoFunc, TipoDatoVar, ID

class Contexto():
    def __init__(self):
        self.tabla = {} 

    def obtener_id(self, nombre: str) -> ID:
        return self.tabla.get(nombre)   #si tiene id nos lo devuelve, sino deberia devolver NONE (probarlo bien)
    
    def id(self) -> dict:
        return self.id

    def imprimirTabla(self):
        for clave, valor in self.tabla.items():
            print("clave:valor"+f"{clave: valor}")

    def traerVariable(self, nombre):
        if nombre in self.tabla:
            return self.tabla[nombre]
        else:
            return None
        