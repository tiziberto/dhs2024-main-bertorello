from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from TablaSimbolos import TablaSimbolos
from Contexto import Contexto
from ID import ID

class Escucha (compiladoresListener) :
    numTokens = 0
    numNodos  = 0

    tablasimbolos = TablaSimbolos()

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
        return super().enterIwhile(ctx)

    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        if ctx.getChild(1).getText()!='(': 
            print ("-----ERROR SINTACTICO: Falta parentesis apertura en WHILE-----")
            return None
        if ctx.getChild(3).getText()!=')': 
            print ("Child 3: "+ctx.getChild(3).getText())
            print ("-----ERROR SINTACTICO: Falta parentesis cierre en WHILE-----")
            return None
        #print("\tCantidad hijos: " + str(ctx.getChildCount()))
        #print("\tTokens: " + ctx.getText())
        print("Fin WHILE")

    #FOR:
    def enterIfor(self, ctx:compiladoresParser.IforContext):
        print("Encontre FOR")
        return super().enterIfor(ctx)

    def exitIfor(self, ctx:compiladoresParser.IforContext):
        if ctx.getChild(1).getText()!='(': 
            print ("-----ERROR SINTACTICO: Falta parentesis apertura en FOR-----")
            return None
        if ctx.getChild(7).getText()!=')': 
            print ("Child 3: "+ctx.getChild(3).getText())
            print ("-----ERROR SINTACTICO: Falta parentesis cierre en FOR-----")
            return None
        print("Fin FOR")  

    #IF:
    def enterIif(self, ctx:compiladoresParser.IifContext):
        print("Encontre IF")
        return super().enterIif(ctx)

    def exitIif(self, ctx:compiladoresParser.IifContext):
        if ctx.getChild(1).getText()!='(': 
            print ("-----ERROR SINTACTICO: Falta parentesis apertura en IF-----")
            return None
        if ctx.getChild(3).getText()!=')': 
            print ("Child 3: "+ctx.getChild(3).getText())
            print ("-----ERROR SINTACTICO: Falta parentesis cierre en IF-----")
            return None
        print("Fin IF")  

    #ELSE:
    def enterElse(self, ctx:compiladoresParser.ElseContext):
        print("Encontre IF") 
        contexto = Contexto()
        self.tablasimbolos.addContexto(contexto)

    def exitElse(self, ctx:compiladoresParser.ElseContext):
        self.tablasimbolos.delContexto()
        print("Fin IF")  

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
        self.tablasimbolos.addContexto(contexto)
    
    def exitBloque(self, ctx):
        print("Salida BLOQUE")
        print("\tCantidad hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
        print("Se encontro:\n")
        #self.TablaSimbolos.contextos.imprimirTabla()
        #TablaSimbolos.delContexto()
        return super().exitBloque(ctx)
    
    #VARIABLES:
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print("Inicializacion de una variable")
        return super().enterDeclaracion(ctx)
    
    def exitDeclaracion (self, ctx: compiladoresParser.DeclaracionContext):
        tipoDato = ctx.getChild(0).getText()
        nombre = ctx.getChild(1).getText()
        comprobarGlobal = self.tablasimbolos.buscarGlobal(nombre)

        if comprobarGlobal is not None:
            if self.tablasimbolos.buscarLocal(nombre) is not None:
                print("Variable agregada con exito")
                print("\ntipo: "+ tipoDato  + "\tNombre: "+nombre+"\n")
            else: print("el id esta usado")
        else: print("el id ya fue usado")

        

    #INSTRUCCION
    def enterInstruccion(self, ctx: compiladoresParser.InstruccionContext):
            pass

    def exitInstruccion(self, ctx: compiladoresParser.InstruccionContext):
        if ctx.declaracion() or ctx.asignacion() or ctx.return_call() or ctx.llamadaFunc(): #funciones con PYC
            numHijos = ctx.getChildCount()
            if numHijos > 0: 
                ultimoHijo = ctx.getChild(numHijos - 1)
                if ultimoHijo.getText() != ';': 
                    print('ERROR SINTACTICO: falta un ;')

    #VARIABLES
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print(" ### Declaracion iniciada")
        #pass

    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        listaVariables = []
        print("Tipo dato variable: " + ctx.getChild(0).getText())
        for i in range (1, ctx.getChildCount(),2):
            text_child = ctx.getChild(i).getText()
            if text_child == ';' or text_child == ',' or text_child == '<missing ID>':
                print('ERROR SINTACTICO: declaracion en formato invalido')
                return None
            elif ctx.getChild(i).getSymbol().type == compiladoresParser.ID:
                listaVariables.append(ctx.getChild(i).getText())
            else: 
                print('ERROR SINTACTICO: falta un ID')
        for nombreVariable in listaVariables:
            if (self.tablasimbolos.buscarGlobal(nombreVariable)) is not None:
                print('ERROR SEMANTICO: la variable "+nombreVariable+"ya existe (global)')
            elif (self.tablasimbolos.buscarLocal(nombreVariable)) is not None:
                print('ERROR SEMANTICO: la variable "+nombreVariable+"ya existe (local)')
            else:
                print('la variable '+nombreVariable+' se agrego a la lista de simbolos')
                self.tablasimbolos.addIdentificador(nombreVariable, ctx.getChild(0).getText())

    #ASIGNACION
    def enterAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        pass

    def exitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        nombreVar = ctx.getChild(0).getText()
        print('solicitud asignacion para la variable: '+nombreVar+'\n')

        cantHijos = ctx.getChildCount()
        varLocal = self.tablasimbolos.buscarLocal(nombreVar)
        varGlobal = self.tablasimbolos.buscarGlobal(nombreVar)
        tipoDatoIzquierda = None
        tipoDatoDerecha = None

        if varLocal is not None:
            print('La variable '+nombreVar+'existe (LOCAL)')
            tipoDatoIzquierda = varLocal.tipoDato
            varLocal.inicializado = 1 
        elif varGlobal is not None:
            print('La variable '+nombreVar+'existe (GLOBAL)' )
            tipoDatoIzquierda = varGlobal.tipoDato
            varGlobal.inicializado = 1 
        else:
            print('ERROR SEMANTICO: La variable '+ nombreVar + ' no fue declarada')

        nombreVarUsada = ctx.getChild(2).getText()
        partes = re.split("[+\-*]", nombreVarUsada)
        for i in partes:
            if i.isdigit():
                print(str(tipoDatoIzquierda))
                tipoDatoDerecha = 'TipoDato.INT'
                if tipoDatoDerecha != str(tipoDatoIzquierda)
                    if str(tipoDatoIzquierda) != 'TipoDato.FLOAT':
                        print('ERROR SEMANTICO: Formato de variable no compatible')
                        if varGlobal is not None:
                            varGlobal.inicializado=0
                        elif varLocal is not None:
                            varLocal.inicializado=0
            else:
                varUsadaGlobal = self.tablasimbolos.buscarGlobal(i)
                varUsadaLocal = self.tablasimbolos.buscarLocal(i)

                if varUsadaLocal is not None:
                    if varUsadaLocal.inicializado == 1:
                        varUsadaLocal.usado = 1
                        tipoDatoDerecha = varUsadaLocal.tipoDato
                    else:
                        tipoDatoDerecha = varUsadaLocal.tipoDato
                        print('ERROR SEMANTICO: La variable '+i+' no fue inicializada')
                elif varUsadaGlobal is not None:
                    if varUsadaGlobal.inicializado == 1:
                        varUsadaGlobal.usado = 1
                        tipoDatoDerecha = varUsadaGlobal.tipoDato
                    else:
                        tipoDatoDerecha = varUsadaGlobal.tipoDato
                        print('ERROR SEMANTICO: La variable: '+i+' no fue inicializada')
                if tipoDatoDerecha != tipoDatoIzquierda:
                    if varUsadaGlobal is not None:
                        varUsadaGlobal.usado = 0
                        varGlobal.inicializado = 0
                    elif varUsadaLocal is not None:
                        varUsadaLocal.usado = 0
                        varLocal.inicializado = 0
                    print('ERROR SEMANTICO: Incompatibilidad con los datos')


        return None
    
    #PROTOTIPO FUNCION
    def enterPrototipofunc(self, ctx: compiladoresParser.PrototipofuncContext):
        pass

    def exitPrototipofunc(self, ctx: compiladoresParser.PrototipofuncContext):
        return None
    
    #FUNCION
    def enterFunc(self, ctx):
        return super().enterFunc(ctx)
    

