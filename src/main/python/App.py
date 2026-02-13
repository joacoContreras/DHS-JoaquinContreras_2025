import sys
try:
    from antlr4 import FileStream, CommonTokenStream
    from antlr4.error.ErrorListener import ErrorListener
except ImportError:
    print('Missing dependency: antlr4 runtime is not installed.')
    print('Install it with: python3 -m pip install antlr4-python3-runtime')
    print('Or create/activate the project virtualenv and install the package there.')
    sys.exit(1)
from compiladorLexer import compiladorLexer
from compiladorParser import compiladorParser
from Escucha import Escucha
from Caminante import Caminante
from IntermediateCodeGenerator import IntermediateCodeGenerator

class CustomErrorListener(ErrorListener):
    """Listener personalizado para capturar errores sintácticos de ANTLR"""
    def __init__(self, error_manager):
        super().__init__()
        self.error_manager = error_manager
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Simplificar el mensaje de error
        mensaje_simple = msg
        if "mismatched input" in msg:
            mensaje_simple = "Token inesperado o falta de un símbolo esperado"
        elif "missing" in msg:
            if "';'" in msg:
                mensaje_simple = "Falta un punto y coma (;)"
            elif "'('" in msg:
                mensaje_simple = "Falta un paréntesis de apertura '('"
            elif "')'" in msg:
                mensaje_simple = "Falta un paréntesis de cierre ')'"
            else:
                mensaje_simple = f"Falta: {msg.split('missing')[1].strip()}"
        elif "extraneous input" in msg:
            mensaje_simple = "Símbolo adicional no esperado"
        elif "no viable alternative" in msg:
            mensaje_simple = "Sintaxis incorrecta"
        
        self.error_manager.reportar_error_sintactico(line, mensaje_simple)

def main(argv):
    archivo = "input/for_correcto.txt"
    if len(argv) > 1 :
        archivo = argv[1]
    
    
    input = FileStream(archivo, encoding='utf-8')
    lexer = compiladorLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladorParser(stream)
    
    # Crear el listener (escucha)
    escucha = Escucha()
    
    # Remover los listeners por defecto y agregar el personalizado
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener(escucha.error_manager))
    
    # Parsear el programa
    tree = parser.programa()
    
    # RECORRER EL ÁRBOL con el listener 
    from antlr4.tree.Tree import ParseTreeWalker
    walker = ParseTreeWalker()
    walker.walk(escucha, tree)
    
    print("\n" + "="*60)
    print(escucha)
    print("="*60)
    
    # Solo mostrar el árbol si NO hay errores
    if not escucha.error_manager.tiene_errores():
        print("\nÁRBOL SINTÁCTICO:")
        print(tree.toStringTree(recog=parser))
        
        # Recorrer el árbol con el caminante
        caminante = Caminante()
        caminante.visit(tree)
        caminante.primerNumeroHojas()
        
        # GENERAR CÓDIGO INTERMEDIO
        print("\n" + "="*60)
        print("CÓDIGO INTERMEDIO (Three Address Code)")
        print("="*60)
        generador = IntermediateCodeGenerator()
        generador.visit(tree)
        print(generador.obtener_codigo())
        print("="*60)

if __name__ == '__main__':
    main(sys.argv)