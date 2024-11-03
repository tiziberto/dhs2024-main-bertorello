from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from TablaSimbolos import TablaSimbolos
from Contexto import Contexto
from ID import ID

class Escucha (compiladoresListener) :
    numTokens = 0
    numNodos  = 0

    TablaSimbolos = TablaSimbolos()

    #PROGRAMA:
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Comienza la compilacion")

    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Fin de la compilacion")
        print("Se encontraron")
        print("\tNodos:  " + str(self.numNodos)) 
        print("\tTokens: " + str(self.numTokens))

    #WHILE:
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        print("Encontre WHILE")
        #print("\tCantidad hijos: " + str(ctx.getChildCount()))
        #print("\tTokens: " + ctx.getText()) 

    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        print("FIN del WHILE")
        print("\tCantidad hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
        print("Fin WHILE")


    #VARIABLES
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print(" ### Declaracion")

    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print("Nombre variable: " + ctx.getChild(1).getText())

    #TOKENS
    def visitTerminal(self, node: TerminalNode):
        print(" ---> Token: " + node.getText())
        self.numTokens += 1
    
    #ERRORES
    def visitErrorNode(self, node: ErrorNode):
        print(" ---> ERROR")
    
    #NODOS DE REGLAS
    def enterEveryRule(self, ctx):
        self.numNodos += 1

    # BLOQUE:
    def enterBloque(self, ctx: compiladoresParser.BloqueContext):
        print("Encontre BLOQUE")
        contexto = Contexto()
        self.TablaSimbolos.addContexto(contexto)
    
    def exitBloque(self, ctx):
        print("Salida BLOQUE")
        print("\tCantidad hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
        print("Se encontro:\n")
        self.TablaSimbolos.imprimirTabla()
        #TablaSimbolos.delContexto()
        return super().exitBloque(ctx)
    
    #VARIABLES:
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print("Inicializacion de una variable")
        return super().enterDeclaracion(ctx)
    
    def exitDeclaracion (self, ctx: compiladoresParser.DeclaracionContext):
        tipoDato = ctx.getChild(0).getText()
        nombre = ctx.getChild(1).getText()
        comprobarGlobal = TablaSimbolos.buscarGlobal(TablaSimbolos, nombre)

        if comprobarGlobal == 1:
            if TablaSimbolos.buscarLocal(TablaSimbolos, nombre) == 1:
                print("Variable agregada con exito")
                print("\ntipo: "+ tipoDato  + "\tNombre: "+nombre+"\n")
            else: print("el id esta usado")
        else: ("el id ya fue usado")

        return super().exitDeclaracion(ctx)
