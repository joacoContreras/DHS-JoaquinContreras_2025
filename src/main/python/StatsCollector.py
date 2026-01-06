"""
Recolector de estadísticas del código analizado.
Mantiene contadores de las diferentes estructuras del programa.
"""

class StatsCollector:
    """Recolector de estadísticas del código"""
    
    def __init__(self):
        """Inicializa todos los contadores"""
        self.num_declaraciones = 0
        self.num_funciones = 0
        self.num_whiles = 0
        self.num_fors = 0
        self.num_ifs = 0
        self.num_nodos = 0
        self.num_asignaciones = 0
        self.num_expresiones = 0
    
    def incrementar_declaraciones(self):
        """Incrementa el contador de declaraciones"""
        self.num_declaraciones += 1
    
    def incrementar_funciones(self):
        """Incrementa el contador de funciones"""
        self.num_funciones += 1
    
    def incrementar_whiles(self):
        """Incrementa el contador de bucles while"""
        self.num_whiles += 1
    
    def incrementar_fors(self):
        """Incrementa el contador de bucles for"""
        self.num_fors += 1
    
    def incrementar_ifs(self):
        """Incrementa el contador de estructuras if"""
        self.num_ifs += 1
    
    def incrementar_nodos(self):
        """Incrementa el contador de nodos visitados"""
        self.num_nodos += 1
    
    def incrementar_asignaciones(self):
        """Incrementa el contador de asignaciones"""
        self.num_asignaciones += 1
    
    def incrementar_expresiones(self):
        """Incrementa el contador de expresiones"""
        self.num_expresiones += 1
    
    def obtener_total_estructuras_control(self):
        """Retorna el total de estructuras de control"""
        return self.num_whiles + self.num_fors + self.num_ifs
    
    def obtener_total_bucles(self):
        """Retorna el total de bucles"""
        return self.num_whiles + self.num_fors
    
    def reiniciar(self):
        """Reinicia todos los contadores a cero"""
        self.__init__()
    
    def generar_reporte(self):
        """Genera un reporte textual de las estadísticas"""
        print("\n" + "=" * 60)
        print("         ESTADÍSTICAS DEL CÓDIGO")
        print("=" * 60)
        print(f"  Declaraciones:          {self.num_declaraciones}")
        print(f"  Funciones:              {self.num_funciones}")
        print(f"  Estructuras if:         {self.num_ifs}")
        print(f"  Bucles while:           {self.num_whiles}")
        print(f"  Bucles for:             {self.num_fors}")
        print(f"  Asignaciones:           {self.num_asignaciones}")
        print(f"  Nodos visitados:        {self.num_nodos}")
        print("=" * 60)
        print(f"  Total estructuras control: {self.obtener_total_estructuras_control()}")
        print(f"  Total bucles:             {self.obtener_total_bucles()}")
        print("=" * 60)
    
    def obtener_resumen(self):
        """
        Obtiene un resumen de las estadísticas como diccionario
        
        Returns:
            Diccionario con todas las estadísticas
        """
        return {
            'declaraciones': self.num_declaraciones,
            'funciones': self.num_funciones,
            'whiles': self.num_whiles,
            'fors': self.num_fors,
            'ifs': self.num_ifs,
            'asignaciones': self.num_asignaciones,
            'expresiones': self.num_expresiones,
            'nodos': self.num_nodos,
            'total_estructuras_control': self.obtener_total_estructuras_control(),
            'total_bucles': self.obtener_total_bucles()
        }
    
    def __str__(self):
        """Representación en string de las estadísticas"""
        resultado = f"Se hicieron {self.num_declaraciones} declaraciones\n"
        resultado += f"Se reconocieron {self.num_funciones} funciones\n"
        resultado += f"Se reconocieron {self.num_whiles} bucles while\n"
        resultado += f"Se reconocieron {self.num_fors} bucles for\n"
        resultado += f"Se reconocieron {self.num_ifs} estructuras if\n"
        resultado += f"Se visitaron {self.num_nodos} nodos"
        return resultado
