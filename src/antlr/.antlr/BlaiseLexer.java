// Generated from /home/abdu/git/group1/src/antlr/BlaiseLexer.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BlaiseLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		WHITESPACE=1, BEGIN=2, END=3, CALL=4, PROCEDURE=5, WHILE=6, DO=7, VAR=8, 
		IF=9, THEN=10, ELSE=11, LPAREN=12, RPAREN=13, COMMA=14, SEMICOLON=15, 
		DOT=16, MULT=17, DIV=18, PLUS=19, MINUS=20, NE=21, EQ=22, LT=23, GT=24, 
		LTE=25, GTE=26, ASSIGN=27, NUMBER=28, ID=29, ERR_CHAR=30;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"WHITESPACE", "BEGIN", "END", "CALL", "PROCEDURE", "WHILE", "DO", "VAR", 
			"IF", "THEN", "ELSE", "LPAREN", "RPAREN", "COMMA", "SEMICOLON", "DOT", 
			"MULT", "DIV", "PLUS", "MINUS", "NE", "EQ", "LT", "GT", "LTE", "GTE", 
			"ASSIGN", "LETTERS", "NUMBER", "ID", "ERR_CHAR"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'BEGIN'", "'END'", "'CALL'", "'PROCEDURE'", "'WHILE'", "'DO'", 
			"'VAR'", "'IF'", "'THEN'", "'ELSE'", "'('", "')'", "','", "';'", "'.'", 
			"'*'", "'/'", "'+'", "'-'", "'<>'", "'='", "'<'", "'>'", "'<='", "'>='", 
			"':='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "WHITESPACE", "BEGIN", "END", "CALL", "PROCEDURE", "WHILE", "DO", 
			"VAR", "IF", "THEN", "ELSE", "LPAREN", "RPAREN", "COMMA", "SEMICOLON", 
			"DOT", "MULT", "DIV", "PLUS", "MINUS", "NE", "EQ", "LT", "GT", "LTE", 
			"GTE", "ASSIGN", "NUMBER", "ID", "ERR_CHAR"
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


	public BlaiseLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "BlaiseLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2 \u00c6\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \3\2"+
		"\6\2C\n\2\r\2\16\2D\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3"+
		"\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7"+
		"\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3"+
		"\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21"+
		"\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\27\3\27"+
		"\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35"+
		"\5\35\u00a1\n\35\3\36\3\36\6\36\u00a5\n\36\r\36\16\36\u00a6\3\36\7\36"+
		"\u00aa\n\36\f\36\16\36\u00ad\13\36\5\36\u00af\n\36\3\37\6\37\u00b2\n\37"+
		"\r\37\16\37\u00b3\3\37\6\37\u00b7\n\37\r\37\16\37\u00b8\3\37\6\37\u00bc"+
		"\n\37\r\37\16\37\u00bd\7\37\u00c0\n\37\f\37\16\37\u00c3\13\37\3 \3 \2"+
		"\2!\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35"+
		"\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\2"+
		";\36=\37? \3\2\4\5\2\13\f\17\17\"\"\4\2C\\c|\2\u00cd\2\3\3\2\2\2\2\5\3"+
		"\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2"+
		"\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3"+
		"\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'"+
		"\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63"+
		"\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\3"+
		"B\3\2\2\2\5H\3\2\2\2\7N\3\2\2\2\tR\3\2\2\2\13W\3\2\2\2\ra\3\2\2\2\17g"+
		"\3\2\2\2\21j\3\2\2\2\23n\3\2\2\2\25q\3\2\2\2\27v\3\2\2\2\31{\3\2\2\2\33"+
		"}\3\2\2\2\35\177\3\2\2\2\37\u0081\3\2\2\2!\u0083\3\2\2\2#\u0085\3\2\2"+
		"\2%\u0087\3\2\2\2\'\u0089\3\2\2\2)\u008b\3\2\2\2+\u008d\3\2\2\2-\u0090"+
		"\3\2\2\2/\u0092\3\2\2\2\61\u0094\3\2\2\2\63\u0096\3\2\2\2\65\u0099\3\2"+
		"\2\2\67\u009c\3\2\2\29\u00a0\3\2\2\2;\u00ae\3\2\2\2=\u00b1\3\2\2\2?\u00c4"+
		"\3\2\2\2AC\t\2\2\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2EF\3\2\2\2F"+
		"G\b\2\2\2G\4\3\2\2\2HI\7D\2\2IJ\7G\2\2JK\7I\2\2KL\7K\2\2LM\7P\2\2M\6\3"+
		"\2\2\2NO\7G\2\2OP\7P\2\2PQ\7F\2\2Q\b\3\2\2\2RS\7E\2\2ST\7C\2\2TU\7N\2"+
		"\2UV\7N\2\2V\n\3\2\2\2WX\7R\2\2XY\7T\2\2YZ\7Q\2\2Z[\7E\2\2[\\\7G\2\2\\"+
		"]\7F\2\2]^\7W\2\2^_\7T\2\2_`\7G\2\2`\f\3\2\2\2ab\7Y\2\2bc\7J\2\2cd\7K"+
		"\2\2de\7N\2\2ef\7G\2\2f\16\3\2\2\2gh\7F\2\2hi\7Q\2\2i\20\3\2\2\2jk\7X"+
		"\2\2kl\7C\2\2lm\7T\2\2m\22\3\2\2\2no\7K\2\2op\7H\2\2p\24\3\2\2\2qr\7V"+
		"\2\2rs\7J\2\2st\7G\2\2tu\7P\2\2u\26\3\2\2\2vw\7G\2\2wx\7N\2\2xy\7U\2\2"+
		"yz\7G\2\2z\30\3\2\2\2{|\7*\2\2|\32\3\2\2\2}~\7+\2\2~\34\3\2\2\2\177\u0080"+
		"\7.\2\2\u0080\36\3\2\2\2\u0081\u0082\7=\2\2\u0082 \3\2\2\2\u0083\u0084"+
		"\7\60\2\2\u0084\"\3\2\2\2\u0085\u0086\7,\2\2\u0086$\3\2\2\2\u0087\u0088"+
		"\7\61\2\2\u0088&\3\2\2\2\u0089\u008a\7-\2\2\u008a(\3\2\2\2\u008b\u008c"+
		"\7/\2\2\u008c*\3\2\2\2\u008d\u008e\7>\2\2\u008e\u008f\7@\2\2\u008f,\3"+
		"\2\2\2\u0090\u0091\7?\2\2\u0091.\3\2\2\2\u0092\u0093\7>\2\2\u0093\60\3"+
		"\2\2\2\u0094\u0095\7@\2\2\u0095\62\3\2\2\2\u0096\u0097\7>\2\2\u0097\u0098"+
		"\7?\2\2\u0098\64\3\2\2\2\u0099\u009a\7@\2\2\u009a\u009b\7?\2\2\u009b\66"+
		"\3\2\2\2\u009c\u009d\7<\2\2\u009d\u009e\7?\2\2\u009e8\3\2\2\2\u009f\u00a1"+
		"\t\3\2\2\u00a0\u009f\3\2\2\2\u00a1:\3\2\2\2\u00a2\u00af\7\62\2\2\u00a3"+
		"\u00a5\4\63;\2\u00a4\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a4\3\2"+
		"\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00ab\3\2\2\2\u00a8\u00aa\4\62;\2\u00a9"+
		"\u00a8\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3\2"+
		"\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00a2\3\2\2\2\u00ae"+
		"\u00a4\3\2\2\2\u00af<\3\2\2\2\u00b0\u00b2\59\35\2\u00b1\u00b0\3\2\2\2"+
		"\u00b2\u00b3\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00c1"+
		"\3\2\2\2\u00b5\u00b7\59\35\2\u00b6\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8"+
		"\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00c0\3\2\2\2\u00ba\u00bc\5;"+
		"\36\2\u00bb\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd"+
		"\u00be\3\2\2\2\u00be\u00c0\3\2\2\2\u00bf\u00b6\3\2\2\2\u00bf\u00bb\3\2"+
		"\2\2\u00c0\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2"+
		">\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c5\13\2\2\2\u00c5@\3\2\2\2\r\2"+
		"D\u00a0\u00a6\u00ab\u00ae\u00b3\u00b8\u00bd\u00bf\u00c1\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}