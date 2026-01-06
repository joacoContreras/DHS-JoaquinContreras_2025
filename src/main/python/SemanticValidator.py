"""
Validador semántico para el compilador.
Contiene la lógica de validación de tipos, inicialización, uso de variables, etc.
"""

from tablaDeSimbolos import Variable, Funcion

class SemanticValidator:
    """Clase para realizar validaciones semánticas"""
    
    def __init__(self, error_manager):
        """
        Inicializa el validador semántico
        
        Args:
            error_manager: Instancia de ErrorManager para reportar errores
        """
        self.error_manager = error_manager
    
    def validar_variable_declarada(self, nombre, linea, tabla_simbolos):
        """
        Valida que una variable esté declarada
        
        Args:
            nombre: Nombre de la variable
            linea: Línea donde se usa
            tabla_simbolos: Instancia de TS
            
        Returns:
            Símbolo si existe, None si no
        """
        simbolo = tabla_simbolos.buscarSimbolo(nombre)
        
        if simbolo is None:
            self.error_manager.reportar_error_semantico(
                linea,
                f"Variable '{nombre}' no ha sido declarada"
            )
            return None
        
        return simbolo
    
    def validar_variable_inicializada(self, simbolo, nombre, linea):
        """
        Valida que una variable esté inicializada antes de usarse
        
        Args:
            simbolo: Símbolo de la variable
            nombre: Nombre de la variable
            linea: Línea donde se usa
            
        Returns:
            True si está inicializada, False si no
        """
        if not simbolo.getInicializado():
            self.error_manager.reportar_error_semantico(
                linea,
                f"Variable '{nombre}' usada sin inicializar"
            )
            return False
        
        return True
    
    def validar_tipo_compatible(self, tipo_esperado, tipo_real, linea, contexto=""):
        """
        Valida que dos tipos sean compatibles
        
        Args:
            tipo_esperado: Tipo esperado
            tipo_real: Tipo real del valor
            linea: Línea donde ocurre
            contexto: Descripción adicional del contexto
            
        Returns:
            True si son compatibles, False si no
        """
        if tipo_real is None or tipo_esperado is None:
            return True  # No podemos validar si no conocemos los tipos
        
        if tipo_esperado == tipo_real:
            return True
        
        # Permitir int -> double (promoción automática)
        if tipo_esperado == "double" and tipo_real == "int":
            return True
        
        # Tipos incompatibles
        mensaje = f"Tipo incompatible: se intenta asignar '{tipo_real}' a variable de tipo '{tipo_esperado}'"
        if contexto:
            mensaje = f"{contexto}: {mensaje}"
        
        self.error_manager.reportar_error_semantico(linea, mensaje)
        return False
    
    def validar_doble_declaracion(self, nombre, linea, tabla_simbolos):
        """
        Valida que no haya doble declaración en el mismo contexto
        
        Args:
            nombre: Nombre de la variable
            linea: Línea de la declaración
            tabla_simbolos: Instancia de TS
            
        Returns:
            True si no hay doble declaración, False si la hay
        """
        # Buscar solo en el contexto actual (no en padres)
        contexto_actual = tabla_simbolos.contextos[-1] if tabla_simbolos.contextos else None
        
        if contexto_actual and nombre in contexto_actual.simbolos:
            self.error_manager.reportar_error_semantico(
                linea,
                f"Variable '{nombre}' ya fue declarada en este contexto"
            )
            return False
        
        return True
    
    def validar_variables_no_usadas(self, tabla_simbolos):
        """
        Valida que todas las variables declaradas hayan sido usadas
        
        Args:
            tabla_simbolos: Instancia de TS
        """
        for contexto in tabla_simbolos.contextos:
            for nombre, simbolo in contexto.simbolos.items():
                if isinstance(simbolo, Variable) and not simbolo.getUsado():
                    self.error_manager.reportar_error_semantico(
                        simbolo.getLinea(),
                        f"Variable '{nombre}' declarada pero no usada"
                    )
    
    def inferir_tipo(self, ctx, tabla_simbolos):
        """
        Intenta inferir el tipo de una expresión con validación de operaciones
        
        Args:
            ctx: Contexto de ANTLR de la expresión
            tabla_simbolos: Instancia de TS
            
        Returns:
            String con el tipo inferido o None si no se puede inferir
        """
        if ctx is None:
            return None
        
        # Obtener el nombre de la regla
        tipo_regla = type(ctx).__name__
        
        # ===== FACTOR: base de las expresiones =====
        if 'FactorContext' in tipo_regla:
            return self._inferir_tipo_factor(ctx, tabla_simbolos)
        
        # ===== TERM: multiplicación, división, módulo, comparaciones =====
        if 'TermContext' in tipo_regla:
            return self._inferir_tipo_term(ctx, tabla_simbolos)
        
        # ===== EXP: suma, resta =====
        if 'ExpContext' in tipo_regla:
            return self._inferir_tipo_exp(ctx, tabla_simbolos)
        
        # ===== OPAL: operación algebraica/lógica =====
        if 'OpalContext' in tipo_regla:
            if ctx.getChildCount() > 0:
                return self.inferir_tipo(ctx.getChild(0), tabla_simbolos)
        
        # Para otros contextos, método genérico
        texto = ctx.getText()
        
        # Si contiene punto decimal, es double
        if '.' in texto and any(c.isdigit() for c in texto):
            return "double"
        
        # Si es solo dígitos, es int
        if texto.isdigit():
            return "int"
        
        # Si es un identificador simple, buscar su tipo
        if texto.isidentifier():
            simbolo = tabla_simbolos.buscarSimbolo(texto)
            if simbolo:
                return simbolo.getTipoDato()
        
        # Si tiene hijos, revisar recursivamente
        if hasattr(ctx, 'getChildCount') and ctx.getChildCount() > 0:
            for i in range(ctx.getChildCount()):
                tipo = self.inferir_tipo(ctx.getChild(i), tabla_simbolos)
                if tipo:
                    return tipo
        
        return None
    
    def _inferir_tipo_factor(self, ctx, tabla_simbolos):
        """Infiere tipo de un factor"""
        from compiladorParser import compiladorParser
        
        if ctx.getChildCount() == 0:
            return None
        
        # factor : PA exp PC | NUMERO | ID | ID PA argumentos? PC
        primer_hijo = ctx.getChild(0)
        texto = primer_hijo.getText()
        
        # Paréntesis: ( exp )
        if texto == '(':
            if ctx.getChildCount() >= 2:
                return self.inferir_tipo(ctx.getChild(1), tabla_simbolos)
        
        # Número con punto decimal = double
        if '.' in texto and any(c.isdigit() for c in texto):
            return "double"
        
        # Número entero = int
        if texto.isdigit():
            return "int"
        
        # Identificador (variable o llamada a función)
        if texto.isidentifier():
            simbolo = tabla_simbolos.buscarSimbolo(texto)
            if simbolo:
                return simbolo.getTipoDato()
        
        return None
    
    def _inferir_tipo_term(self, ctx, tabla_simbolos):
        """Infiere tipo de un term con validación de operaciones"""
        if ctx.getChildCount() < 2:
            # Solo factor
            return self.inferir_tipo(ctx.getChild(0), tabla_simbolos)
        
        # term : factor t | factor l
        tipo_izq = self.inferir_tipo(ctx.getChild(0), tabla_simbolos)
        
        # Ver si hay operación (t o l)
        if ctx.getChildCount() >= 2:
            operacion_ctx = ctx.getChild(1)
            if operacion_ctx and operacion_ctx.getChildCount() > 0:
                return self._procesar_operacion(tipo_izq, operacion_ctx, tabla_simbolos, ctx.start.line)
        
        return tipo_izq
    
    def _inferir_tipo_exp(self, ctx, tabla_simbolos):
        """Infiere tipo de una expresión con validación de operaciones"""
        if ctx.getChildCount() < 2:
            # Solo term
            return self.inferir_tipo(ctx.getChild(0), tabla_simbolos)
        
        # exp : term e
        tipo_izq = self.inferir_tipo(ctx.getChild(0), tabla_simbolos)
        
        # Ver si hay continuación 'e'
        if ctx.getChildCount() >= 2:
            e_ctx = ctx.getChild(1)
            if e_ctx and e_ctx.getChildCount() > 0:
                return self._procesar_operacion_e(tipo_izq, e_ctx, tabla_simbolos, ctx.start.line)
        
        return tipo_izq
    
    def _procesar_operacion(self, tipo_izq, operacion_ctx, tabla_simbolos, linea):
        """Procesa operaciones en 't' y 'l' (*, /, %, <, >, ==, etc.)"""
        if not operacion_ctx or operacion_ctx.getChildCount() < 2:
            return tipo_izq
        
        # t : MULT factor t | DIV factor t | MOD factor t
        # l : MENOR factor l | MAYOR factor l | ...
        operador = operacion_ctx.getChild(0).getText()
        tipo_der = self.inferir_tipo(operacion_ctx.getChild(1), tabla_simbolos)
        
        # Validar compatibilidad de tipos
        tipo_resultado = self._validar_operacion_binaria(tipo_izq, tipo_der, operador, linea)
        
        # Si hay más operaciones, procesar recursivamente
        if operacion_ctx.getChildCount() >= 3:
            siguiente_ctx = operacion_ctx.getChild(2)
            if siguiente_ctx and siguiente_ctx.getChildCount() > 0:
                return self._procesar_operacion(tipo_resultado, siguiente_ctx, tabla_simbolos, linea)
        
        return tipo_resultado
    
    def _procesar_operacion_e(self, tipo_izq, e_ctx, tabla_simbolos, linea):
        """Procesa operaciones en 'e' (+, -)"""
        if not e_ctx or e_ctx.getChildCount() < 2:
            return tipo_izq
        
        # e : SUMA term e | RESTA term e
        operador = e_ctx.getChild(0).getText()
        tipo_der = self.inferir_tipo(e_ctx.getChild(1), tabla_simbolos)
        
        # Validar compatibilidad
        tipo_resultado = self._validar_operacion_binaria(tipo_izq, tipo_der, operador, linea)
        
        # Si hay más operaciones, procesar recursivamente
        if e_ctx.getChildCount() >= 3:
            siguiente_ctx = e_ctx.getChild(2)
            if siguiente_ctx and siguiente_ctx.getChildCount() > 0:
                return self._procesar_operacion_e(tipo_resultado, siguiente_ctx, tabla_simbolos, linea)
        
        return tipo_resultado
    
    def _validar_operacion_binaria(self, tipo_izq, tipo_der, operador, linea):
        """
        Valida una operación binaria y retorna el tipo resultante
        
        Reglas:
        - int op int = int (para aritméticas) o int (para comparaciones siempre int/bool)
        - double op double = double (para aritméticas)
        - int op double = double (promoción)
        - double op int = double (promoción)
        - Comparaciones siempre retornan int (simulando bool)
        - Módulo (%) solo acepta int op int
        """
        if tipo_izq is None or tipo_der is None:
            return None  # No podemos validar
        
        # Operadores de comparación retornan int (simulando bool)
        operadores_comparacion = ['<', '>', '<=', '>=', '==', '!=']
        if operador in operadores_comparacion:
            # Validar que los tipos sean compatibles
            if tipo_izq != tipo_der:
                if not ((tipo_izq == "int" and tipo_der == "double") or 
                       (tipo_izq == "double" and tipo_der == "int")):
                    self.error_manager.reportar_error_semantico(
                        linea,
                        f"Tipos incompatibles en comparación: '{tipo_izq}' {operador} '{tipo_der}'"
                    )
            return "int"  # Las comparaciones retornan booleano (representado como int)
        
        # Módulo solo acepta enteros
        if operador == '%':
            if tipo_izq != "int" or tipo_der != "int":
                self.error_manager.reportar_error_semantico(
                    linea,
                    f"El operador módulo (%) requiere operandos enteros, se encontró: '{tipo_izq}' % '{tipo_der}'"
                )
                return "int"
            return "int"
        
        # Operaciones aritméticas (+, -, *, /)
        # Regla: si alguno es double, el resultado es double
        if tipo_izq == "double" or tipo_der == "double":
            if tipo_izq != "double" and tipo_izq != "int":
                self.error_manager.reportar_error_semantico(
                    linea,
                    f"Tipo incompatible en operación: '{tipo_izq}' {operador} '{tipo_der}'"
                )
            if tipo_der != "double" and tipo_der != "int":
                self.error_manager.reportar_error_semantico(
                    linea,
                    f"Tipo incompatible en operación: '{tipo_izq}' {operador} '{tipo_der}'"
                )
            return "double"
        
        # Si ambos son int, el resultado es int
        if tipo_izq == "int" and tipo_der == "int":
            return "int"
        
        # Tipos incompatibles
        self.error_manager.reportar_error_semantico(
            linea,
            f"Tipos incompatibles en operación: '{tipo_izq}' {operador} '{tipo_der}'"
        )
        return tipo_izq  # Retornar algo para continuar
    
    def validar_asignacion(self, id_nombre, valor_ctx, linea, tabla_simbolos):
        """
        Valida una asignación completa
        
        Args:
            id_nombre: Nombre de la variable
            valor_ctx: Contexto del valor asignado
            linea: Línea de la asignación
            tabla_simbolos: Instancia de TS
            
        Returns:
            True si la asignación es válida, False si no
        """
        # Buscar el símbolo
        simbolo = tabla_simbolos.buscarSimbolo(id_nombre)
        
        if simbolo is None:
            self.error_manager.reportar_error_semantico(
                linea,
                f"Variable '{id_nombre}' no ha sido declarada"
            )
            return False
        
        # Marcar como inicializada
        simbolo.setInicializado(linea)
        
        # Verificar tipos
        tipo_valor = self.inferir_tipo(valor_ctx, tabla_simbolos)
        if tipo_valor:
            self.validar_tipo_compatible(
                simbolo.getTipoDato(),
                tipo_valor,
                linea,
                f"Asignación a '{id_nombre}'"
            )
        
        return True
    
    def validar_uso_variable(self, nombre, linea, tabla_simbolos):
        """
        Valida el uso de una variable en una expresión
        
        Args:
            nombre: Nombre de la variable
            linea: Línea donde se usa
            tabla_simbolos: Instancia de TS
            
        Returns:
            True si el uso es válido, False si no
        """
        simbolo = self.validar_variable_declarada(nombre, linea, tabla_simbolos)
        
        if simbolo is None:
            return False
        
        if not self.validar_variable_inicializada(simbolo, nombre, linea):
            return False
        
        # Marcar como usada
        simbolo.setUsado()
        return True
