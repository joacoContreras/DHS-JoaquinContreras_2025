// Generated from /home/joacontreras/Documents/GitHub/DHS-JoaquinContreras_2025/src/main/python/compilador.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class compiladorParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PA=1, PC=2, LLA=3, LLC=4, CA=5, CC=6, PYC=7, COMA=8, ASIG=9, SUMA=10, 
		RESTA=11, MULT=12, DIV=13, MOD=14, MASIG=15, RESIG=16, MULASIG=17, DIVASIG=18, 
		MODASIG=19, MENOR=20, MAYOR=21, MENOREQ=22, MAYOREQ=23, EQUAL=24, NEQUAL=25, 
		NUMERO=26, INT=27, DOUBLE=28, IF=29, ELSE=30, FOR=31, WHILE=32, RETURN=33, 
		ID=34, WS=35, OTRO=36, INCREMENTO=37, DECREMENTO=38;
	public static final int
		RULE_programa = 0, RULE_instrucciones = 1, RULE_instruccion = 2, RULE_retorno = 3, 
		RULE_bloque = 4, RULE_iwhile = 5, RULE_iif = 6, RULE_ielse = 7, RULE_ifor = 8, 
		RULE_forInit = 9, RULE_listaVarFor = 10, RULE_listaAsignacionFor = 11, 
		RULE_asignacionFor = 12, RULE_declaracion = 13, RULE_listavar = 14, RULE_inic = 15, 
		RULE_tipo = 16, RULE_asignacion = 17, RULE_opal = 18, RULE_relacion = 19, 
		RULE_exp = 20, RULE_e = 21, RULE_term = 22, RULE_t = 23, RULE_l = 24, 
		RULE_funcion = 25, RULE_parametros = 26, RULE_lista_param = 27, RULE_factor = 28, 
		RULE_argumentos = 29, RULE_prototipo = 30, RULE_parametrosTipados = 31;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "instrucciones", "instruccion", "retorno", "bloque", "iwhile", 
			"iif", "ielse", "ifor", "forInit", "listaVarFor", "listaAsignacionFor", 
			"asignacionFor", "declaracion", "listavar", "inic", "tipo", "asignacion", 
			"opal", "relacion", "exp", "e", "term", "t", "l", "funcion", "parametros", 
			"lista_param", "factor", "argumentos", "prototipo", "parametrosTipados"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "'='", 
			"'+'", "'-'", "'*'", "'/'", "'%'", "'+='", "'-='", "'*='", "'/='", "'%='", 
			"'<'", "'>'", "'<='", "'>='", "'=='", "'!='", null, "'int'", "'double'", 
			"'if'", "'else'", "'for'", "'while'", "'return'", null, null, null, "'++'", 
			"'--'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PA", "PC", "LLA", "LLC", "CA", "CC", "PYC", "COMA", "ASIG", "SUMA", 
			"RESTA", "MULT", "DIV", "MOD", "MASIG", "RESIG", "MULASIG", "DIVASIG", 
			"MODASIG", "MENOR", "MAYOR", "MENOREQ", "MAYOREQ", "EQUAL", "NEQUAL", 
			"NUMERO", "INT", "DOUBLE", "IF", "ELSE", "FOR", "WHILE", "RETURN", "ID", 
			"WS", "OTRO", "INCREMENTO", "DECREMENTO"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "compilador.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public compiladorParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public TerminalNode EOF() { return getToken(compiladorParser.EOF, 0); }
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterPrograma(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitPrograma(this);
		}
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			instrucciones();
			setState(65);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InstruccionesContext extends ParserRuleContext {
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public InstruccionesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instrucciones; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterInstrucciones(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitInstrucciones(this);
		}
	}

	public final InstruccionesContext instrucciones() throws RecognitionException {
		InstruccionesContext _localctx = new InstruccionesContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_instrucciones);
		try {
			setState(71);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PA:
			case LLA:
			case NUMERO:
			case INT:
			case DOUBLE:
			case IF:
			case FOR:
			case WHILE:
			case RETURN:
			case ID:
			case INCREMENTO:
			case DECREMENTO:
				enterOuterAlt(_localctx, 1);
				{
				setState(67);
				instruccion();
				setState(68);
				instrucciones();
				}
				break;
			case EOF:
			case LLC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InstruccionContext extends ParserRuleContext {
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public DeclaracionContext declaracion() {
			return getRuleContext(DeclaracionContext.class,0);
		}
		public IifContext iif() {
			return getRuleContext(IifContext.class,0);
		}
		public IwhileContext iwhile() {
			return getRuleContext(IwhileContext.class,0);
		}
		public IforContext ifor() {
			return getRuleContext(IforContext.class,0);
		}
		public FuncionContext funcion() {
			return getRuleContext(FuncionContext.class,0);
		}
		public RetornoContext retorno() {
			return getRuleContext(RetornoContext.class,0);
		}
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public TerminalNode PYC() { return getToken(compiladorParser.PYC, 0); }
		public InstruccionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instruccion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterInstruccion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitInstruccion(this);
		}
	}

	public final InstruccionContext instruccion() throws RecognitionException {
		InstruccionContext _localctx = new InstruccionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_instruccion);
		try {
			setState(84);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(73);
				asignacion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(74);
				declaracion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(75);
				iif();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(76);
				iwhile();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(77);
				ifor();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(78);
				funcion();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(79);
				retorno();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(80);
				bloque();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(81);
				opal();
				setState(82);
				match(PYC);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RetornoContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(compiladorParser.RETURN, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public TerminalNode PYC() { return getToken(compiladorParser.PYC, 0); }
		public RetornoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_retorno; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterRetorno(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitRetorno(this);
		}
	}

	public final RetornoContext retorno() throws RecognitionException {
		RetornoContext _localctx = new RetornoContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_retorno);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(RETURN);
			setState(87);
			opal();
			setState(88);
			match(PYC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BloqueContext extends ParserRuleContext {
		public TerminalNode LLA() { return getToken(compiladorParser.LLA, 0); }
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public TerminalNode LLC() { return getToken(compiladorParser.LLC, 0); }
		public BloqueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloque; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterBloque(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitBloque(this);
		}
	}

	public final BloqueContext bloque() throws RecognitionException {
		BloqueContext _localctx = new BloqueContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_bloque);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(LLA);
			setState(91);
			instrucciones();
			setState(92);
			match(LLC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IwhileContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(compiladorParser.WHILE, 0); }
		public TerminalNode PA() { return getToken(compiladorParser.PA, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladorParser.PC, 0); }
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public IwhileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iwhile; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterIwhile(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitIwhile(this);
		}
	}

	public final IwhileContext iwhile() throws RecognitionException {
		IwhileContext _localctx = new IwhileContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_iwhile);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(WHILE);
			setState(95);
			match(PA);
			setState(96);
			opal();
			setState(97);
			match(PC);
			setState(98);
			instruccion();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IifContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(compiladorParser.IF, 0); }
		public TerminalNode PA() { return getToken(compiladorParser.PA, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladorParser.PC, 0); }
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public IelseContext ielse() {
			return getRuleContext(IelseContext.class,0);
		}
		public IifContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iif; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterIif(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitIif(this);
		}
	}

	public final IifContext iif() throws RecognitionException {
		IifContext _localctx = new IifContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_iif);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			match(IF);
			setState(101);
			match(PA);
			setState(102);
			opal();
			setState(103);
			match(PC);
			setState(104);
			instruccion();
			setState(105);
			ielse();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IelseContext extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(compiladorParser.ELSE, 0); }
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public IelseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ielse; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterIelse(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitIelse(this);
		}
	}

	public final IelseContext ielse() throws RecognitionException {
		IelseContext _localctx = new IelseContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_ielse);
		try {
			setState(110);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(107);
				match(ELSE);
				setState(108);
				instruccion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IforContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(compiladorParser.FOR, 0); }
		public TerminalNode PA() { return getToken(compiladorParser.PA, 0); }
		public ForInitContext forInit() {
			return getRuleContext(ForInitContext.class,0);
		}
		public List<TerminalNode> PYC() { return getTokens(compiladorParser.PYC); }
		public TerminalNode PYC(int i) {
			return getToken(compiladorParser.PYC, i);
		}
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public AsignacionForContext asignacionFor() {
			return getRuleContext(AsignacionForContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladorParser.PC, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public IforContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterIfor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitIfor(this);
		}
	}

	public final IforContext ifor() throws RecognitionException {
		IforContext _localctx = new IforContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_ifor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			match(FOR);
			setState(113);
			match(PA);
			setState(114);
			forInit();
			setState(115);
			match(PYC);
			setState(116);
			opal();
			setState(117);
			match(PYC);
			setState(118);
			asignacionFor();
			setState(119);
			match(PC);
			setState(120);
			bloque();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForInitContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladorParser.ID, 0); }
		public InicContext inic() {
			return getRuleContext(InicContext.class,0);
		}
		public ListaVarForContext listaVarFor() {
			return getRuleContext(ListaVarForContext.class,0);
		}
		public ListaAsignacionForContext listaAsignacionFor() {
			return getRuleContext(ListaAsignacionForContext.class,0);
		}
		public ForInitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forInit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterForInit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitForInit(this);
		}
	}

	public final ForInitContext forInit() throws RecognitionException {
		ForInitContext _localctx = new ForInitContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_forInit);
		try {
			setState(128);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case DOUBLE:
				enterOuterAlt(_localctx, 1);
				{
				setState(122);
				tipo();
				setState(123);
				match(ID);
				setState(124);
				inic();
				setState(125);
				listaVarFor();
				}
				break;
			case ID:
			case INCREMENTO:
			case DECREMENTO:
				enterOuterAlt(_localctx, 2);
				{
				setState(127);
				listaAsignacionFor();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListaVarForContext extends ParserRuleContext {
		public TerminalNode COMA() { return getToken(compiladorParser.COMA, 0); }
		public TerminalNode ID() { return getToken(compiladorParser.ID, 0); }
		public InicContext inic() {
			return getRuleContext(InicContext.class,0);
		}
		public ListaVarForContext listaVarFor() {
			return getRuleContext(ListaVarForContext.class,0);
		}
		public ListaVarForContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listaVarFor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterListaVarFor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitListaVarFor(this);
		}
	}

	public final ListaVarForContext listaVarFor() throws RecognitionException {
		ListaVarForContext _localctx = new ListaVarForContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_listaVarFor);
		try {
			setState(136);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(130);
				match(COMA);
				setState(131);
				match(ID);
				setState(132);
				inic();
				setState(133);
				listaVarFor();
				}
				break;
			case PYC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListaAsignacionForContext extends ParserRuleContext {
		public List<AsignacionForContext> asignacionFor() {
			return getRuleContexts(AsignacionForContext.class);
		}
		public AsignacionForContext asignacionFor(int i) {
			return getRuleContext(AsignacionForContext.class,i);
		}
		public List<TerminalNode> COMA() { return getTokens(compiladorParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(compiladorParser.COMA, i);
		}
		public ListaAsignacionForContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listaAsignacionFor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterListaAsignacionFor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitListaAsignacionFor(this);
		}
	}

	public final ListaAsignacionForContext listaAsignacionFor() throws RecognitionException {
		ListaAsignacionForContext _localctx = new ListaAsignacionForContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_listaAsignacionFor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(138);
			asignacionFor();
			setState(143);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMA) {
				{
				{
				setState(139);
				match(COMA);
				setState(140);
				asignacionFor();
				}
				}
				setState(145);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionForContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(compiladorParser.ID, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public TerminalNode ASIG() { return getToken(compiladorParser.ASIG, 0); }
		public TerminalNode MASIG() { return getToken(compiladorParser.MASIG, 0); }
		public TerminalNode RESIG() { return getToken(compiladorParser.RESIG, 0); }
		public TerminalNode MULASIG() { return getToken(compiladorParser.MULASIG, 0); }
		public TerminalNode DIVASIG() { return getToken(compiladorParser.DIVASIG, 0); }
		public TerminalNode MODASIG() { return getToken(compiladorParser.MODASIG, 0); }
		public TerminalNode INCREMENTO() { return getToken(compiladorParser.INCREMENTO, 0); }
		public TerminalNode DECREMENTO() { return getToken(compiladorParser.DECREMENTO, 0); }
		public AsignacionForContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacionFor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterAsignacionFor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitAsignacionFor(this);
		}
	}

	public final AsignacionForContext asignacionFor() throws RecognitionException {
		AsignacionForContext _localctx = new AsignacionForContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_asignacionFor);
		int _la;
		try {
			setState(153);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(146);
				match(ID);
				setState(147);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1016320L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(148);
				opal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(149);
				match(ID);
				setState(150);
				_la = _input.LA(1);
				if ( !(_la==INCREMENTO || _la==DECREMENTO) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(151);
				_la = _input.LA(1);
				if ( !(_la==INCREMENTO || _la==DECREMENTO) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(152);
				match(ID);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladorParser.ID, 0); }
		public InicContext inic() {
			return getRuleContext(InicContext.class,0);
		}
		public ListavarContext listavar() {
			return getRuleContext(ListavarContext.class,0);
		}
		public TerminalNode PYC() { return getToken(compiladorParser.PYC, 0); }
		public DeclaracionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterDeclaracion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitDeclaracion(this);
		}
	}

	public final DeclaracionContext declaracion() throws RecognitionException {
		DeclaracionContext _localctx = new DeclaracionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_declaracion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			tipo();
			setState(156);
			match(ID);
			setState(157);
			inic();
			setState(158);
			listavar();
			setState(159);
			match(PYC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListavarContext extends ParserRuleContext {
		public TerminalNode COMA() { return getToken(compiladorParser.COMA, 0); }
		public TerminalNode ID() { return getToken(compiladorParser.ID, 0); }
		public InicContext inic() {
			return getRuleContext(InicContext.class,0);
		}
		public ListavarContext listavar() {
			return getRuleContext(ListavarContext.class,0);
		}
		public ListavarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listavar; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterListavar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitListavar(this);
		}
	}

	public final ListavarContext listavar() throws RecognitionException {
		ListavarContext _localctx = new ListavarContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_listavar);
		try {
			setState(167);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(161);
				match(COMA);
				setState(162);
				match(ID);
				setState(163);
				inic();
				setState(164);
				listavar();
				}
				break;
			case PYC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InicContext extends ParserRuleContext {
		public TerminalNode ASIG() { return getToken(compiladorParser.ASIG, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public InicContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inic; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterInic(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitInic(this);
		}
	}

	public final InicContext inic() throws RecognitionException {
		InicContext _localctx = new InicContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_inic);
		try {
			setState(172);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ASIG:
				enterOuterAlt(_localctx, 1);
				{
				setState(169);
				match(ASIG);
				setState(170);
				opal();
				}
				break;
			case PYC:
			case COMA:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TipoContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(compiladorParser.INT, 0); }
		public TerminalNode DOUBLE() { return getToken(compiladorParser.DOUBLE, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterTipo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitTipo(this);
		}
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==DOUBLE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(compiladorParser.ID, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public TerminalNode PYC() { return getToken(compiladorParser.PYC, 0); }
		public TerminalNode ASIG() { return getToken(compiladorParser.ASIG, 0); }
		public TerminalNode MASIG() { return getToken(compiladorParser.MASIG, 0); }
		public TerminalNode RESIG() { return getToken(compiladorParser.RESIG, 0); }
		public TerminalNode MULASIG() { return getToken(compiladorParser.MULASIG, 0); }
		public TerminalNode DIVASIG() { return getToken(compiladorParser.DIVASIG, 0); }
		public TerminalNode MODASIG() { return getToken(compiladorParser.MODASIG, 0); }
		public TerminalNode INCREMENTO() { return getToken(compiladorParser.INCREMENTO, 0); }
		public TerminalNode DECREMENTO() { return getToken(compiladorParser.DECREMENTO, 0); }
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterAsignacion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitAsignacion(this);
		}
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_asignacion);
		int _la;
		try {
			setState(187);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(176);
				match(ID);
				setState(177);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1016320L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(178);
				opal();
				setState(179);
				match(PYC);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(181);
				match(ID);
				setState(182);
				_la = _input.LA(1);
				if ( !(_la==INCREMENTO || _la==DECREMENTO) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(183);
				match(PYC);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(184);
				_la = _input.LA(1);
				if ( !(_la==INCREMENTO || _la==DECREMENTO) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(185);
				match(ID);
				setState(186);
				match(PYC);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpalContext extends ParserRuleContext {
		public RelacionContext relacion() {
			return getRuleContext(RelacionContext.class,0);
		}
		public OpalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterOpal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitOpal(this);
		}
	}

	public final OpalContext opal() throws RecognitionException {
		OpalContext _localctx = new OpalContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_opal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(189);
			relacion();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RelacionContext extends ParserRuleContext {
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public LContext l() {
			return getRuleContext(LContext.class,0);
		}
		public RelacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relacion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterRelacion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitRelacion(this);
		}
	}

	public final RelacionContext relacion() throws RecognitionException {
		RelacionContext _localctx = new RelacionContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_relacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			exp();
			setState(192);
			l();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpContext extends ParserRuleContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public EContext e() {
			return getRuleContext(EContext.class,0);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterExp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitExp(this);
		}
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(194);
			term();
			setState(195);
			e();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EContext extends ParserRuleContext {
		public TerminalNode SUMA() { return getToken(compiladorParser.SUMA, 0); }
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public EContext e() {
			return getRuleContext(EContext.class,0);
		}
		public TerminalNode RESTA() { return getToken(compiladorParser.RESTA, 0); }
		public EContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_e; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterE(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitE(this);
		}
	}

	public final EContext e() throws RecognitionException {
		EContext _localctx = new EContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_e);
		try {
			setState(206);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SUMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(197);
				match(SUMA);
				setState(198);
				term();
				setState(199);
				e();
				}
				break;
			case RESTA:
				enterOuterAlt(_localctx, 2);
				{
				setState(201);
				match(RESTA);
				setState(202);
				term();
				setState(203);
				e();
				}
				break;
			case PC:
			case PYC:
			case COMA:
			case MENOR:
			case MAYOR:
			case MENOREQ:
			case MAYOREQ:
			case EQUAL:
			case NEQUAL:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TContext t() {
			return getRuleContext(TContext.class,0);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterTerm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitTerm(this);
		}
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_term);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(208);
			factor();
			setState(209);
			t();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TContext extends ParserRuleContext {
		public TerminalNode MULT() { return getToken(compiladorParser.MULT, 0); }
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TContext t() {
			return getRuleContext(TContext.class,0);
		}
		public TerminalNode DIV() { return getToken(compiladorParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(compiladorParser.MOD, 0); }
		public TContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_t; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterT(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitT(this);
		}
	}

	public final TContext t() throws RecognitionException {
		TContext _localctx = new TContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_t);
		try {
			setState(224);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MULT:
				enterOuterAlt(_localctx, 1);
				{
				setState(211);
				match(MULT);
				setState(212);
				factor();
				setState(213);
				t();
				}
				break;
			case DIV:
				enterOuterAlt(_localctx, 2);
				{
				setState(215);
				match(DIV);
				setState(216);
				factor();
				setState(217);
				t();
				}
				break;
			case MOD:
				enterOuterAlt(_localctx, 3);
				{
				setState(219);
				match(MOD);
				setState(220);
				factor();
				setState(221);
				t();
				}
				break;
			case PC:
			case PYC:
			case COMA:
			case SUMA:
			case RESTA:
			case MENOR:
			case MAYOR:
			case MENOREQ:
			case MAYOREQ:
			case EQUAL:
			case NEQUAL:
				enterOuterAlt(_localctx, 4);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LContext extends ParserRuleContext {
		public TerminalNode MENOR() { return getToken(compiladorParser.MENOR, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public LContext l() {
			return getRuleContext(LContext.class,0);
		}
		public TerminalNode MAYOR() { return getToken(compiladorParser.MAYOR, 0); }
		public TerminalNode MENOREQ() { return getToken(compiladorParser.MENOREQ, 0); }
		public TerminalNode MAYOREQ() { return getToken(compiladorParser.MAYOREQ, 0); }
		public TerminalNode EQUAL() { return getToken(compiladorParser.EQUAL, 0); }
		public TerminalNode NEQUAL() { return getToken(compiladorParser.NEQUAL, 0); }
		public LContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_l; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterL(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitL(this);
		}
	}

	public final LContext l() throws RecognitionException {
		LContext _localctx = new LContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_l);
		try {
			setState(251);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MENOR:
				enterOuterAlt(_localctx, 1);
				{
				setState(226);
				match(MENOR);
				setState(227);
				exp();
				setState(228);
				l();
				}
				break;
			case MAYOR:
				enterOuterAlt(_localctx, 2);
				{
				setState(230);
				match(MAYOR);
				setState(231);
				exp();
				setState(232);
				l();
				}
				break;
			case MENOREQ:
				enterOuterAlt(_localctx, 3);
				{
				setState(234);
				match(MENOREQ);
				setState(235);
				exp();
				setState(236);
				l();
				}
				break;
			case MAYOREQ:
				enterOuterAlt(_localctx, 4);
				{
				setState(238);
				match(MAYOREQ);
				setState(239);
				exp();
				setState(240);
				l();
				}
				break;
			case EQUAL:
				enterOuterAlt(_localctx, 5);
				{
				setState(242);
				match(EQUAL);
				setState(243);
				exp();
				setState(244);
				l();
				}
				break;
			case NEQUAL:
				enterOuterAlt(_localctx, 6);
				{
				setState(246);
				match(NEQUAL);
				setState(247);
				exp();
				setState(248);
				l();
				}
				break;
			case PC:
			case PYC:
			case COMA:
				enterOuterAlt(_localctx, 7);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncionContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladorParser.ID, 0); }
		public TerminalNode PA() { return getToken(compiladorParser.PA, 0); }
		public ParametrosContext parametros() {
			return getRuleContext(ParametrosContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladorParser.PC, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public FuncionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterFuncion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitFuncion(this);
		}
	}

	public final FuncionContext funcion() throws RecognitionException {
		FuncionContext _localctx = new FuncionContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_funcion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(253);
			tipo();
			setState(254);
			match(ID);
			setState(255);
			match(PA);
			setState(256);
			parametros();
			setState(257);
			match(PC);
			setState(258);
			bloque();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametrosContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladorParser.ID, 0); }
		public Lista_paramContext lista_param() {
			return getRuleContext(Lista_paramContext.class,0);
		}
		public ParametrosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parametros; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterParametros(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitParametros(this);
		}
	}

	public final ParametrosContext parametros() throws RecognitionException {
		ParametrosContext _localctx = new ParametrosContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_parametros);
		try {
			setState(265);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case DOUBLE:
				enterOuterAlt(_localctx, 1);
				{
				setState(260);
				tipo();
				setState(261);
				match(ID);
				setState(262);
				lista_param();
				}
				break;
			case PC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Lista_paramContext extends ParserRuleContext {
		public TerminalNode COMA() { return getToken(compiladorParser.COMA, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladorParser.ID, 0); }
		public Lista_paramContext lista_param() {
			return getRuleContext(Lista_paramContext.class,0);
		}
		public Lista_paramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_param; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterLista_param(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitLista_param(this);
		}
	}

	public final Lista_paramContext lista_param() throws RecognitionException {
		Lista_paramContext _localctx = new Lista_paramContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_lista_param);
		try {
			setState(273);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(267);
				match(COMA);
				setState(268);
				tipo();
				setState(269);
				match(ID);
				setState(270);
				lista_param();
				}
				break;
			case PC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public TerminalNode PA() { return getToken(compiladorParser.PA, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladorParser.PC, 0); }
		public TerminalNode NUMERO() { return getToken(compiladorParser.NUMERO, 0); }
		public TerminalNode ID() { return getToken(compiladorParser.ID, 0); }
		public ArgumentosContext argumentos() {
			return getRuleContext(ArgumentosContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterFactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitFactor(this);
		}
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_factor);
		int _la;
		try {
			setState(287);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(275);
				match(PA);
				setState(276);
				exp();
				setState(277);
				match(PC);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(279);
				match(NUMERO);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(280);
				match(ID);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(281);
				match(ID);
				setState(282);
				match(PA);
				setState(284);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17246978050L) != 0)) {
					{
					setState(283);
					argumentos();
					}
				}

				setState(286);
				match(PC);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentosContext extends ParserRuleContext {
		public List<OpalContext> opal() {
			return getRuleContexts(OpalContext.class);
		}
		public OpalContext opal(int i) {
			return getRuleContext(OpalContext.class,i);
		}
		public List<TerminalNode> COMA() { return getTokens(compiladorParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(compiladorParser.COMA, i);
		}
		public ArgumentosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentos; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterArgumentos(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitArgumentos(this);
		}
	}

	public final ArgumentosContext argumentos() throws RecognitionException {
		ArgumentosContext _localctx = new ArgumentosContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_argumentos);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(289);
			opal();
			setState(294);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMA) {
				{
				{
				setState(290);
				match(COMA);
				setState(291);
				opal();
				}
				}
				setState(296);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrototipoContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladorParser.ID, 0); }
		public TerminalNode PA() { return getToken(compiladorParser.PA, 0); }
		public TerminalNode PC() { return getToken(compiladorParser.PC, 0); }
		public TerminalNode PYC() { return getToken(compiladorParser.PYC, 0); }
		public ParametrosTipadosContext parametrosTipados() {
			return getRuleContext(ParametrosTipadosContext.class,0);
		}
		public PrototipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prototipo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterPrototipo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitPrototipo(this);
		}
	}

	public final PrototipoContext prototipo() throws RecognitionException {
		PrototipoContext _localctx = new PrototipoContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_prototipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(297);
			tipo();
			setState(298);
			match(ID);
			setState(299);
			match(PA);
			setState(301);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INT || _la==DOUBLE) {
				{
				setState(300);
				parametrosTipados();
				}
			}

			setState(303);
			match(PC);
			setState(304);
			match(PYC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametrosTipadosContext extends ParserRuleContext {
		public List<TipoContext> tipo() {
			return getRuleContexts(TipoContext.class);
		}
		public TipoContext tipo(int i) {
			return getRuleContext(TipoContext.class,i);
		}
		public List<TerminalNode> ID() { return getTokens(compiladorParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(compiladorParser.ID, i);
		}
		public List<TerminalNode> COMA() { return getTokens(compiladorParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(compiladorParser.COMA, i);
		}
		public ParametrosTipadosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parametrosTipados; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).enterParametrosTipados(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladorListener ) ((compiladorListener)listener).exitParametrosTipados(this);
		}
	}

	public final ParametrosTipadosContext parametrosTipados() throws RecognitionException {
		ParametrosTipadosContext _localctx = new ParametrosTipadosContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_parametrosTipados);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(306);
			tipo();
			setState(307);
			match(ID);
			setState(314);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMA) {
				{
				{
				setState(308);
				match(COMA);
				setState(309);
				tipo();
				setState(310);
				match(ID);
				}
				}
				setState(316);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001&\u013e\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001H\b\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002U\b\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0003\u0007o\b\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0003\t\u0081\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0003\n\u0089\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b\u008e"+
		"\b\u000b\n\u000b\f\u000b\u0091\t\u000b\u0001\f\u0001\f\u0001\f\u0001\f"+
		"\u0001\f\u0001\f\u0001\f\u0003\f\u009a\b\f\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0003\u000e\u00a8\b\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0003\u000f\u00ad\b\u000f\u0001\u0010\u0001\u0010\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00bc\b\u0011\u0001"+
		"\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u00cf"+
		"\b\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0003\u0017\u00e1"+
		"\b\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0003\u0018\u00fc\b\u0018\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0003\u001a\u010a\b\u001a\u0001"+
		"\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0003"+
		"\u001b\u0112\b\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0003\u001c\u011d"+
		"\b\u001c\u0001\u001c\u0003\u001c\u0120\b\u001c\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0005\u001d\u0125\b\u001d\n\u001d\f\u001d\u0128\t\u001d\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0003\u001e\u012e\b\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0001\u001f\u0005\u001f\u0139\b\u001f\n\u001f\f\u001f"+
		"\u013c\t\u001f\u0001\u001f\u0000\u0000 \u0000\u0002\u0004\u0006\b\n\f"+
		"\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:"+
		"<>\u0000\u0003\u0002\u0000\t\t\u000f\u0013\u0001\u0000%&\u0001\u0000\u001b"+
		"\u001c\u0144\u0000@\u0001\u0000\u0000\u0000\u0002G\u0001\u0000\u0000\u0000"+
		"\u0004T\u0001\u0000\u0000\u0000\u0006V\u0001\u0000\u0000\u0000\bZ\u0001"+
		"\u0000\u0000\u0000\n^\u0001\u0000\u0000\u0000\fd\u0001\u0000\u0000\u0000"+
		"\u000en\u0001\u0000\u0000\u0000\u0010p\u0001\u0000\u0000\u0000\u0012\u0080"+
		"\u0001\u0000\u0000\u0000\u0014\u0088\u0001\u0000\u0000\u0000\u0016\u008a"+
		"\u0001\u0000\u0000\u0000\u0018\u0099\u0001\u0000\u0000\u0000\u001a\u009b"+
		"\u0001\u0000\u0000\u0000\u001c\u00a7\u0001\u0000\u0000\u0000\u001e\u00ac"+
		"\u0001\u0000\u0000\u0000 \u00ae\u0001\u0000\u0000\u0000\"\u00bb\u0001"+
		"\u0000\u0000\u0000$\u00bd\u0001\u0000\u0000\u0000&\u00bf\u0001\u0000\u0000"+
		"\u0000(\u00c2\u0001\u0000\u0000\u0000*\u00ce\u0001\u0000\u0000\u0000,"+
		"\u00d0\u0001\u0000\u0000\u0000.\u00e0\u0001\u0000\u0000\u00000\u00fb\u0001"+
		"\u0000\u0000\u00002\u00fd\u0001\u0000\u0000\u00004\u0109\u0001\u0000\u0000"+
		"\u00006\u0111\u0001\u0000\u0000\u00008\u011f\u0001\u0000\u0000\u0000:"+
		"\u0121\u0001\u0000\u0000\u0000<\u0129\u0001\u0000\u0000\u0000>\u0132\u0001"+
		"\u0000\u0000\u0000@A\u0003\u0002\u0001\u0000AB\u0005\u0000\u0000\u0001"+
		"B\u0001\u0001\u0000\u0000\u0000CD\u0003\u0004\u0002\u0000DE\u0003\u0002"+
		"\u0001\u0000EH\u0001\u0000\u0000\u0000FH\u0001\u0000\u0000\u0000GC\u0001"+
		"\u0000\u0000\u0000GF\u0001\u0000\u0000\u0000H\u0003\u0001\u0000\u0000"+
		"\u0000IU\u0003\"\u0011\u0000JU\u0003\u001a\r\u0000KU\u0003\f\u0006\u0000"+
		"LU\u0003\n\u0005\u0000MU\u0003\u0010\b\u0000NU\u00032\u0019\u0000OU\u0003"+
		"\u0006\u0003\u0000PU\u0003\b\u0004\u0000QR\u0003$\u0012\u0000RS\u0005"+
		"\u0007\u0000\u0000SU\u0001\u0000\u0000\u0000TI\u0001\u0000\u0000\u0000"+
		"TJ\u0001\u0000\u0000\u0000TK\u0001\u0000\u0000\u0000TL\u0001\u0000\u0000"+
		"\u0000TM\u0001\u0000\u0000\u0000TN\u0001\u0000\u0000\u0000TO\u0001\u0000"+
		"\u0000\u0000TP\u0001\u0000\u0000\u0000TQ\u0001\u0000\u0000\u0000U\u0005"+
		"\u0001\u0000\u0000\u0000VW\u0005!\u0000\u0000WX\u0003$\u0012\u0000XY\u0005"+
		"\u0007\u0000\u0000Y\u0007\u0001\u0000\u0000\u0000Z[\u0005\u0003\u0000"+
		"\u0000[\\\u0003\u0002\u0001\u0000\\]\u0005\u0004\u0000\u0000]\t\u0001"+
		"\u0000\u0000\u0000^_\u0005 \u0000\u0000_`\u0005\u0001\u0000\u0000`a\u0003"+
		"$\u0012\u0000ab\u0005\u0002\u0000\u0000bc\u0003\u0004\u0002\u0000c\u000b"+
		"\u0001\u0000\u0000\u0000de\u0005\u001d\u0000\u0000ef\u0005\u0001\u0000"+
		"\u0000fg\u0003$\u0012\u0000gh\u0005\u0002\u0000\u0000hi\u0003\u0004\u0002"+
		"\u0000ij\u0003\u000e\u0007\u0000j\r\u0001\u0000\u0000\u0000kl\u0005\u001e"+
		"\u0000\u0000lo\u0003\u0004\u0002\u0000mo\u0001\u0000\u0000\u0000nk\u0001"+
		"\u0000\u0000\u0000nm\u0001\u0000\u0000\u0000o\u000f\u0001\u0000\u0000"+
		"\u0000pq\u0005\u001f\u0000\u0000qr\u0005\u0001\u0000\u0000rs\u0003\u0012"+
		"\t\u0000st\u0005\u0007\u0000\u0000tu\u0003$\u0012\u0000uv\u0005\u0007"+
		"\u0000\u0000vw\u0003\u0018\f\u0000wx\u0005\u0002\u0000\u0000xy\u0003\b"+
		"\u0004\u0000y\u0011\u0001\u0000\u0000\u0000z{\u0003 \u0010\u0000{|\u0005"+
		"\"\u0000\u0000|}\u0003\u001e\u000f\u0000}~\u0003\u0014\n\u0000~\u0081"+
		"\u0001\u0000\u0000\u0000\u007f\u0081\u0003\u0016\u000b\u0000\u0080z\u0001"+
		"\u0000\u0000\u0000\u0080\u007f\u0001\u0000\u0000\u0000\u0081\u0013\u0001"+
		"\u0000\u0000\u0000\u0082\u0083\u0005\b\u0000\u0000\u0083\u0084\u0005\""+
		"\u0000\u0000\u0084\u0085\u0003\u001e\u000f\u0000\u0085\u0086\u0003\u0014"+
		"\n\u0000\u0086\u0089\u0001\u0000\u0000\u0000\u0087\u0089\u0001\u0000\u0000"+
		"\u0000\u0088\u0082\u0001\u0000\u0000\u0000\u0088\u0087\u0001\u0000\u0000"+
		"\u0000\u0089\u0015\u0001\u0000\u0000\u0000\u008a\u008f\u0003\u0018\f\u0000"+
		"\u008b\u008c\u0005\b\u0000\u0000\u008c\u008e\u0003\u0018\f\u0000\u008d"+
		"\u008b\u0001\u0000\u0000\u0000\u008e\u0091\u0001\u0000\u0000\u0000\u008f"+
		"\u008d\u0001\u0000\u0000\u0000\u008f\u0090\u0001\u0000\u0000\u0000\u0090"+
		"\u0017\u0001\u0000\u0000\u0000\u0091\u008f\u0001\u0000\u0000\u0000\u0092"+
		"\u0093\u0005\"\u0000\u0000\u0093\u0094\u0007\u0000\u0000\u0000\u0094\u009a"+
		"\u0003$\u0012\u0000\u0095\u0096\u0005\"\u0000\u0000\u0096\u009a\u0007"+
		"\u0001\u0000\u0000\u0097\u0098\u0007\u0001\u0000\u0000\u0098\u009a\u0005"+
		"\"\u0000\u0000\u0099\u0092\u0001\u0000\u0000\u0000\u0099\u0095\u0001\u0000"+
		"\u0000\u0000\u0099\u0097\u0001\u0000\u0000\u0000\u009a\u0019\u0001\u0000"+
		"\u0000\u0000\u009b\u009c\u0003 \u0010\u0000\u009c\u009d\u0005\"\u0000"+
		"\u0000\u009d\u009e\u0003\u001e\u000f\u0000\u009e\u009f\u0003\u001c\u000e"+
		"\u0000\u009f\u00a0\u0005\u0007\u0000\u0000\u00a0\u001b\u0001\u0000\u0000"+
		"\u0000\u00a1\u00a2\u0005\b\u0000\u0000\u00a2\u00a3\u0005\"\u0000\u0000"+
		"\u00a3\u00a4\u0003\u001e\u000f\u0000\u00a4\u00a5\u0003\u001c\u000e\u0000"+
		"\u00a5\u00a8\u0001\u0000\u0000\u0000\u00a6\u00a8\u0001\u0000\u0000\u0000"+
		"\u00a7\u00a1\u0001\u0000\u0000\u0000\u00a7\u00a6\u0001\u0000\u0000\u0000"+
		"\u00a8\u001d\u0001\u0000\u0000\u0000\u00a9\u00aa\u0005\t\u0000\u0000\u00aa"+
		"\u00ad\u0003$\u0012\u0000\u00ab\u00ad\u0001\u0000\u0000\u0000\u00ac\u00a9"+
		"\u0001\u0000\u0000\u0000\u00ac\u00ab\u0001\u0000\u0000\u0000\u00ad\u001f"+
		"\u0001\u0000\u0000\u0000\u00ae\u00af\u0007\u0002\u0000\u0000\u00af!\u0001"+
		"\u0000\u0000\u0000\u00b0\u00b1\u0005\"\u0000\u0000\u00b1\u00b2\u0007\u0000"+
		"\u0000\u0000\u00b2\u00b3\u0003$\u0012\u0000\u00b3\u00b4\u0005\u0007\u0000"+
		"\u0000\u00b4\u00bc\u0001\u0000\u0000\u0000\u00b5\u00b6\u0005\"\u0000\u0000"+
		"\u00b6\u00b7\u0007\u0001\u0000\u0000\u00b7\u00bc\u0005\u0007\u0000\u0000"+
		"\u00b8\u00b9\u0007\u0001\u0000\u0000\u00b9\u00ba\u0005\"\u0000\u0000\u00ba"+
		"\u00bc\u0005\u0007\u0000\u0000\u00bb\u00b0\u0001\u0000\u0000\u0000\u00bb"+
		"\u00b5\u0001\u0000\u0000\u0000\u00bb\u00b8\u0001\u0000\u0000\u0000\u00bc"+
		"#\u0001\u0000\u0000\u0000\u00bd\u00be\u0003&\u0013\u0000\u00be%\u0001"+
		"\u0000\u0000\u0000\u00bf\u00c0\u0003(\u0014\u0000\u00c0\u00c1\u00030\u0018"+
		"\u0000\u00c1\'\u0001\u0000\u0000\u0000\u00c2\u00c3\u0003,\u0016\u0000"+
		"\u00c3\u00c4\u0003*\u0015\u0000\u00c4)\u0001\u0000\u0000\u0000\u00c5\u00c6"+
		"\u0005\n\u0000\u0000\u00c6\u00c7\u0003,\u0016\u0000\u00c7\u00c8\u0003"+
		"*\u0015\u0000\u00c8\u00cf\u0001\u0000\u0000\u0000\u00c9\u00ca\u0005\u000b"+
		"\u0000\u0000\u00ca\u00cb\u0003,\u0016\u0000\u00cb\u00cc\u0003*\u0015\u0000"+
		"\u00cc\u00cf\u0001\u0000\u0000\u0000\u00cd\u00cf\u0001\u0000\u0000\u0000"+
		"\u00ce\u00c5\u0001\u0000\u0000\u0000\u00ce\u00c9\u0001\u0000\u0000\u0000"+
		"\u00ce\u00cd\u0001\u0000\u0000\u0000\u00cf+\u0001\u0000\u0000\u0000\u00d0"+
		"\u00d1\u00038\u001c\u0000\u00d1\u00d2\u0003.\u0017\u0000\u00d2-\u0001"+
		"\u0000\u0000\u0000\u00d3\u00d4\u0005\f\u0000\u0000\u00d4\u00d5\u00038"+
		"\u001c\u0000\u00d5\u00d6\u0003.\u0017\u0000\u00d6\u00e1\u0001\u0000\u0000"+
		"\u0000\u00d7\u00d8\u0005\r\u0000\u0000\u00d8\u00d9\u00038\u001c\u0000"+
		"\u00d9\u00da\u0003.\u0017\u0000\u00da\u00e1\u0001\u0000\u0000\u0000\u00db"+
		"\u00dc\u0005\u000e\u0000\u0000\u00dc\u00dd\u00038\u001c\u0000\u00dd\u00de"+
		"\u0003.\u0017\u0000\u00de\u00e1\u0001\u0000\u0000\u0000\u00df\u00e1\u0001"+
		"\u0000\u0000\u0000\u00e0\u00d3\u0001\u0000\u0000\u0000\u00e0\u00d7\u0001"+
		"\u0000\u0000\u0000\u00e0\u00db\u0001\u0000\u0000\u0000\u00e0\u00df\u0001"+
		"\u0000\u0000\u0000\u00e1/\u0001\u0000\u0000\u0000\u00e2\u00e3\u0005\u0014"+
		"\u0000\u0000\u00e3\u00e4\u0003(\u0014\u0000\u00e4\u00e5\u00030\u0018\u0000"+
		"\u00e5\u00fc\u0001\u0000\u0000\u0000\u00e6\u00e7\u0005\u0015\u0000\u0000"+
		"\u00e7\u00e8\u0003(\u0014\u0000\u00e8\u00e9\u00030\u0018\u0000\u00e9\u00fc"+
		"\u0001\u0000\u0000\u0000\u00ea\u00eb\u0005\u0016\u0000\u0000\u00eb\u00ec"+
		"\u0003(\u0014\u0000\u00ec\u00ed\u00030\u0018\u0000\u00ed\u00fc\u0001\u0000"+
		"\u0000\u0000\u00ee\u00ef\u0005\u0017\u0000\u0000\u00ef\u00f0\u0003(\u0014"+
		"\u0000\u00f0\u00f1\u00030\u0018\u0000\u00f1\u00fc\u0001\u0000\u0000\u0000"+
		"\u00f2\u00f3\u0005\u0018\u0000\u0000\u00f3\u00f4\u0003(\u0014\u0000\u00f4"+
		"\u00f5\u00030\u0018\u0000\u00f5\u00fc\u0001\u0000\u0000\u0000\u00f6\u00f7"+
		"\u0005\u0019\u0000\u0000\u00f7\u00f8\u0003(\u0014\u0000\u00f8\u00f9\u0003"+
		"0\u0018\u0000\u00f9\u00fc\u0001\u0000\u0000\u0000\u00fa\u00fc\u0001\u0000"+
		"\u0000\u0000\u00fb\u00e2\u0001\u0000\u0000\u0000\u00fb\u00e6\u0001\u0000"+
		"\u0000\u0000\u00fb\u00ea\u0001\u0000\u0000\u0000\u00fb\u00ee\u0001\u0000"+
		"\u0000\u0000\u00fb\u00f2\u0001\u0000\u0000\u0000\u00fb\u00f6\u0001\u0000"+
		"\u0000\u0000\u00fb\u00fa\u0001\u0000\u0000\u0000\u00fc1\u0001\u0000\u0000"+
		"\u0000\u00fd\u00fe\u0003 \u0010\u0000\u00fe\u00ff\u0005\"\u0000\u0000"+
		"\u00ff\u0100\u0005\u0001\u0000\u0000\u0100\u0101\u00034\u001a\u0000\u0101"+
		"\u0102\u0005\u0002\u0000\u0000\u0102\u0103\u0003\b\u0004\u0000\u01033"+
		"\u0001\u0000\u0000\u0000\u0104\u0105\u0003 \u0010\u0000\u0105\u0106\u0005"+
		"\"\u0000\u0000\u0106\u0107\u00036\u001b\u0000\u0107\u010a\u0001\u0000"+
		"\u0000\u0000\u0108\u010a\u0001\u0000\u0000\u0000\u0109\u0104\u0001\u0000"+
		"\u0000\u0000\u0109\u0108\u0001\u0000\u0000\u0000\u010a5\u0001\u0000\u0000"+
		"\u0000\u010b\u010c\u0005\b\u0000\u0000\u010c\u010d\u0003 \u0010\u0000"+
		"\u010d\u010e\u0005\"\u0000\u0000\u010e\u010f\u00036\u001b\u0000\u010f"+
		"\u0112\u0001\u0000\u0000\u0000\u0110\u0112\u0001\u0000\u0000\u0000\u0111"+
		"\u010b\u0001\u0000\u0000\u0000\u0111\u0110\u0001\u0000\u0000\u0000\u0112"+
		"7\u0001\u0000\u0000\u0000\u0113\u0114\u0005\u0001\u0000\u0000\u0114\u0115"+
		"\u0003(\u0014\u0000\u0115\u0116\u0005\u0002\u0000\u0000\u0116\u0120\u0001"+
		"\u0000\u0000\u0000\u0117\u0120\u0005\u001a\u0000\u0000\u0118\u0120\u0005"+
		"\"\u0000\u0000\u0119\u011a\u0005\"\u0000\u0000\u011a\u011c\u0005\u0001"+
		"\u0000\u0000\u011b\u011d\u0003:\u001d\u0000\u011c\u011b\u0001\u0000\u0000"+
		"\u0000\u011c\u011d\u0001\u0000\u0000\u0000\u011d\u011e\u0001\u0000\u0000"+
		"\u0000\u011e\u0120\u0005\u0002\u0000\u0000\u011f\u0113\u0001\u0000\u0000"+
		"\u0000\u011f\u0117\u0001\u0000\u0000\u0000\u011f\u0118\u0001\u0000\u0000"+
		"\u0000\u011f\u0119\u0001\u0000\u0000\u0000\u01209\u0001\u0000\u0000\u0000"+
		"\u0121\u0126\u0003$\u0012\u0000\u0122\u0123\u0005\b\u0000\u0000\u0123"+
		"\u0125\u0003$\u0012\u0000\u0124\u0122\u0001\u0000\u0000\u0000\u0125\u0128"+
		"\u0001\u0000\u0000\u0000\u0126\u0124\u0001\u0000\u0000\u0000\u0126\u0127"+
		"\u0001\u0000\u0000\u0000\u0127;\u0001\u0000\u0000\u0000\u0128\u0126\u0001"+
		"\u0000\u0000\u0000\u0129\u012a\u0003 \u0010\u0000\u012a\u012b\u0005\""+
		"\u0000\u0000\u012b\u012d\u0005\u0001\u0000\u0000\u012c\u012e\u0003>\u001f"+
		"\u0000\u012d\u012c\u0001\u0000\u0000\u0000\u012d\u012e\u0001\u0000\u0000"+
		"\u0000\u012e\u012f\u0001\u0000\u0000\u0000\u012f\u0130\u0005\u0002\u0000"+
		"\u0000\u0130\u0131\u0005\u0007\u0000\u0000\u0131=\u0001\u0000\u0000\u0000"+
		"\u0132\u0133\u0003 \u0010\u0000\u0133\u013a\u0005\"\u0000\u0000\u0134"+
		"\u0135\u0005\b\u0000\u0000\u0135\u0136\u0003 \u0010\u0000\u0136\u0137"+
		"\u0005\"\u0000\u0000\u0137\u0139\u0001\u0000\u0000\u0000\u0138\u0134\u0001"+
		"\u0000\u0000\u0000\u0139\u013c\u0001\u0000\u0000\u0000\u013a\u0138\u0001"+
		"\u0000\u0000\u0000\u013a\u013b\u0001\u0000\u0000\u0000\u013b?\u0001\u0000"+
		"\u0000\u0000\u013c\u013a\u0001\u0000\u0000\u0000\u0014GTn\u0080\u0088"+
		"\u008f\u0099\u00a7\u00ac\u00bb\u00ce\u00e0\u00fb\u0109\u0111\u011c\u011f"+
		"\u0126\u012d\u013a";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}