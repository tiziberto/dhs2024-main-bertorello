from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser

class Walker (compiladoresVisitor):
    def visitPrograma(self, ctx):
        print("=-"*20)
        print("-- Comienza a caminar")
        return super().visitPrograma(ctx)
    
    def visitDeclaracion(self, ctx):
        print(ctx.getChild(0).getText()+" - "+ ctx.getChild(1).getText())
        return None

    def visitBloque(self, ctx):
        print("Nuevo Contexto")
        print (ctx.getText())
        return super().visitInstrucciones(ctx.getChild(1))

    def visitTerminal(self, node):
        print("==>> Token "+ node.getText())
        return super().visitTerminal(node)