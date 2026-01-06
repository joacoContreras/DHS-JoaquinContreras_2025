"""
Generador de Código Intermedio (Three Address Code - TAC)
Convierte el AST en instrucciones de tres direcciones
"""
from compiladorVisitor import compiladorVisitor
from compiladorParser import compiladorParser

class IntermediateCodeGenerator(compiladorVisitor):
    """
    Genera código de tres direcciones a partir del árbol sintáctico.
    
    El código de tres direcciones tiene la forma:
        resultado = operando1 op operando2
    
    Donde cada instrucción tiene como máximo un operador y tres operandos.
    """
    
    def __init__(self):
        self.codigo = []  # Lista de instrucciones TAC
        self.temp_counter = 0  # Contador para temporales (t0, t1, t2, ...)
        self.label_counter = 0  # Contador para etiquetas (L0, L1, L2, ...)
        self.indentacion = 0  # Para mejor visualización
        
    def nuevo_temporal(self):
        """Genera un nuevo nombre de variable temporal"""
        temp = f"t{self.temp_counter}"
        self.temp_counter += 1
        return temp
    
    def nueva_etiqueta(self):
        """Genera una nueva etiqueta para saltos"""
        label = f"L{self.label_counter}"
        self.label_counter += 1
        return label
    
    def emitir(self, instruccion):
        """Agrega una instrucción al código generado"""
        indent = "  " * self.indentacion
        self.codigo.append(indent + instruccion)
        return instruccion
    
    def obtener_codigo(self):
        """Retorna todo el código generado como string"""
        return "\n".join(self.codigo)
    
    # ========== VISITADORES PARA EXPRESIONES ==========
    
    def visitOpal(self, ctx):
        """Visita operación algebraica/lógica y retorna el temporal con el resultado"""
        return self.visit(ctx.exp())
    
    def visitExp(self, ctx):
        """
        Maneja expresiones: exp = term e
        Donde e puede ser: + term e | - term e | vacio
        """
        # Obtener el primer term
        result = self.visit(ctx.term())
        
        # Si hay 'e' (expresiones adicionales)
        if ctx.e():
            result = self.visit_e(ctx.e(), result)
        
        return result
    
    def visit_e(self, ctx, left_operand):
        """
        Procesa la continuación de expresión (e)
        e : SUMA term e | RESTA term e | vacío
        """
        if ctx.getChildCount() == 0:
            # Es epsilon (vacío)
            return left_operand
        
        # Obtener el operador
        op = ctx.getChild(0).getText()  # SUMA o RESTA
        
        # Obtener el term
        right = self.visit(ctx.term())
        
        # Generar temporal para el resultado
        result = self.nuevo_temporal()
        self.emitir(f"{result} = {left_operand} {op} {right}")
        
        # Si hay más 'e', procesar recursivamente
        if ctx.e():
            return self.visit_e(ctx.e(), result)
        
        return result
    
    def visitTerm(self, ctx):
        """
        Maneja términos: term = factor (t | l)
        t: operaciones multiplicativas
        l: operaciones comparativas
        """
        # Obtener el primer factor
        result = self.visit(ctx.factor())
        
        # Si hay 't' (multiplicación/división/módulo)
        if ctx.t():
            result = self.visit_t(ctx.t(), result)
        
        # Si hay 'l' (comparaciones)
        if ctx.l():
            result = self.visit_l(ctx.l(), result)
        
        return result
    
    def visit_t(self, ctx, left_operand):
        """
        Procesa operaciones multiplicativas (t)
        t : MULT factor t | DIV factor t | MOD factor t | vacío
        """
        if ctx.getChildCount() == 0:
            return left_operand
        
        # Obtener el operador
        op = ctx.getChild(0).getText()  # *, /, %
        
        # Obtener el factor
        right = self.visit(ctx.factor())
        
        # Generar temporal
        result = self.nuevo_temporal()
        self.emitir(f"{result} = {left_operand} {op} {right}")
        
        # Si hay más 't', procesar recursivamente
        if ctx.t():
            return self.visit_t(ctx.t(), result)
        
        return result
    
    def visit_l(self, ctx, left_operand):
        """
        Procesa operaciones comparativas (l)
        l : MENOR | MAYOR | MENOREQ | MAYOREQ | EQUAL | NEQUAL factor l | vacío
        """
        if ctx.getChildCount() == 0:
            return left_operand
        
        # Obtener el operador
        op = ctx.getChild(0).getText()  # <, >, <=, >=, ==, !=
        
        # Obtener el factor
        right = self.visit(ctx.factor())
        
        # Generar temporal
        result = self.nuevo_temporal()
        self.emitir(f"{result} = {left_operand} {op} {right}")
        
        # Si hay más 'l', procesar recursivamente
        if ctx.l():
            return self.visit_l(ctx.l(), result)
        
        return result
    
    def visitFactor(self, ctx):
        """
        Maneja factores: números, variables, expresiones entre paréntesis, llamadas a función
        factor : (exp) | NUMERO | ID | ID(argumentos?)
        """
        # Si es un número
        if ctx.NUMERO():
            return ctx.NUMERO().getText()
        
        # Si es un identificador
        elif ctx.ID():
            # Verificar si es una llamada a función (tiene paréntesis)
            if ctx.PA():
                # Es una llamada a función
                func_name = ctx.ID().getText()
                
                # Procesar argumentos si existen
                if ctx.argumentos():
                    args = self.visit(ctx.argumentos())
                    # Generar código para pasar argumentos
                    for i, arg in enumerate(args):
                        self.emitir(f"param {arg}")
                
                # Generar la llamada
                result = self.nuevo_temporal()
                self.emitir(f"{result} = call {func_name}")
                return result
            else:
                # Es solo una variable
                return ctx.ID().getText()
        
        # Si es una expresión entre paréntesis
        elif ctx.PA():
            return self.visit(ctx.exp())
        
        return self.visitChildren(ctx)
    
    def visitArgumentos(self, ctx):
        """Procesa la lista de argumentos de una función"""
        args = []
        # Cada argumento es un opal
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if hasattr(child, 'getRuleIndex'):  # Es un nodo opal
                args.append(self.visit(child))
        return args
    
    # ========== VISITADORES PARA SENTENCIAS ==========
    
    def visitAsignacion(self, ctx):
        """
        Genera código para asignación: ID = opal;
        Soporta: =, +=, -=, *=, /=, %=
        """
        variable = ctx.ID().getText()
        
        # Obtener el operador de asignación
        op_asig = ctx.getChild(1).getText()
        
        # Visitar la expresión
        valor = self.visit(ctx.opal())
        
        if op_asig == '=':
            # Asignación simple
            self.emitir(f"{variable} = {valor}")
        else:
            # Asignación compuesta (+=, -=, etc.)
            # Convertir += a +, -= a -, etc.
            op = op_asig[0]  # Toma el primer carácter (+, -, *, /, %)
            result = self.nuevo_temporal()
            self.emitir(f"{result} = {variable} {op} {valor}")
            self.emitir(f"{variable} = {result}")
        
        return None
    
    def visitDeclaracion(self, ctx):
        """
        Genera código para declaración: tipo ID (= opal)? (, ID (= opal)?)* ;
        """
        # Procesar la primera variable
        variable = ctx.ID().getText()
        
        # Si hay inicialización
        if ctx.inic() and ctx.inic().ASIG():
            valor = self.visit(ctx.inic().opal())
            self.emitir(f"{variable} = {valor}")
        else:
            # Declaración sin inicialización
            self.emitir(f"DECLARE {variable}")
        
        # Procesar listavar (variables adicionales)
        if ctx.listavar():
            self.visit(ctx.listavar())
        
        return None
    
    def visitListavar(self, ctx):
        """Procesa lista de variables en declaración"""
        if ctx.getChildCount() == 0:
            return None
        
        variable = ctx.ID().getText()
        
        # Si hay inicialización
        if ctx.inic() and ctx.inic().ASIG():
            valor = self.visit(ctx.inic().opal())
            self.emitir(f"{variable} = {valor}")
        else:
            self.emitir(f"DECLARE {variable}")
        
        # Recursivo para más variables
        if ctx.listavar():
            self.visit(ctx.listavar())
        
        return None
    
    def visitIwhile(self, ctx):
        """
        Genera código para while: while (opal) instruccion
        
        Código generado:
            Linicio:
                if not condicion goto Lfin
                <codigo del bloque>
                goto Linicio
            Lfin:
        """
        label_inicio = self.nueva_etiqueta()
        label_fin = self.nueva_etiqueta()
        
        # Etiqueta de inicio del while
        self.emitir(f"{label_inicio}:")
        self.indentacion += 1
        
        # Evaluar condición
        condicion = self.visit(ctx.opal())
        self.emitir(f"if not {condicion} goto {label_fin}")
        
        # Código del bloque/instrucción
        self.visit(ctx.instruccion())
        
        # Salto incondicional al inicio
        self.emitir(f"goto {label_inicio}")
        
        self.indentacion -= 1
        self.emitir(f"{label_fin}:")
        
        return None
    
    def visitIfor(self, ctx):
        """
        Genera código para for: for (init; cond; iter) bloque
        
        Código generado:
            <init>
            Linicio:
                if not <cond> goto Lfin
                <codigo del bloque>
                <incremento>
                goto Linicio
            Lfin:
        """
        label_inicio = self.nueva_etiqueta()
        label_fin = self.nueva_etiqueta()
        
        # Inicialización (puede ser asignacionFor o declaracionFor)
        if ctx.asignacionFor():
            self.visit(ctx.asignacionFor(0))  # Primera asignación es la init
        elif ctx.declaracionFor():
            self.visit(ctx.declaracionFor())
        
        # Etiqueta de inicio
        self.emitir(f"{label_inicio}:")
        self.indentacion += 1
        
        # Condición (opal)
        if ctx.opal():
            condicion = self.visit(ctx.opal())
            self.emitir(f"if not {condicion} goto {label_fin}")
        
        # Bloque de código
        self.visit(ctx.bloque())
        
        # Incremento (segunda asignacionFor)
        if ctx.getChildCount() > 8 and ctx.asignacionFor(1):
            self.visit(ctx.asignacionFor(1))
        
        # Salto al inicio
        self.emitir(f"goto {label_inicio}")
        
        self.indentacion -= 1
        self.emitir(f"{label_fin}:")
        
        return None
    
    def visitAsignacionFor(self, ctx):
        """
        Procesa asignaciones dentro del for
        ID op opal | ID++ | ID--
        """
        variable = ctx.ID().getText()
        
        # Si es incremento/decremento
        if ctx.INCREMENTO():
            temp = self.nuevo_temporal()
            self.emitir(f"{temp} = {variable} + 1")
            self.emitir(f"{variable} = {temp}")
        elif ctx.DECREMENTO():
            temp = self.nuevo_temporal()
            self.emitir(f"{temp} = {variable} - 1")
            self.emitir(f"{variable} = {temp}")
        else:
            # Es asignación normal
            op_asig = ctx.getChild(1).getText()
            valor = self.visit(ctx.opal())
            
            if op_asig == '=':
                self.emitir(f"{variable} = {valor}")
            else:
                # Asignación compuesta
                op = op_asig[0]
                result = self.nuevo_temporal()
                self.emitir(f"{result} = {variable} {op} {valor}")
                self.emitir(f"{variable} = {result}")
        
        return None
    
    def visitDeclaracionFor(self, ctx):
        """Procesa declaración dentro del for"""
        variable = ctx.ID().getText()
        
        if ctx.inic() and ctx.inic().ASIG():
            valor = self.visit(ctx.inic().opal())
            self.emitir(f"{variable} = {valor}")
        else:
            self.emitir(f"DECLARE {variable}")
        
        # Procesar listavar si existe
        if ctx.listavar():
            self.visit(ctx.listavar())
        
        return None
    
    def visitIif(self, ctx):
        """
        Genera código para if-else: if (opal) instruccion (else instruccion)?
        
        if simple:
            if not <cond> goto Lfin
            <bloque>
            Lfin:
        
        if-else:
            if not <cond> goto Lelse
            <bloque_if>
            goto Lfin
            Lelse:
            <bloque_else>
            Lfin:
        """
        label_else = self.nueva_etiqueta()
        label_fin = self.nueva_etiqueta()
        
        # Condición
        condicion = self.visit(ctx.opal())
        
        # Si hay else (verificar ielse)
        if ctx.ielse() and ctx.ielse().getChildCount() > 0:
            self.emitir(f"if not {condicion} goto {label_else}")
            self.indentacion += 1
            
            # Bloque del if (primera instrucción)
            self.visit(ctx.instruccion())
            self.emitir(f"goto {label_fin}")
            
            self.indentacion -= 1
            self.emitir(f"{label_else}:")
            self.indentacion += 1
            
            # Bloque del else
            self.visit(ctx.ielse())
            
            self.indentacion -= 1
            self.emitir(f"{label_fin}:")
        else:
            # Solo if sin else
            self.emitir(f"if not {condicion} goto {label_fin}")
            self.indentacion += 1
            
            self.visit(ctx.instruccion())
            
            self.indentacion -= 1
            self.emitir(f"{label_fin}:")
        
        return None
    
    def visitIelse(self, ctx):
        """Procesa la parte else"""
        if ctx.getChildCount() > 0:
            return self.visit(ctx.instruccion())
        return None
    
    # ========== VISITADORES GENERALES ==========
    
    def visitPrograma(self, ctx):
        """Visita el programa completo"""
        self.emitir("# === INICIO DEL PROGRAMA ===")
        result = self.visitChildren(ctx)
        self.emitir("# === FIN DEL PROGRAMA ===")
        return result
    
    def visitBloque(self, ctx):
        """Visita un bloque de instrucciones"""
        return self.visitChildren(ctx)
    
    def visitInstrucciones(self, ctx):
        """Visita una lista de instrucciones"""
        return self.visitChildren(ctx)
    
    def visitInstruccion(self, ctx):
        """Visita una instrucción individual"""
        return self.visitChildren(ctx)
