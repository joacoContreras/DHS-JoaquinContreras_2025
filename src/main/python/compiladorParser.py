# Generated from compilador.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,319,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,3,1,72,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,85,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,3,7,111,8,7,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,129,
        8,9,1,10,1,10,1,10,1,10,1,10,1,10,3,10,137,8,10,1,11,1,11,1,11,5,
        11,142,8,11,10,11,12,11,145,9,11,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,3,12,154,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,
        14,1,14,1,14,3,14,168,8,14,1,15,1,15,1,15,3,15,173,8,15,1,16,1,16,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,188,
        8,17,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,3,21,207,8,21,1,22,1,22,1,22,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,225,
        8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        3,24,252,8,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,
        1,26,1,26,3,26,266,8,26,1,27,1,27,1,27,1,27,1,27,1,27,3,27,274,8,
        27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,286,8,
        28,1,28,3,28,289,8,28,1,29,1,29,1,29,5,29,294,8,29,10,29,12,29,297,
        9,29,1,30,1,30,1,30,1,30,3,30,303,8,30,1,30,1,30,1,30,1,31,1,31,
        1,31,1,31,1,31,1,31,5,31,314,8,31,10,31,12,31,317,9,31,1,31,0,0,
        32,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,0,3,2,0,9,9,15,19,1,0,38,39,1,0,28,
        29,326,0,64,1,0,0,0,2,71,1,0,0,0,4,84,1,0,0,0,6,86,1,0,0,0,8,90,
        1,0,0,0,10,94,1,0,0,0,12,100,1,0,0,0,14,110,1,0,0,0,16,112,1,0,0,
        0,18,128,1,0,0,0,20,136,1,0,0,0,22,138,1,0,0,0,24,153,1,0,0,0,26,
        155,1,0,0,0,28,167,1,0,0,0,30,172,1,0,0,0,32,174,1,0,0,0,34,187,
        1,0,0,0,36,189,1,0,0,0,38,191,1,0,0,0,40,194,1,0,0,0,42,206,1,0,
        0,0,44,208,1,0,0,0,46,224,1,0,0,0,48,251,1,0,0,0,50,253,1,0,0,0,
        52,265,1,0,0,0,54,273,1,0,0,0,56,288,1,0,0,0,58,290,1,0,0,0,60,298,
        1,0,0,0,62,307,1,0,0,0,64,65,3,2,1,0,65,66,5,0,0,1,66,1,1,0,0,0,
        67,68,3,4,2,0,68,69,3,2,1,0,69,72,1,0,0,0,70,72,1,0,0,0,71,67,1,
        0,0,0,71,70,1,0,0,0,72,3,1,0,0,0,73,85,3,34,17,0,74,85,3,26,13,0,
        75,85,3,12,6,0,76,85,3,10,5,0,77,85,3,16,8,0,78,85,3,50,25,0,79,
        85,3,6,3,0,80,85,3,8,4,0,81,82,3,36,18,0,82,83,5,7,0,0,83,85,1,0,
        0,0,84,73,1,0,0,0,84,74,1,0,0,0,84,75,1,0,0,0,84,76,1,0,0,0,84,77,
        1,0,0,0,84,78,1,0,0,0,84,79,1,0,0,0,84,80,1,0,0,0,84,81,1,0,0,0,
        85,5,1,0,0,0,86,87,5,34,0,0,87,88,3,36,18,0,88,89,5,7,0,0,89,7,1,
        0,0,0,90,91,5,3,0,0,91,92,3,2,1,0,92,93,5,4,0,0,93,9,1,0,0,0,94,
        95,5,33,0,0,95,96,5,1,0,0,96,97,3,36,18,0,97,98,5,2,0,0,98,99,3,
        4,2,0,99,11,1,0,0,0,100,101,5,30,0,0,101,102,5,1,0,0,102,103,3,36,
        18,0,103,104,5,2,0,0,104,105,3,4,2,0,105,106,3,14,7,0,106,13,1,0,
        0,0,107,108,5,31,0,0,108,111,3,4,2,0,109,111,1,0,0,0,110,107,1,0,
        0,0,110,109,1,0,0,0,111,15,1,0,0,0,112,113,5,32,0,0,113,114,5,1,
        0,0,114,115,3,18,9,0,115,116,5,7,0,0,116,117,3,36,18,0,117,118,5,
        7,0,0,118,119,3,24,12,0,119,120,5,2,0,0,120,121,3,8,4,0,121,17,1,
        0,0,0,122,123,3,32,16,0,123,124,5,35,0,0,124,125,3,30,15,0,125,126,
        3,20,10,0,126,129,1,0,0,0,127,129,3,22,11,0,128,122,1,0,0,0,128,
        127,1,0,0,0,129,19,1,0,0,0,130,131,5,8,0,0,131,132,5,35,0,0,132,
        133,3,30,15,0,133,134,3,20,10,0,134,137,1,0,0,0,135,137,1,0,0,0,
        136,130,1,0,0,0,136,135,1,0,0,0,137,21,1,0,0,0,138,143,3,24,12,0,
        139,140,5,8,0,0,140,142,3,24,12,0,141,139,1,0,0,0,142,145,1,0,0,
        0,143,141,1,0,0,0,143,144,1,0,0,0,144,23,1,0,0,0,145,143,1,0,0,0,
        146,147,5,35,0,0,147,148,7,0,0,0,148,154,3,36,18,0,149,150,5,35,
        0,0,150,154,7,1,0,0,151,152,7,1,0,0,152,154,5,35,0,0,153,146,1,0,
        0,0,153,149,1,0,0,0,153,151,1,0,0,0,154,25,1,0,0,0,155,156,3,32,
        16,0,156,157,5,35,0,0,157,158,3,30,15,0,158,159,3,28,14,0,159,160,
        5,7,0,0,160,27,1,0,0,0,161,162,5,8,0,0,162,163,5,35,0,0,163,164,
        3,30,15,0,164,165,3,28,14,0,165,168,1,0,0,0,166,168,1,0,0,0,167,
        161,1,0,0,0,167,166,1,0,0,0,168,29,1,0,0,0,169,170,5,9,0,0,170,173,
        3,36,18,0,171,173,1,0,0,0,172,169,1,0,0,0,172,171,1,0,0,0,173,31,
        1,0,0,0,174,175,7,2,0,0,175,33,1,0,0,0,176,177,5,35,0,0,177,178,
        7,0,0,0,178,179,3,36,18,0,179,180,5,7,0,0,180,188,1,0,0,0,181,182,
        5,35,0,0,182,183,7,1,0,0,183,188,5,7,0,0,184,185,7,1,0,0,185,186,
        5,35,0,0,186,188,5,7,0,0,187,176,1,0,0,0,187,181,1,0,0,0,187,184,
        1,0,0,0,188,35,1,0,0,0,189,190,3,38,19,0,190,37,1,0,0,0,191,192,
        3,40,20,0,192,193,3,48,24,0,193,39,1,0,0,0,194,195,3,44,22,0,195,
        196,3,42,21,0,196,41,1,0,0,0,197,198,5,10,0,0,198,199,3,44,22,0,
        199,200,3,42,21,0,200,207,1,0,0,0,201,202,5,11,0,0,202,203,3,44,
        22,0,203,204,3,42,21,0,204,207,1,0,0,0,205,207,1,0,0,0,206,197,1,
        0,0,0,206,201,1,0,0,0,206,205,1,0,0,0,207,43,1,0,0,0,208,209,3,56,
        28,0,209,210,3,46,23,0,210,45,1,0,0,0,211,212,5,12,0,0,212,213,3,
        56,28,0,213,214,3,46,23,0,214,225,1,0,0,0,215,216,5,13,0,0,216,217,
        3,56,28,0,217,218,3,46,23,0,218,225,1,0,0,0,219,220,5,14,0,0,220,
        221,3,56,28,0,221,222,3,46,23,0,222,225,1,0,0,0,223,225,1,0,0,0,
        224,211,1,0,0,0,224,215,1,0,0,0,224,219,1,0,0,0,224,223,1,0,0,0,
        225,47,1,0,0,0,226,227,5,20,0,0,227,228,3,40,20,0,228,229,3,48,24,
        0,229,252,1,0,0,0,230,231,5,21,0,0,231,232,3,40,20,0,232,233,3,48,
        24,0,233,252,1,0,0,0,234,235,5,22,0,0,235,236,3,40,20,0,236,237,
        3,48,24,0,237,252,1,0,0,0,238,239,5,23,0,0,239,240,3,40,20,0,240,
        241,3,48,24,0,241,252,1,0,0,0,242,243,5,24,0,0,243,244,3,40,20,0,
        244,245,3,48,24,0,245,252,1,0,0,0,246,247,5,25,0,0,247,248,3,40,
        20,0,248,249,3,48,24,0,249,252,1,0,0,0,250,252,1,0,0,0,251,226,1,
        0,0,0,251,230,1,0,0,0,251,234,1,0,0,0,251,238,1,0,0,0,251,242,1,
        0,0,0,251,246,1,0,0,0,251,250,1,0,0,0,252,49,1,0,0,0,253,254,3,32,
        16,0,254,255,5,35,0,0,255,256,5,1,0,0,256,257,3,52,26,0,257,258,
        5,2,0,0,258,259,3,8,4,0,259,51,1,0,0,0,260,261,3,32,16,0,261,262,
        5,35,0,0,262,263,3,54,27,0,263,266,1,0,0,0,264,266,1,0,0,0,265,260,
        1,0,0,0,265,264,1,0,0,0,266,53,1,0,0,0,267,268,5,8,0,0,268,269,3,
        32,16,0,269,270,5,35,0,0,270,271,3,54,27,0,271,274,1,0,0,0,272,274,
        1,0,0,0,273,267,1,0,0,0,273,272,1,0,0,0,274,55,1,0,0,0,275,276,5,
        1,0,0,276,277,3,40,20,0,277,278,5,2,0,0,278,289,1,0,0,0,279,289,
        5,27,0,0,280,289,5,26,0,0,281,289,5,35,0,0,282,283,5,35,0,0,283,
        285,5,1,0,0,284,286,3,58,29,0,285,284,1,0,0,0,285,286,1,0,0,0,286,
        287,1,0,0,0,287,289,5,2,0,0,288,275,1,0,0,0,288,279,1,0,0,0,288,
        280,1,0,0,0,288,281,1,0,0,0,288,282,1,0,0,0,289,57,1,0,0,0,290,295,
        3,36,18,0,291,292,5,8,0,0,292,294,3,36,18,0,293,291,1,0,0,0,294,
        297,1,0,0,0,295,293,1,0,0,0,295,296,1,0,0,0,296,59,1,0,0,0,297,295,
        1,0,0,0,298,299,3,32,16,0,299,300,5,35,0,0,300,302,5,1,0,0,301,303,
        3,62,31,0,302,301,1,0,0,0,302,303,1,0,0,0,303,304,1,0,0,0,304,305,
        5,2,0,0,305,306,5,7,0,0,306,61,1,0,0,0,307,308,3,32,16,0,308,315,
        5,35,0,0,309,310,5,8,0,0,310,311,3,32,16,0,311,312,5,35,0,0,312,
        314,1,0,0,0,313,309,1,0,0,0,314,317,1,0,0,0,315,313,1,0,0,0,315,
        316,1,0,0,0,316,63,1,0,0,0,317,315,1,0,0,0,20,71,84,110,128,136,
        143,153,167,172,187,206,224,251,265,273,285,288,295,302,315
    ]

