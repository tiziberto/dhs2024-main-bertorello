from ID import Funcion, Variable, TipoDatoFunc, TipoDatoVar, ID

class Contexto():
    def __init__(self):
        self.tabla = {} 

    def __init__(self, nombre: str, id: ID): 
         self.tabla[nombre] = id 

    def obtener_id(self, nombre: str) -> ID:
        return self.tabla.get(nombre)   #si tiene id nos lo devuelve, sino deberia devolver NONE (probarlo bien)
    
    def id(self) -> dict:
        return self.id

    def imprimirTabla(self):
        for clave, valor in self.tabla.items():
            print(f"{clave: valor}")