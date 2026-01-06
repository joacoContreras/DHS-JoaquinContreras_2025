from compiladorVisitor import compiladorVisitor
from compiladorParser import compiladorParser

class Caminante(compiladorVisitor):
    instr = 0
    hojas = 0
    
    def visitPrograma (self, ctx:compiladorParser.ProgramaContext):
        """Visita el nodo programa"""
        print("Programa Procesado")
        return self.visitChildren(ctx)
    
    def visitAsignacion (self, ctx:compiladorParser.AsignacionContext):
        """Visita el nodo asignación"""
        print("Declaracion " + str(self.instr))
        print("\t" + ctx.getText())
        return self.visitChildren(ctx)
    
    def visitDeclaracion(self, ctx):
        print("Declaracion " + str(self.instr))
        print("\t" + ctx.getText())
        return self.visitChildren(ctx)
    
    def visitIwhile(self, ctx):
        # for i in list(range(ctx.getChildCount())):
        #     print(self.visitChildren(ctx.getText()))
        print("Entro al while")
        return self.visitChildren(ctx)
    
    def visitTerminal(self, node):
        self.hojas += 1
        print("Hoja " + str(self.hojas) + " -> |" + node.getText() + "|")
        return super().visitTerminal(node)
    
    def primerNumeroHojas (self):
        print("Hojas: " + str(self.hojas))
        