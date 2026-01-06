from antlr4 import TerminalNode
from compiladorParser import compiladorParser
from compiladorListener import compiladorListener
from tablaDeSimbolos import TS, Variable, Funcion

# Importar los módulos modulares
from ErrorManager import ErrorManager
from SemanticValidator import SemanticValidator
from SymbolTableManager import SymbolTableManager
from StatsCollector import StatsCollector

class Escucha(compiladorListener):
    """
    Listener modular para el compilador.
    Coordina entre los diferentes módulos especializados.
    """
    
    indent = 1
    profundidad = 0
    tipo_actual = None
    
    def __init__(self):
        """Inicializa el listener y sus componentes modulares"""
        super().__init__()
        # Componentes modulares
        self.error_manager = ErrorManager.getInstance()
        self.validator = SemanticValidator(self.error_manager)
        self.symbol_manager = SymbolTableManager()
        self.stats = StatsCollector()

    def enterPrograma(self, ctx: compiladorParser.ProgramaContext):
        """Inicio del análisis"""
        print("Comienza el parsing")
        self.error_manager.reiniciar()

    def exitPrograma(self, ctx: compiladorParser.ProgramaContext):
        """Finalización del análisis"""
        print("Fin del Parsing")
        
        # Validaciones finales
        self.validator.validar_variables_no_usadas(self.symbol_manager.obtener_tabla_simbolos())
        
        # Generar reportes
        self.error_manager.generar_reporte(self.symbol_manager.obtener_tabla_simbolos())
        
        # Mostrar estadísticas si no hay errores
        if not self.error_manager.tiene_errores():
            print("\n" + str(self.stats))
        
    def enterIwhile(self, ctx:compiladorParser.IwhileContext):
        """Entrada a un bucle while"""
        self.stats.incrementar_whiles()
        print("  "*self.indent + " WHILE ENTER")
        self.indent += 1
        self.symbol_manager.agregar_contexto()

    def exitIwhile(self, ctx:compiladorParser.IwhileContext):
        """Salida de un bucle while"""
        self.indent -= 1
        print("  "*self.indent + "WHILE EXIT")
        self.symbol_manager.eliminar_contexto()
        
    def enterDeclaracion(self, ctx: compiladorParser.DeclaracionContext):
        """Entrada a una declaración"""
        self.stats.incrementar_declaraciones()
        print("Declaracion ENTER -> |" + ctx.getText() + "|")
        
    def exitDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        """Salida de una declaración - procesa variables"""
        print("Declaracion EXIT  -> |" + ctx.getText() + "|")
        
        if ctx.getChildCount() >= 3:
            # Estructura: tipo ID inic listavar PYC
            linea = ctx.start.line if ctx.start else 0
            tipo = ctx.getChild(0).getText()
            print(f"  -- Tipo detectado: {tipo}")
            
            # Primera variable
            primer_id = ctx.getChild(1).getText()
            inic_ctx = ctx.getChild(2)
            inicializado = inic_ctx and inic_ctx.getChildCount() > 0
            
            # Validar doble declaración
            if not self.validator.validar_doble_declaracion(
                primer_id, linea, self.symbol_manager.obtener_tabla_simbolos()
            ):
                return
            
            # Si tiene inicialización, validar tipo del valor
            if inicializado and inic_ctx.getChildCount() >= 2:
                # inic : ASIG opal
                valor_ctx = inic_ctx.getChild(1)  # El opal
                tipo_valor = self.validator.inferir_tipo(valor_ctx, self.symbol_manager.obtener_tabla_simbolos())
                
                if tipo_valor:
                    self.validator.validar_tipo_compatible(
                        tipo, 
                        tipo_valor, 
                        linea,
                        f"Inicialización de '{primer_id}'"
                    )
            
            # Agregar variable
            self.symbol_manager.agregar_variable(primer_id, tipo, linea, inicializado)
            
            # Procesar variables adicionales en listavar
            self.tipo_actual = tipo
            self.linea_actual = linea
            self.procesar_listavar(ctx.getChild(3))
            self.tipo_actual = None
    
    def procesar_listavar(self, ctx):
        """Procesa recursivamente las variables adicionales en listavar"""
        if ctx is None or ctx.getChildCount() < 2:
            return
        
        # Estructura de listavar: COMA ID inic listavar
        if ctx.getChildCount() >= 2:
            nombre_var = ctx.getChild(1).getText()
            if nombre_var and nombre_var != ',':
                # Verificar inicialización
                inicializado = False
                if ctx.getChildCount() >= 3:
                    inic_ctx = ctx.getChild(2)
                    inicializado = inic_ctx and inic_ctx.getChildCount() > 0
                    
                    # Si tiene inicialización, validar tipo del valor
                    if inicializado and inic_ctx.getChildCount() >= 2:
                        valor_ctx = inic_ctx.getChild(1)  # El opal
                        tipo_valor = self.validator.inferir_tipo(valor_ctx, self.symbol_manager.obtener_tabla_simbolos())
                        
                        if tipo_valor:
                            self.validator.validar_tipo_compatible(
                                self.tipo_actual, 
                                tipo_valor, 
                                self.linea_actual,
                                f"Inicialización de '{nombre_var}'"
                            )
                
                # Validar doble declaración
                if not self.validator.validar_doble_declaracion(
                    nombre_var, self.linea_actual, self.symbol_manager.obtener_tabla_simbolos()
                ):
                    return
                
                # Agregar variable
                self.symbol_manager.agregar_variable(
                    nombre_var, self.tipo_actual, self.linea_actual, inicializado
                )
            
            # Procesar siguiente listavar
            if ctx.getChildCount() >= 4:
                self.procesar_listavar(ctx.getChild(3))
        
    def enterListavar(self, ctx:compiladorParser.ListavarContext):
        """Entrada a listavar"""
        self.profundidad += 1

    def exitListavar(self, ctx:compiladorParser.ListavarContext):
        """Salida de listavar"""
        self.profundidad -= 1
        if ctx.getChildCount() > 0:
            print("  -- ListaVar(%d) Cant. hijos  = %d" % (self.profundidad + 1, ctx.getChildCount()))
    
    def enterFuncion(self, ctx:compiladorParser.FuncionContext):
        """Entrada a una función"""
        self.stats.incrementar_funciones()
        print("  " * self.indent + " FUNCION ENTER")
        self.indent += 1
        self.symbol_manager.agregar_contexto()
    
    def exitFuncion(self, ctx:compiladorParser.FuncionContext):
        """Salida de una función"""
        # Estructura: tipo ID PA parametros PC bloque
        if ctx.getChildCount() >= 6:
            tipo_retorno = ctx.getChild(0).getText()
            nombre_funcion = ctx.getChild(1).getText()
            linea = ctx.start.line if ctx.start else 0
            
            # Extraer parámetros (simplificado)
            params = []
            parametros_ctx = ctx.getChild(3)
            if parametros_ctx and parametros_ctx.getChildCount() > 0:
                params.append("...")
            
            # Eliminar contexto de la función y agregar el símbolo
            self.symbol_manager.eliminar_contexto()
            self.symbol_manager.agregar_funcion(nombre_funcion, tipo_retorno, params, linea)
            
            self.indent -= 1
            print("  " * self.indent + f" FUNCION EXIT: {nombre_funcion}() -> {tipo_retorno}")
        else:
            self.indent -= 1
            print("  " * self.indent + " FUNCION EXIT (incompleta)")
    
    def enterIif(self, ctx:compiladorParser.IifContext):
        """Entrada a una estructura if"""
        self.stats.incrementar_ifs()
        print("  " * self.indent + "IF ENTER")
        self.indent += 1
        self.symbol_manager.agregar_contexto()
    
    def exitIif(self, ctx:compiladorParser.IifContext):
        """Salida de una estructura if"""
        self.indent -= 1
        self.symbol_manager.eliminar_contexto()
        print("  " * self.indent + " IF EXIT")
    
    def enterIfor(self, ctx:compiladorParser.IforContext):
        """Entrada a un bucle for"""
        self.stats.incrementar_fors()
        print("  " * self.indent + " FOR ENTER")
        self.indent += 1
        self.symbol_manager.agregar_contexto()
    
    def exitIfor(self, ctx:compiladorParser.IforContext):
        """Salida de un bucle for"""
        self.indent -= 1
        self.symbol_manager.eliminar_contexto()
        print("  " * self.indent + "FOR EXIT")
    
    # ============== DETECCIÓN DE USO DE VARIABLES ==============
    def enterAsignacion(self, ctx:compiladorParser.AsignacionContext):
        """Detecta asignaciones y valida la variable"""
        if ctx.getChildCount() >= 3:
            self.stats.incrementar_asignaciones()
            linea = ctx.start.line if ctx.start else 0
            id_nombre = ctx.getChild(0).getText()
            opal_ctx = ctx.getChild(2)  # La expresión del valor
            
            # Validar asignación usando el validador
            self.validator.validar_asignacion(
                id_nombre,
                opal_ctx,
                linea,
                self.symbol_manager.obtener_tabla_simbolos()
            )

    
    def enterFactor(self, ctx:compiladorParser.FactorContext):
        """Detecta uso de variables en expresiones"""
        # factor puede ser: PA exp PC | NUMERO | ID | ID PA argumentos? PC
        linea = ctx.start.line if ctx.start else 0
        
        # Si el primer hijo es un ID
        if ctx.getChildCount() > 0:
            primer_hijo = ctx.getChild(0).getText()
            
            # Verificar si es un identificador válido
            if primer_hijo.isidentifier() and primer_hijo not in ['int', 'double', 'if', 'while', 'for', 'return']:
                self.validator.validar_uso_variable(
                    primer_hijo,
                    linea,
                    self.symbol_manager.obtener_tabla_simbolos()
                )
                
    def enterEveryRule(self, ctx):
        """Se ejecuta al entrar a cualquier regla"""
        self.stats.incrementar_nodos()

    def __str__(self):
        """Representación en string del listener"""
        return str(self.stats)