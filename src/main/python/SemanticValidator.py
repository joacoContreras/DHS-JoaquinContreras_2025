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
        Intenta inferir el tipo de una expresión
        
        Args:
            ctx: Contexto de ANTLR de la expresión
            tabla_simbolos: Instancia de TS
            
        Returns:
            String con el tipo inferido o None si no se puede inferir
        """
        if ctx is None:
            return None
        
        texto = ctx.getText()
        
        # Si contiene punto decimal, es double
        if '.' in texto:
            return "double"
        
        # Si es solo dígitos, es int
        if texto.isdigit():
            return "int"
        
        # Si es un identificador, buscar su tipo
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
