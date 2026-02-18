"""
Generador de Código Intermedio
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
                """
                Visita un nodo 'opal' (operación algebraica/lógica) y retorna la
                representación (literal, identificador o temporal) del resultado.

                Contract:
                - Input: ctx (OpalContext) que contiene una producción 'relacion'.
                - Output: string con el nombre del lugar donde está el resultado
                    (por ejemplo '5', 'x' o 't0').
                - Efectos: delega totalmente en visitRelacion; puede provocar que se
                    emitan instrucciones TAC cuando las subexpresiones lo requieran.
                """
                return self.visit(ctx.relacion())

    def visitRelacion(self, ctx):
        """
        Maneja relaciones: relacion = exp l
        Donde l puede ser: < exp l | > exp l | ... | vacio
        
        Primero evalúa la expresión aritmética, luego aplica
        operadores de comparación si existen.
        """
        result = self.visit(ctx.exp())
        
        if ctx.l():
            result = self.visit_l(ctx.l(), result)
        
        return result
    
    def visitExp(self, ctx):
        """
        Maneja expresiones: exp = term e
        Donde e puede ser: + term e | - term e | vacio
        """
        # Obtener el primer term (lado izquierdo inicial).
        # Puede devolver un número literal, un identificador o un temporal
        # si la subexpresión ya generó código.
        result = self.visit(ctx.term())

        # Si hay 'e' (continuación de sumas/restas), la procesamos pasando
        # el resultado acumulado como 'left_operand'. Esto construye
        # secuencialmente las operaciones left-to-right y emite TAC
        # intermedio en cada paso.
        if ctx.e():
            result = self.visit_e(ctx.e(), result)

        # 'result' es la representación final del valor de la expresión.
        return result
    
    def visit_e(self, ctx, left_operand):
        """
        Procesa la continuación de expresión (e)
        e : SUMA term e | RESTA term e | vacío
        """
        # Caso base: si no hay hijos es la producción vacía (epsilon). En
        # ese caso devolvemos el operando acumulado tal cual.
        if ctx.getChildCount() == 0:
            return left_operand
        
        # Obtener el operador (+ o -) y evaluar el operando derecho.
        op = ctx.getChild(0).getText()
        right = self.visit(ctx.term())

        # Crear un temporal para almacenar el resultado de la operación
        # izquierda op derecha. Emitimos la instrucción TAC correspondiente.
        result = self.nuevo_temporal()
        self.emitir(f"{result} = {left_operand} {op} {right}")

        # Si hay más operaciones encadenadas, seguir acumulando de forma
        # recursiva usando el temporal recién creado como nuevo left_operand.
        if ctx.e():
            return self.visit_e(ctx.e(), result)

        return result
    
    def visitTerm(self, ctx):
        """
        Maneja términos: term = factor t
        t: operaciones multiplicativas (*, /, %)
        
        Las comparaciones se manejan ahora en visitRelacion/visit_l.
        """
        # Evaluar el primer factor (puede ser número, variable o subexpresión
        # parentizada) y luego aplicar multiplicaciones/divisiones (t).
        result = self.visit(ctx.factor())

        if ctx.t():
            result = self.visit_t(ctx.t(), result)

        return result
    
    def visit_t(self, ctx, left_operand):
        """
        Procesa operaciones multiplicativas (t)
        t : MULT factor t | DIV factor t | MOD factor t | vacío
        """
        # Caso base: t vacío -> devolvemos el operando izquierdo tal cual.
        if ctx.getChildCount() == 0:
            return left_operand

        # Multiplicación/división/mod: obtener operador y evaluar el factor
        op = ctx.getChild(0).getText()
        right = self.visit(ctx.factor())

        # Generar temporal para el resultado y emitir la instrucción TAC
        result = self.nuevo_temporal()
        self.emitir(f"{result} = {left_operand} {op} {right}")

        # Si hay más operaciones de t encadenadas, procesarlas recursivamente
        if ctx.t():
            return self.visit_t(ctx.t(), result)

        return result
    
    def visit_l(self, ctx, left_operand):
        """
        Procesa operaciones comparativas (l)
        l : MENOR exp l | MAYOR exp l | ... | vacío
        
        Ahora opera sobre expresiones completas (exp) en lugar de factores,
        permitiendo comparaciones como (a + b) < (c + d).
        """
        # Caso base: producción vacía (epsilon)
        if ctx.getChildCount() == 0:
            return left_operand

        # Comparadores: tomar operador y evaluar la expresión derecha
        op = ctx.getChild(0).getText()
        right = self.visit(ctx.exp())

        # Crear temporal para el resultado de la comparación
        result = self.nuevo_temporal()
        self.emitir(f"{result} = {left_operand} {op} {right}")

        # Recursión si hay más comparadores encadenados
        if ctx.l():
            return self.visit_l(ctx.l(), result)

        return result
    
    def visitFactor(self, ctx):
        """
        Maneja factores: números, variables, expresiones entre paréntesis, llamadas a función
        factor : (exp) | NUMERO | ID | ID(argumentos?)
        """
        # Si es un número (hoja): devolvemos el token tal cual.
        if ctx.NUMERO():
            return ctx.NUMERO().getText()
        
        # Si es un identificador
        elif ctx.ID():
            # Si tiene paréntesis, es una llamada a función; debemos evaluar
            # sus argumentos (si existen) y emitir instrucciones 'param'
            # antes de la llamada. El resultado de la llamada se guarda en
            # un temporal.
            if ctx.PA():
                func_name = ctx.ID().getText()

                if ctx.argumentos():
                    args = self.visit(ctx.argumentos())
                    for i, arg in enumerate(args):
                        # Pasamos cada argumento como 'param <valor>'
                        self.emitir(f"param {arg}")

                result = self.nuevo_temporal()
                self.emitir(f"{result} = call {func_name}")
                return result
            else:
                # Identificador simple: devolvemos su nombre para usarlo en
                # instrucciones posteriores.
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
                # Cada 'child' corresponde a una subexpresión; la visitamos
                # para obtener la representación (literal/identificador/temporal)
                args.append(self.visit(child))
        return args
    
    # ========== VISITADORES PARA SENTENCIAS ==========
    
    def visitAsignacion(self, ctx):
        """
        Genera código para asignación: ID = opal;
        Soporta: =, +=, -=, *=, /=, %=, i++, i--, ++i, --i
        """
        primer_hijo = ctx.getChild(0).getText()
        
        if primer_hijo in ('++', '--'):
            # Prefijo: (INCREMENTO | DECREMENTO) ID PYC  →  ++x; o --x;
            variable = ctx.ID().getText()
            op = '+' if primer_hijo == '++' else '-'
            temp = self.nuevo_temporal()
            self.emitir(f"{temp} = {variable} {op} 1")
            self.emitir(f"{variable} = {temp}")
        elif ctx.INCREMENTO():
            # Postfijo: ID INCREMENTO PYC  →  x++;
            variable = ctx.ID().getText()
            temp = self.nuevo_temporal()
            self.emitir(f"{temp} = {variable} + 1")
            self.emitir(f"{variable} = {temp}")
        elif ctx.DECREMENTO():
            # Postfijo: ID DECREMENTO PYC  →  x--;
            variable = ctx.ID().getText()
            temp = self.nuevo_temporal()
            self.emitir(f"{temp} = {variable} - 1")
            self.emitir(f"{variable} = {temp}")
        else:
            # Asignación normal: ID (ASIG | MASIG | ...) opal PYC
            variable = ctx.ID().getText()

            # Operador de asignación (puede ser '=', '+=', '-='...)
            op_asig = ctx.getChild(1).getText()

            # Evaluar el lado derecho y obtener su representación
            valor = self.visit(ctx.opal())

            if op_asig == '=':
                # Asignación simple: emitimos 'variable = valor'
                self.emitir(f"{variable} = {valor}")
            else:
                # Asignación compuesta: descomponemos 'x += y' en 't = x + y' y
                # luego 'x = t' para mantener un TAC de 3 direcciones.
                op = op_asig[0]
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

        # Si la declaración incluye inicialización 'int x = expr;', emitimos
        # la asignación correspondiente. Si no, registramos la variable con
        # 'DECLARE' para dejar constancia en el código intermedio.
        if ctx.inic() and ctx.inic().ASIG():
            valor = self.visit(ctx.inic().opal())
            self.emitir(f"{variable} = {valor}")
        else:
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
        Genera código para for: for (forInit; cond; incr) bloque
        
        Gramática actualizada:
            ifor : FOR PA forInit PYC opal PYC asignacionFor PC bloque ;
            forInit : tipo ID inic listaVarFor | listaAsignacionFor ;
        
        Ahora soporta declaraciones en la inicialización:
            for (int i = 0; i < 5; i++)
        
        Código TAC generado:
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
        
        # Inicialización (puede ser declaración o lista de asignaciones)
        if ctx.forInit():
            self.visit(ctx.forInit())
        
        # Etiqueta de inicio del loop
        self.emitir(f"{label_inicio}:")
        self.indentacion += 1
        
        # Condición
        if ctx.opal():
            condicion = self.visit(ctx.opal())
            self.emitir(f"if not {condicion} goto {label_fin}")
        
        # Bloque de código
        self.visit(ctx.bloque())
        
        # Incremento (usa asignacionFor, la versión sin PYC)
        if ctx.asignacionFor():
            self.visit(ctx.asignacionFor())
        
        # Salto al inicio
        self.emitir(f"goto {label_inicio}")
        
        self.indentacion -= 1
        self.emitir(f"{label_fin}:")
        
        return None
    
    def visitForInit(self, ctx):
        """
        Procesa la inicialización del for.
        
        Gramática:
            forInit : tipo ID inic listaVarFor | listaAsignacionFor ;
        
        Si es una declaración (tipo ID inic listaVarFor), genera DECLARE y/o
        asignación. Si es lista de asignaciones, delega a visitListaAsignacionFor.
        """
        # Si tiene tipo, es una declaración (alternativa 1)
        if ctx.tipo():
            variable = ctx.ID().getText()
            if ctx.inic() and ctx.inic().ASIG():
                valor = self.visit(ctx.inic().opal())
                self.emitir(f"{variable} = {valor}")
            else:
                self.emitir(f"DECLARE {variable}")
            
            # Procesar variables adicionales
            if ctx.listaVarFor():
                self.visit(ctx.listaVarFor())
        else:
            # Es una lista de asignaciones (alternativa 2)
            if ctx.listaAsignacionFor():
                self.visit(ctx.listaAsignacionFor())
        
        return None
    
    def visitListaVarFor(self, ctx):
        """
        Procesa variables adicionales en la declaración del forInit.
        
        Gramática:
            listaVarFor : COMA ID inic listaVarFor | ;
        """
        if ctx.getChildCount() == 0:
            return None
        
        variable = ctx.ID().getText()
        if ctx.inic() and ctx.inic().ASIG():
            valor = self.visit(ctx.inic().opal())
            self.emitir(f"{variable} = {valor}")
        else:
            self.emitir(f"DECLARE {variable}")
        
        if ctx.listaVarFor():
            self.visit(ctx.listaVarFor())
        
        return None
    
    def visitListaAsignacionFor(self, ctx):
        """
        Procesa la lista de asignaciones de inicialización del for.
        
        Gramática:
            listaAsignacionFor : asignacionFor (COMA asignacionFor)* ;
        
        Visita cada asignacionFor en la lista y genera TAC para cada una.
        """
        for child in ctx.asignacionFor():
            self.visit(child)
        return None
    
    def visitAsignacionFor(self, ctx):
        """
        Procesa la parte de incremento del for (sin punto y coma).
        
        Gramática:
            asignacionFor : ID (ASIG | MASIG | ...) opal
                          | ID (INCREMENTO | DECREMENTO)
                          | (INCREMENTO | DECREMENTO) ID
                          ;
        
        Genera TAC para:
        - Asignación simple:   x = <valor>
        - Asignación compuesta: t = x + <valor>; x = t
        - Postfijo i++ / i--:  t = x + 1; x = t
        - Prefijo ++i / --i:   t = x + 1; x = t
        """
        # Determinar si es prefijo (++x) o postfijo/asignación (x++ o x = ...)
        primer_hijo = ctx.getChild(0).getText()
        
        if primer_hijo in ('++', '--'):
            # Prefijo: (INCREMENTO | DECREMENTO) ID
            variable = ctx.ID().getText()
            op = '+' if primer_hijo == '++' else '-'
            temp = self.nuevo_temporal()
            self.emitir(f"{temp} = {variable} {op} 1")
            self.emitir(f"{variable} = {temp}")
        elif ctx.INCREMENTO():
            # Postfijo: ID INCREMENTO (i++)
            variable = ctx.ID().getText()
            temp = self.nuevo_temporal()
            self.emitir(f"{temp} = {variable} + 1")
            self.emitir(f"{variable} = {temp}")
        elif ctx.DECREMENTO():
            # Postfijo: ID DECREMENTO (i--)
            variable = ctx.ID().getText()
            temp = self.nuevo_temporal()
            self.emitir(f"{temp} = {variable} - 1")
            self.emitir(f"{variable} = {temp}")
        else:
            # Es una asignación normal (x = expr, x += expr, etc.)
            variable = ctx.ID().getText()
            op_asig = ctx.getChild(1).getText()
            valor = self.visit(ctx.opal())
            
            if op_asig == '=':
                self.emitir(f"{variable} = {valor}")
            else:
                # Asignación compuesta: descomponer x += y en t = x + y; x = t
                op = op_asig[0]
                result = self.nuevo_temporal()
                self.emitir(f"{result} = {variable} {op} {valor}")
                self.emitir(f"{variable} = {result}")
        
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
    
    def visitRetorno(self, ctx):
        """
        Genera código para return: return opal ;
        
        Código TAC generado:
            return <valor>
        """
        valor = self.visit(ctx.opal())
        self.emitir(f"return {valor}")
        return None
    
    def visitFuncion(self, ctx):
        """
        Genera código para definición de función: tipo ID ( parametros ) bloque
        
        Los parámetros se sacan de la pila de parámetros (pop) al entrar
        a la función, simulando cómo un procesador real manejaría el
        paso de parámetros.
        
        Código TAC generado:
            FUNC <nombre>:
                pop <param1>
                pop <param2>
                ...
                <cuerpo>
            END FUNC <nombre>
        """
        nombre = ctx.ID().getText()
        self.emitir(f"FUNC {nombre}:")
        self.indentacion += 1
        
        # Extraer parámetros y generar instrucciones 'pop' para cada uno
        # Esto simula sacar los valores de la pila de parámetros
        parametros = ctx.parametros()
        if parametros and parametros.getChildCount() > 0:
            # Primer parámetro: tipo ID
            if parametros.ID():
                self.emitir(f"pop {parametros.ID().getText()}")
            
            # Parámetros adicionales: lista_param → COMA tipo ID lista_param
            lista = parametros.lista_param()
            while lista and lista.getChildCount() > 0:
                if lista.ID():
                    self.emitir(f"pop {lista.ID().getText()}")
                lista = lista.lista_param()
        
        self.visit(ctx.bloque())
        self.indentacion -= 1
        self.emitir(f"END FUNC {nombre}")
        return None
    
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