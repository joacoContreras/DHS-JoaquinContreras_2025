"""
Gestor de operaciones sobre la Tabla de Símbolos.
Proporciona una capa de abstracción para operaciones comunes sobre la TS.
"""

from tablaDeSimbolos import TS, Variable, Funcion

class SymbolTableManager:
    """Gestor de operaciones sobre la tabla de símbolos"""
    
    def __init__(self, tabla_simbolos=None):
        """
        Inicializa el gestor
        
        Args:
            tabla_simbolos: Instancia de TS (si es None, usa el singleton)
        """
        self.ts = tabla_simbolos if tabla_simbolos else TS.getInstance()
    
    def agregar_contexto(self):
        """Agrega un nuevo contexto (scope) a la tabla"""
        self.ts.addContexto()
    
    def eliminar_contexto(self):
        """Elimina el contexto actual"""
        self.ts.delContexto()
    
    def agregar_variable(self, nombre, tipo, linea, inicializado=False):
        """
        Agrega una variable a la tabla de símbolos
        
        Args:
            nombre: Nombre de la variable
            tipo: Tipo de dato
            linea: Línea de declaración
            inicializado: Si está inicializada
            
        Returns:
            True si se agregó, False si ya existe
        """
        var = Variable(nombre, tipo)
        var.setLinea(linea)
        
        if inicializado:
            var.setInicializado(linea)
        
        exito = self.ts.addSimbolo(var)
        
        if exito:
            print(f"  -> Variable '{nombre}' de tipo '{tipo}' agregada")
        
        return exito
    
    def agregar_funcion(self, nombre, tipo_retorno, parametros, linea=0):
        """
        Agrega una función a la tabla de símbolos
        
        Args:
            nombre: Nombre de la función
            tipo_retorno: Tipo de retorno
            parametros: Lista de parámetros
            linea: Línea de declaración
            
        Returns:
            True si se agregó, False si ya existe
        """
        funcion = Funcion(nombre, tipo_retorno, parametros)
        funcion.setLinea(linea)
        
        exito = self.ts.addSimbolo(funcion)
        
        if exito:
            print(f"  -> Función '{nombre}()' de tipo '{tipo_retorno}' agregada")
        
        return exito
    
    def buscar_simbolo(self, nombre):
        """
        Busca un símbolo en la tabla (incluyendo contextos padre)
        
        Args:
            nombre: Nombre del símbolo
            
        Returns:
            Símbolo si existe, None si no
        """
        return self.ts.buscarSimbolo(nombre)
    
    def buscar_en_contexto_actual(self, nombre):
        """
        Busca un símbolo solo en el contexto actual (no en padres)
        
        Args:
            nombre: Nombre del símbolo
            
        Returns:
            Símbolo si existe, None si no
        """
        if not self.ts.contextos:
            return None
        
        contexto_actual = self.ts.contextos[-1]
        return contexto_actual.simbolos.get(nombre, None)
    
    def marcar_como_usado(self, nombre):
        """
        Marca una variable como usada
        
        Args:
            nombre: Nombre de la variable
            
        Returns:
            True si se marcó, False si no existe
        """
        simbolo = self.buscar_simbolo(nombre)
        if simbolo:
            simbolo.setUsado()
            return True
        return False
    
    def marcar_como_inicializado(self, nombre, linea):
        """
        Marca una variable como inicializada
        
        Args:
            nombre: Nombre de la variable
            linea: Línea donde se inicializa
            
        Returns:
            True si se marcó, False si no existe
        """
        simbolo = self.buscar_simbolo(nombre)
        if simbolo:
            simbolo.setInicializado(linea)
            return True
        return False
    
    def obtener_tabla_simbolos(self):
        """Retorna la instancia de la tabla de símbolos"""
        return self.ts
    
    def obtener_todas_variables(self):
        """
        Obtiene todas las variables de todos los contextos
        
        Returns:
            Lista de tuplas (nombre, simbolo, contexto_nivel)
        """
        variables = []
        for nivel, contexto in enumerate(self.ts.contextos):
            for nombre, simbolo in contexto.simbolos.items():
                if isinstance(simbolo, Variable):
                    variables.append((nombre, simbolo, nivel))
        return variables
    
    def obtener_todas_funciones(self):
        """
        Obtiene todas las funciones de todos los contextos
        
        Returns:
            Lista de tuplas (nombre, simbolo, contexto_nivel)
        """
        funciones = []
        for nivel, contexto in enumerate(self.ts.contextos):
            for nombre, simbolo in contexto.simbolos.items():
                if isinstance(simbolo, Funcion):
                    funciones.append((nombre, simbolo, nivel))
        return funciones
    
    def __str__(self):
        """Representación en string del gestor"""
        num_contextos = len(self.ts.contextos)
        total_simbolos = sum(len(ctx.simbolos) for ctx in self.ts.contextos)
        return f"SymbolTableManager(contextos={num_contextos}, símbolos={total_simbolos})"
