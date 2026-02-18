"""
Gestor de errores sintácticos y semánticos.
Maneja la recolección, reporte y visualización de errores encontrados durante el análisis.
"""

class ErrorManager:
    """Clase singleton para gestionar errores de compilación"""
    
    _instance = None
    
    def __init__(self):
        """Inicializa las listas de errores y advertencias"""
        self.errores_sintacticos = []
        self.errores_semanticos = []
        self.advertencias = []
    
    @classmethod
    def getInstance(cls):
        """Obtiene la instancia única del ErrorManager"""
        if cls._instance is None:
            cls._instance = ErrorManager()
        return cls._instance
    
    @classmethod
    def reset(cls):
        """Reinicia el ErrorManager (para nuevos análisis)"""
        cls._instance = ErrorManager()
        return cls._instance
    
    def reiniciar(self):
        """Limpia todas las listas de errores y advertencias"""
        self.errores_sintacticos = []
        self.errores_semanticos = []
        self.advertencias = []
    
    def reportar_error_sintactico(self, linea, mensaje):
        """
        Reporta un error sintáctico
        
        Args:
            linea: Número de línea donde ocurre el error
            mensaje: Descripción del error
        """
        error = f"[SINTÁCTICO] Línea {linea}: {mensaje}"
        self.errores_sintacticos.append(error)
        print(f"{error}")
    
    def reportar_error_semantico(self, linea, mensaje):
        """
        Reporta un error semántico
        
        Args:
            linea: Número de línea donde ocurre el error
            mensaje: Descripción del error
        """
        error = f"[SEMÁNTICO] Línea {linea}: {mensaje}"
        self.errores_semanticos.append(error)
        print(f"{error}")
    
    def reportar_advertencia(self, linea, mensaje):
        """
        Reporta una advertencia (no bloquea la generación de TAC)
        
        Args:
            linea: Número de línea donde ocurre la advertencia
            mensaje: Descripción de la advertencia
        """
        adv = f"[ADVERTENCIA] Línea {linea}: {mensaje}"
        self.advertencias.append(adv)
        print(f"{adv}")
    
    def tiene_errores(self):
        """Retorna True si hay algún error registrado"""
        return len(self.errores_sintacticos) > 0 or len(self.errores_semanticos) > 0
    
    def obtener_total_errores(self):
        """Retorna el número total de errores"""
        return len(self.errores_sintacticos) + len(self.errores_semanticos)
    
    def obtener_errores_sintacticos(self):
        """Retorna la lista de errores sintácticos"""
        return self.errores_sintacticos.copy()
    
    def obtener_errores_semanticos(self):
        """Retorna la lista de errores semánticos"""
        return self.errores_semanticos.copy()
    
    def generar_reporte(self, tabla_simbolos=None):
        """
        Genera un reporte completo de errores
        
        Args:
            tabla_simbolos: Instancia de TS para mostrar si no hay errores
        """
        total_errores = self.obtener_total_errores()
        
        if total_errores == 0:
            # No hay errores, mostrar tabla de símbolos si se proporciona
            if tabla_simbolos:
                print(tabla_simbolos)
            else:
                print("\nAnálisis completado sin errores")
            
            # Mostrar advertencias si las hay
            if self.advertencias:
                print("\nADVERTENCIAS:")
                print("-" * 60)
                for adv in self.advertencias:
                    print(f"  {adv}")
            return
        
        # Hay errores, mostrar reporte detallado
        self._imprimir_reporte_detallado()
    
    def _imprimir_reporte_detallado(self):
        print("\n" + "=" * 60)
        print("         REPORTE DE ERRORES")
        print("=" * 60)
        print(f"Total de errores: {self.obtener_total_errores()}")
        print(f"  • Errores sintácticos: {len(self.errores_sintacticos)}")
        print(f"  • Errores semánticos: {len(self.errores_semanticos)}")
        if self.advertencias:
            print(f"  • Advertencias: {len(self.advertencias)}")
        print("=" * 60)
        
        if self.errores_sintacticos:
            print("\nERRORES SINTÁCTICOS:")
            print("-" * 60)
            for error in self.errores_sintacticos:
                print(f"  {error}")
        
        if self.errores_semanticos:
            print("\nERRORES SEMÁNTICOS:")
            print("-" * 60)
            for error in self.errores_semanticos:
                print(f"  {error}")
        
        if self.advertencias:
            print("\nADVERTENCIAS:")
            print("-" * 60)
            for adv in self.advertencias:
                print(f"  {adv}")
        
        print("\n" + "=" * 60)
    
    def __str__(self):
        """Representación en string del estado de errores"""
        return f"ErrorManager(sintácticos={len(self.errores_sintacticos)}, semánticos={len(self.errores_semanticos)})"
