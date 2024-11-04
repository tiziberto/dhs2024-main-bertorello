class Contexto():
    def __init__(self):
        self.tabla = {} 

    def imprimirTabla(self):
        for clave, valor in self.tabla.items():
            print("clave:valor"+f"{clave}:{valor}")

    def traerVariable(self, nombre):
        if nombre in self.tabla:
            #print("Enviando contexto>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            return self.tabla[nombre]
        else:
            #print("SIN contexto>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            return None
        