class compiladorParser ( Parser ):

    grammarFileName = "compilador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "','", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'<'", "'>'", 
                     "'<='", "'>='", "'=='", "'!='", "<INVALID>", "<INVALID>", 
                     "'int'", "'double'", "'if'", "'else'", "'for'", "'while'", 
                     "'return'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "CA", "CC", 
                      "PYC", "COMA", "ASIG", "SUMA", "RESTA", "MULT", "DIV", 
                      "MOD", "MASIG", "RESIG", "MULASIG", "DIVASIG", "MODASIG", 
                      "MENOR", "MAYOR", "MENOREQ", "MAYOREQ", "EQUAL", "NEQUAL", 
                      "DECIMAL", "NUMERO", "INT", "DOUBLE", "IF", "ELSE", 
                      "FOR", "WHILE", "RETURN", "ID", "WS", "OTRO", "INCREMENTO", 
                      "DECREMENTO" ]

    RULE_programa = 0
    RULE_instrucciones = 1
    RULE_instruccion = 2
    RULE_retorno = 3
    RULE_bloque = 4
    RULE_iwhile = 5
    RULE_iif = 6
    RULE_ielse = 7
    RULE_ifor = 8
    RULE_forInit = 9
    RULE_listaVarFor = 10
    RULE_listaAsignacionFor = 11
    RULE_asignacionFor = 12
    RULE_declaracion = 13
    RULE_listavar = 14
    RULE_inic = 15
    RULE_tipo = 16
    RULE_asignacion = 17
    RULE_opal = 18
    RULE_relacion = 19
    RULE_exp = 20
    RULE_e = 21
    RULE_term = 22
    RULE_t = 23
    RULE_l = 24
    RULE_funcion = 25
    RULE_parametros = 26
    RULE_lista_param = 27
    RULE_factor = 28
    RULE_argumentos = 29
    RULE_prototipo = 30
    RULE_parametrosTipados = 31

    ruleNames =  [ "programa", "instrucciones", "instruccion", "retorno", 
                   "bloque", "iwhile", "iif", "ielse", "ifor", "forInit", 
                   "listaVarFor", "listaAsignacionFor", "asignacionFor", 
                   "declaracion", "listavar", "inic", "tipo", "asignacion", 
                   "opal", "relacion", "exp", "e", "term", "t", "l", "funcion", 
                   "parametros", "lista_param", "factor", "argumentos", 
                   "prototipo", "parametrosTipados" ]

    EOF = Token.EOF
    PA=1
    PC=2
    LLA=3
    LLC=4
    CA=5
    CC=6
    PYC=7
    COMA=8
    ASIG=9
    SUMA=10
    RESTA=11
    MULT=12
    DIV=13
    MOD=14
    MASIG=15
    RESIG=16
    MULASIG=17
    DIVASIG=18
    MODASIG=19
    MENOR=20
    MAYOR=21
    MENOREQ=22
    MAYOREQ=23
    EQUAL=24
    NEQUAL=25
    DECIMAL=26
    NUMERO=27
    INT=28
    DOUBLE=29
    IF=30
    ELSE=31
    FOR=32
    WHILE=33
    RETURN=34
    ID=35
    WS=36
    OTRO=37
    INCREMENTO=38
    DECREMENTO=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrucciones(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionesContext,0)


        def EOF(self):
            return self.getToken(compiladorParser.EOF, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = compiladorParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.instrucciones()
            self.state = 65
            self.match(compiladorParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def instrucciones(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionesContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = compiladorParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucciones)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 26, 27, 28, 29, 30, 32, 33, 34, 35, 38, 39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.instruccion()
                self.state = 68
                self.instrucciones()
                pass
            elif token in [-1, 4]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(compiladorParser.AsignacionContext,0)


        def declaracion(self):
            return self.getTypedRuleContext(compiladorParser.DeclaracionContext,0)


        def iif(self):
            return self.getTypedRuleContext(compiladorParser.IifContext,0)


        def iwhile(self):
            return self.getTypedRuleContext(compiladorParser.IwhileContext,0)


        def ifor(self):
            return self.getTypedRuleContext(compiladorParser.IforContext,0)


        def funcion(self):
            return self.getTypedRuleContext(compiladorParser.FuncionContext,0)


        def retorno(self):
            return self.getTypedRuleContext(compiladorParser.RetornoContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compiladorParser.BloqueContext,0)


        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = compiladorParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruccion)
        try:
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.declaracion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.iif()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.iwhile()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.ifor()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 78
                self.funcion()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 79
                self.retorno()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 80
                self.bloque()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 81
                self.opal()
                self.state = 82
                self.match(compiladorParser.PYC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(compiladorParser.RETURN, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_retorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetorno" ):
                listener.enterRetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetorno" ):
                listener.exitRetorno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetorno" ):
                return visitor.visitRetorno(self)
            else:
                return visitor.visitChildren(self)




    def retorno(self):

        localctx = compiladorParser.RetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_retorno)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(compiladorParser.RETURN)
            self.state = 87
            self.opal()
            self.state = 88
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLA(self):
            return self.getToken(compiladorParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionesContext,0)


        def LLC(self):
            return self.getToken(compiladorParser.LLC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = compiladorParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(compiladorParser.LLA)
            self.state = 91
            self.instrucciones()
            self.state = 92
            self.match(compiladorParser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IwhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(compiladorParser.WHILE, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_iwhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIwhile" ):
                listener.enterIwhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIwhile" ):
                listener.exitIwhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIwhile" ):
                return visitor.visitIwhile(self)
            else:
                return visitor.visitChildren(self)




    def iwhile(self):

        localctx = compiladorParser.IwhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(compiladorParser.WHILE)
            self.state = 95
            self.match(compiladorParser.PA)
            self.state = 96
            self.opal()
            self.state = 97
            self.match(compiladorParser.PC)
            self.state = 98
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(compiladorParser.IF, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def ielse(self):
            return self.getTypedRuleContext(compiladorParser.IelseContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_iif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIif" ):
                listener.enterIif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIif" ):
                listener.exitIif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIif" ):
                return visitor.visitIif(self)
            else:
                return visitor.visitChildren(self)




    def iif(self):

        localctx = compiladorParser.IifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_iif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(compiladorParser.IF)
            self.state = 101
            self.match(compiladorParser.PA)
            self.state = 102
            self.opal()
            self.state = 103
            self.match(compiladorParser.PC)
            self.state = 104
            self.instruccion()
            self.state = 105
            self.ielse()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IelseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(compiladorParser.ELSE, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_ielse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIelse" ):
                listener.enterIelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIelse" ):
                listener.exitIelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIelse" ):
                return visitor.visitIelse(self)
            else:
                return visitor.visitChildren(self)




    def ielse(self):

        localctx = compiladorParser.IelseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ielse)
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(compiladorParser.ELSE)
                self.state = 108
                self.instruccion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(compiladorParser.FOR, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def forInit(self):
            return self.getTypedRuleContext(compiladorParser.ForInitContext,0)


        def PYC(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.PYC)
            else:
                return self.getToken(compiladorParser.PYC, i)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def asignacionFor(self):
            return self.getTypedRuleContext(compiladorParser.AsignacionForContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladorParser.BloqueContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_ifor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfor" ):
                listener.enterIfor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfor" ):
                listener.exitIfor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfor" ):
                return visitor.visitIfor(self)
            else:
                return visitor.visitChildren(self)




    def ifor(self):

        localctx = compiladorParser.IforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(compiladorParser.FOR)
            self.state = 113
            self.match(compiladorParser.PA)
            self.state = 114
            self.forInit()
            self.state = 115
            self.match(compiladorParser.PYC)
            self.state = 116
            self.opal()
            self.state = 117
            self.match(compiladorParser.PYC)
            self.state = 118
            self.asignacionFor()
            self.state = 119
            self.match(compiladorParser.PC)
            self.state = 120
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def inic(self):
            return self.getTypedRuleContext(compiladorParser.InicContext,0)


        def listaVarFor(self):
            return self.getTypedRuleContext(compiladorParser.ListaVarForContext,0)


        def listaAsignacionFor(self):
            return self.getTypedRuleContext(compiladorParser.ListaAsignacionForContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = compiladorParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forInit)
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28, 29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.tipo()
                self.state = 123
                self.match(compiladorParser.ID)
                self.state = 124
                self.inic()
                self.state = 125
                self.listaVarFor()
                pass
            elif token in [35, 38, 39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.listaAsignacionFor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaVarForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladorParser.COMA, 0)

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def inic(self):
            return self.getTypedRuleContext(compiladorParser.InicContext,0)


        def listaVarFor(self):
            return self.getTypedRuleContext(compiladorParser.ListaVarForContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_listaVarFor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaVarFor" ):
                listener.enterListaVarFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaVarFor" ):
                listener.exitListaVarFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaVarFor" ):
                return visitor.visitListaVarFor(self)
            else:
                return visitor.visitChildren(self)




    def listaVarFor(self):

        localctx = compiladorParser.ListaVarForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_listaVarFor)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(compiladorParser.COMA)
                self.state = 131
                self.match(compiladorParser.ID)
                self.state = 132
                self.inic()
                self.state = 133
                self.listaVarFor()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaAsignacionForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacionFor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladorParser.AsignacionForContext)
            else:
                return self.getTypedRuleContext(compiladorParser.AsignacionForContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.COMA)
            else:
                return self.getToken(compiladorParser.COMA, i)

        def getRuleIndex(self):
            return compiladorParser.RULE_listaAsignacionFor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaAsignacionFor" ):
                listener.enterListaAsignacionFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaAsignacionFor" ):
                listener.exitListaAsignacionFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaAsignacionFor" ):
                return visitor.visitListaAsignacionFor(self)
            else:
                return visitor.visitChildren(self)




    def listaAsignacionFor(self):

        localctx = compiladorParser.ListaAsignacionForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_listaAsignacionFor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.asignacionFor()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 139
                self.match(compiladorParser.COMA)
                self.state = 140
                self.asignacionFor()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def ASIG(self):
            return self.getToken(compiladorParser.ASIG, 0)

        def MASIG(self):
            return self.getToken(compiladorParser.MASIG, 0)

        def RESIG(self):
            return self.getToken(compiladorParser.RESIG, 0)

        def MULASIG(self):
            return self.getToken(compiladorParser.MULASIG, 0)

        def DIVASIG(self):
            return self.getToken(compiladorParser.DIVASIG, 0)

        def MODASIG(self):
            return self.getToken(compiladorParser.MODASIG, 0)

        def INCREMENTO(self):
            return self.getToken(compiladorParser.INCREMENTO, 0)

        def DECREMENTO(self):
            return self.getToken(compiladorParser.DECREMENTO, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_asignacionFor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacionFor" ):
                listener.enterAsignacionFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacionFor" ):
                listener.exitAsignacionFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacionFor" ):
                return visitor.visitAsignacionFor(self)
            else:
                return visitor.visitChildren(self)




    def asignacionFor(self):

        localctx = compiladorParser.AsignacionForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_asignacionFor)
        self._la = 0 # Token type
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(compiladorParser.ID)
                self.state = 147
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1016320) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 148
                self.opal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(compiladorParser.ID)
                self.state = 150
                _la = self._input.LA(1)
                if not(_la==38 or _la==39):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 151
                _la = self._input.LA(1)
                if not(_la==38 or _la==39):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 152
                self.match(compiladorParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def inic(self):
            return self.getTypedRuleContext(compiladorParser.InicContext,0)


        def listavar(self):
            return self.getTypedRuleContext(compiladorParser.ListavarContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = compiladorParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.tipo()
            self.state = 156
            self.match(compiladorParser.ID)
            self.state = 157
            self.inic()
            self.state = 158
            self.listavar()
            self.state = 159
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListavarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladorParser.COMA, 0)

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def inic(self):
            return self.getTypedRuleContext(compiladorParser.InicContext,0)


        def listavar(self):
            return self.getTypedRuleContext(compiladorParser.ListavarContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_listavar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListavar" ):
                listener.enterListavar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListavar" ):
                listener.exitListavar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListavar" ):
                return visitor.visitListavar(self)
            else:
                return visitor.visitChildren(self)




    def listavar(self):

        localctx = compiladorParser.ListavarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listavar)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(compiladorParser.COMA)
                self.state = 162
                self.match(compiladorParser.ID)
                self.state = 163
                self.inic()
                self.state = 164
                self.listavar()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASIG(self):
            return self.getToken(compiladorParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_inic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInic" ):
                listener.enterInic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInic" ):
                listener.exitInic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInic" ):
                return visitor.visitInic(self)
            else:
                return visitor.visitChildren(self)




    def inic(self):

        localctx = compiladorParser.InicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_inic)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(compiladorParser.ASIG)
                self.state = 170
                self.opal()
                pass
            elif token in [7, 8]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(compiladorParser.INT, 0)

        def DOUBLE(self):
            return self.getToken(compiladorParser.DOUBLE, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = compiladorParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def ASIG(self):
            return self.getToken(compiladorParser.ASIG, 0)

        def MASIG(self):
            return self.getToken(compiladorParser.MASIG, 0)

        def RESIG(self):
            return self.getToken(compiladorParser.RESIG, 0)

        def MULASIG(self):
            return self.getToken(compiladorParser.MULASIG, 0)

        def DIVASIG(self):
            return self.getToken(compiladorParser.DIVASIG, 0)

        def MODASIG(self):
            return self.getToken(compiladorParser.MODASIG, 0)

        def INCREMENTO(self):
            return self.getToken(compiladorParser.INCREMENTO, 0)

        def DECREMENTO(self):
            return self.getToken(compiladorParser.DECREMENTO, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = compiladorParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_asignacion)
        self._la = 0 # Token type
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(compiladorParser.ID)
                self.state = 177
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1016320) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 178
                self.opal()
                self.state = 179
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(compiladorParser.ID)
                self.state = 182
                _la = self._input.LA(1)
                if not(_la==38 or _la==39):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 183
                self.match(compiladorParser.PYC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                _la = self._input.LA(1)
                if not(_la==38 or _la==39):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 185
                self.match(compiladorParser.ID)
                self.state = 186
                self.match(compiladorParser.PYC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relacion(self):
            return self.getTypedRuleContext(compiladorParser.RelacionContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_opal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpal" ):
                listener.enterOpal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpal" ):
                listener.exitOpal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpal" ):
                return visitor.visitOpal(self)
            else:
                return visitor.visitChildren(self)




    def opal(self):

        localctx = compiladorParser.OpalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_opal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.relacion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(compiladorParser.ExpContext,0)


        def l(self):
            return self.getTypedRuleContext(compiladorParser.LContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_relacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelacion" ):
                listener.enterRelacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelacion" ):
                listener.exitRelacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelacion" ):
                return visitor.visitRelacion(self)
            else:
                return visitor.visitChildren(self)




    def relacion(self):

        localctx = compiladorParser.RelacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_relacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.exp()
            self.state = 192
            self.l()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(compiladorParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compiladorParser.EContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = compiladorParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.term()
            self.state = 195
            self.e()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(compiladorParser.SUMA, 0)

        def term(self):
            return self.getTypedRuleContext(compiladorParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compiladorParser.EContext,0)


        def RESTA(self):
            return self.getToken(compiladorParser.RESTA, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_e

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE" ):
                listener.enterE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE" ):
                listener.exitE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE" ):
                return visitor.visitE(self)
            else:
                return visitor.visitChildren(self)




    def e(self):

        localctx = compiladorParser.EContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_e)
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(compiladorParser.SUMA)
                self.state = 198
                self.term()
                self.state = 199
                self.e()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.match(compiladorParser.RESTA)
                self.state = 202
                self.term()
                self.state = 203
                self.e()
                pass
            elif token in [2, 7, 8, 20, 21, 22, 23, 24, 25]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compiladorParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladorParser.TContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = compiladorParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.factor()
            self.state = 209
            self.t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(compiladorParser.MULT, 0)

        def factor(self):
            return self.getTypedRuleContext(compiladorParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladorParser.TContext,0)


        def DIV(self):
            return self.getToken(compiladorParser.DIV, 0)

        def MOD(self):
            return self.getToken(compiladorParser.MOD, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT" ):
                listener.enterT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT" ):
                listener.exitT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT" ):
                return visitor.visitT(self)
            else:
                return visitor.visitChildren(self)




    def t(self):

        localctx = compiladorParser.TContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_t)
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(compiladorParser.MULT)
                self.state = 212
                self.factor()
                self.state = 213
                self.t()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(compiladorParser.DIV)
                self.state = 216
                self.factor()
                self.state = 217
                self.t()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 219
                self.match(compiladorParser.MOD)
                self.state = 220
                self.factor()
                self.state = 221
                self.t()
                pass
            elif token in [2, 7, 8, 10, 11, 20, 21, 22, 23, 24, 25]:
                self.enterOuterAlt(localctx, 4)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MENOR(self):
            return self.getToken(compiladorParser.MENOR, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladorParser.ExpContext,0)


        def l(self):
            return self.getTypedRuleContext(compiladorParser.LContext,0)


        def MAYOR(self):
            return self.getToken(compiladorParser.MAYOR, 0)

        def MENOREQ(self):
            return self.getToken(compiladorParser.MENOREQ, 0)

        def MAYOREQ(self):
            return self.getToken(compiladorParser.MAYOREQ, 0)

        def EQUAL(self):
            return self.getToken(compiladorParser.EQUAL, 0)

        def NEQUAL(self):
            return self.getToken(compiladorParser.NEQUAL, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_l

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL" ):
                listener.enterL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL" ):
                listener.exitL(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL" ):
                return visitor.visitL(self)
            else:
                return visitor.visitChildren(self)




    def l(self):

        localctx = compiladorParser.LContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_l)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(compiladorParser.MENOR)
                self.state = 227
                self.exp()
                self.state = 228
                self.l()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.match(compiladorParser.MAYOR)
                self.state = 231
                self.exp()
                self.state = 232
                self.l()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.match(compiladorParser.MENOREQ)
                self.state = 235
                self.exp()
                self.state = 236
                self.l()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 238
                self.match(compiladorParser.MAYOREQ)
                self.state = 239
                self.exp()
                self.state = 240
                self.l()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 242
                self.match(compiladorParser.EQUAL)
                self.state = 243
                self.exp()
                self.state = 244
                self.l()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 6)
                self.state = 246
                self.match(compiladorParser.NEQUAL)
                self.state = 247
                self.exp()
                self.state = 248
                self.l()
                pass
            elif token in [2, 7, 8]:
                self.enterOuterAlt(localctx, 7)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def parametros(self):
            return self.getTypedRuleContext(compiladorParser.ParametrosContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladorParser.BloqueContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)




    def funcion(self):

        localctx = compiladorParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.tipo()
            self.state = 254
            self.match(compiladorParser.ID)
            self.state = 255
            self.match(compiladorParser.PA)
            self.state = 256
            self.parametros()
            self.state = 257
            self.match(compiladorParser.PC)
            self.state = 258
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def lista_param(self):
            return self.getTypedRuleContext(compiladorParser.Lista_paramContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = compiladorParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_parametros)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28, 29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.tipo()
                self.state = 261
                self.match(compiladorParser.ID)
                self.state = 262
                self.lista_param()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladorParser.COMA, 0)

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def lista_param(self):
            return self.getTypedRuleContext(compiladorParser.Lista_paramContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_lista_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_param" ):
                listener.enterLista_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_param" ):
                listener.exitLista_param(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_param" ):
                return visitor.visitLista_param(self)
            else:
                return visitor.visitChildren(self)




    def lista_param(self):

        localctx = compiladorParser.Lista_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_lista_param)
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(compiladorParser.COMA)
                self.state = 268
                self.tipo()
                self.state = 269
                self.match(compiladorParser.ID)
                self.state = 270
                self.lista_param()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladorParser.ExpContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def NUMERO(self):
            return self.getToken(compiladorParser.NUMERO, 0)

        def DECIMAL(self):
            return self.getToken(compiladorParser.DECIMAL, 0)

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def argumentos(self):
            return self.getTypedRuleContext(compiladorParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = compiladorParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(compiladorParser.PA)
                self.state = 276
                self.exp()
                self.state = 277
                self.match(compiladorParser.PC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.match(compiladorParser.NUMERO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 280
                self.match(compiladorParser.DECIMAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 281
                self.match(compiladorParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 282
                self.match(compiladorParser.ID)
                self.state = 283
                self.match(compiladorParser.PA)
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34561064962) != 0):
                    self.state = 284
                    self.argumentos()


                self.state = 287
                self.match(compiladorParser.PC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladorParser.OpalContext)
            else:
                return self.getTypedRuleContext(compiladorParser.OpalContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.COMA)
            else:
                return self.getToken(compiladorParser.COMA, i)

        def getRuleIndex(self):
            return compiladorParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = compiladorParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.opal()
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 291
                self.match(compiladorParser.COMA)
                self.state = 292
                self.opal()
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrototipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def parametrosTipados(self):
            return self.getTypedRuleContext(compiladorParser.ParametrosTipadosContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_prototipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrototipo" ):
                listener.enterPrototipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrototipo" ):
                listener.exitPrototipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrototipo" ):
                return visitor.visitPrototipo(self)
            else:
                return visitor.visitChildren(self)




    def prototipo(self):

        localctx = compiladorParser.PrototipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_prototipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.tipo()
            self.state = 299
            self.match(compiladorParser.ID)
            self.state = 300
            self.match(compiladorParser.PA)
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28 or _la==29:
                self.state = 301
                self.parametrosTipados()


            self.state = 304
            self.match(compiladorParser.PC)
            self.state = 305
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosTipadosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladorParser.TipoContext)
            else:
                return self.getTypedRuleContext(compiladorParser.TipoContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.ID)
            else:
                return self.getToken(compiladorParser.ID, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.COMA)
            else:
                return self.getToken(compiladorParser.COMA, i)

        def getRuleIndex(self):
            return compiladorParser.RULE_parametrosTipados

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametrosTipados" ):
                listener.enterParametrosTipados(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametrosTipados" ):
                listener.exitParametrosTipados(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametrosTipados" ):
                return visitor.visitParametrosTipados(self)
            else:
                return visitor.visitChildren(self)




    def parametrosTipados(self):

        localctx = compiladorParser.ParametrosTipadosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_parametrosTipados)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.tipo()
            self.state = 308
            self.match(compiladorParser.ID)
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 309
                self.match(compiladorParser.COMA)
                self.state = 310
                self.tipo()
                self.state = 311
                self.match(compiladorParser.ID)
                self.state = 317
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





