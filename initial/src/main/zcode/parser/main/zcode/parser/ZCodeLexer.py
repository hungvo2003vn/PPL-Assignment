# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\60")
        buf.write("\u0115\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3")
        buf.write("$\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\7+\u0103\n+\f+\16+\u0106\13+\3,\6,\u0109\n,\r,\16")
        buf.write(",\u010a\3,\3,\3-\3-\3-\3.\3.\3/\3/\2\2\60\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[")
        buf.write("/]\60\3\2\5\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\13\17\17")
        buf.write("\"\"\2\u0116\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\3_\3\2\2\2\5d\3\2\2\2\7j\3\2\2\2\tq")
        buf.write("\3\2\2\2\13v\3\2\2\2\r}\3\2\2\2\17\u0084\3\2\2\2\21\u0088")
        buf.write("\3\2\2\2\23\u0090\3\2\2\2\25\u0095\3\2\2\2\27\u0099\3")
        buf.write("\2\2\2\31\u009f\3\2\2\2\33\u00a2\3\2\2\2\35\u00a8\3\2")
        buf.write("\2\2\37\u00b1\3\2\2\2!\u00b4\3\2\2\2#\u00b9\3\2\2\2%\u00be")
        buf.write("\3\2\2\2\'\u00c4\3\2\2\2)\u00c8\3\2\2\2+\u00cc\3\2\2\2")
        buf.write("-\u00d0\3\2\2\2/\u00d3\3\2\2\2\61\u00d5\3\2\2\2\63\u00d7")
        buf.write("\3\2\2\2\65\u00d9\3\2\2\2\67\u00db\3\2\2\29\u00dd\3\2")
        buf.write("\2\2;\u00df\3\2\2\2=\u00e2\3\2\2\2?\u00e5\3\2\2\2A\u00e7")
        buf.write("\3\2\2\2C\u00ea\3\2\2\2E\u00ec\3\2\2\2G\u00ef\3\2\2\2")
        buf.write("I\u00f3\3\2\2\2K\u00f6\3\2\2\2M\u00f8\3\2\2\2O\u00fa\3")
        buf.write("\2\2\2Q\u00fc\3\2\2\2S\u00fe\3\2\2\2U\u0100\3\2\2\2W\u0108")
        buf.write("\3\2\2\2Y\u010e\3\2\2\2[\u0111\3\2\2\2]\u0113\3\2\2\2")
        buf.write("_`\7v\2\2`a\7t\2\2ab\7w\2\2bc\7g\2\2c\4\3\2\2\2de\7h\2")
        buf.write("\2ef\7c\2\2fg\7n\2\2gh\7u\2\2hi\7g\2\2i\6\3\2\2\2jk\7")
        buf.write("p\2\2kl\7w\2\2lm\7o\2\2mn\7d\2\2no\7g\2\2op\7t\2\2p\b")
        buf.write("\3\2\2\2qr\7d\2\2rs\7q\2\2st\7q\2\2tu\7n\2\2u\n\3\2\2")
        buf.write("\2vw\7u\2\2wx\7v\2\2xy\7t\2\2yz\7k\2\2z{\7p\2\2{|\7i\2")
        buf.write("\2|\f\3\2\2\2}~\7t\2\2~\177\7g\2\2\177\u0080\7v\2\2\u0080")
        buf.write("\u0081\7w\2\2\u0081\u0082\7t\2\2\u0082\u0083\7p\2\2\u0083")
        buf.write("\16\3\2\2\2\u0084\u0085\7x\2\2\u0085\u0086\7c\2\2\u0086")
        buf.write("\u0087\7t\2\2\u0087\20\3\2\2\2\u0088\u0089\7f\2\2\u0089")
        buf.write("\u008a\7{\2\2\u008a\u008b\7p\2\2\u008b\u008c\7c\2\2\u008c")
        buf.write("\u008d\7o\2\2\u008d\u008e\7k\2\2\u008e\u008f\7e\2\2\u008f")
        buf.write("\22\3\2\2\2\u0090\u0091\7h\2\2\u0091\u0092\7w\2\2\u0092")
        buf.write("\u0093\7p\2\2\u0093\u0094\7e\2\2\u0094\24\3\2\2\2\u0095")
        buf.write("\u0096\7h\2\2\u0096\u0097\7q\2\2\u0097\u0098\7t\2\2\u0098")
        buf.write("\26\3\2\2\2\u0099\u009a\7w\2\2\u009a\u009b\7p\2\2\u009b")
        buf.write("\u009c\7v\2\2\u009c\u009d\7k\2\2\u009d\u009e\7n\2\2\u009e")
        buf.write("\30\3\2\2\2\u009f\u00a0\7d\2\2\u00a0\u00a1\7{\2\2\u00a1")
        buf.write("\32\3\2\2\2\u00a2\u00a3\7d\2\2\u00a3\u00a4\7t\2\2\u00a4")
        buf.write("\u00a5\7g\2\2\u00a5\u00a6\7c\2\2\u00a6\u00a7\7m\2\2\u00a7")
        buf.write("\34\3\2\2\2\u00a8\u00a9\7e\2\2\u00a9\u00aa\7q\2\2\u00aa")
        buf.write("\u00ab\7p\2\2\u00ab\u00ac\7v\2\2\u00ac\u00ad\7k\2\2\u00ad")
        buf.write("\u00ae\7p\2\2\u00ae\u00af\7w\2\2\u00af\u00b0\7g\2\2\u00b0")
        buf.write("\36\3\2\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3\7h\2\2\u00b3")
        buf.write(" \3\2\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6\7n\2\2\u00b6")
        buf.write("\u00b7\7u\2\2\u00b7\u00b8\7g\2\2\u00b8\"\3\2\2\2\u00b9")
        buf.write("\u00ba\7g\2\2\u00ba\u00bb\7n\2\2\u00bb\u00bc\7k\2\2\u00bc")
        buf.write("\u00bd\7h\2\2\u00bd$\3\2\2\2\u00be\u00bf\7d\2\2\u00bf")
        buf.write("\u00c0\7g\2\2\u00c0\u00c1\7i\2\2\u00c1\u00c2\7k\2\2\u00c2")
        buf.write("\u00c3\7p\2\2\u00c3&\3\2\2\2\u00c4\u00c5\7g\2\2\u00c5")
        buf.write("\u00c6\7p\2\2\u00c6\u00c7\7f\2\2\u00c7(\3\2\2\2\u00c8")
        buf.write("\u00c9\7p\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb\7v\2\2\u00cb")
        buf.write("*\3\2\2\2\u00cc\u00cd\7c\2\2\u00cd\u00ce\7p\2\2\u00ce")
        buf.write("\u00cf\7f\2\2\u00cf,\3\2\2\2\u00d0\u00d1\7q\2\2\u00d1")
        buf.write("\u00d2\7t\2\2\u00d2.\3\2\2\2\u00d3\u00d4\7-\2\2\u00d4")
        buf.write("\60\3\2\2\2\u00d5\u00d6\7/\2\2\u00d6\62\3\2\2\2\u00d7")
        buf.write("\u00d8\7,\2\2\u00d8\64\3\2\2\2\u00d9\u00da\7\61\2\2\u00da")
        buf.write("\66\3\2\2\2\u00db\u00dc\7\'\2\2\u00dc8\3\2\2\2\u00dd\u00de")
        buf.write("\7?\2\2\u00de:\3\2\2\2\u00df\u00e0\7>\2\2\u00e0\u00e1")
        buf.write("\7/\2\2\u00e1<\3\2\2\2\u00e2\u00e3\7#\2\2\u00e3\u00e4")
        buf.write("\7?\2\2\u00e4>\3\2\2\2\u00e5\u00e6\7>\2\2\u00e6@\3\2\2")
        buf.write("\2\u00e7\u00e8\7>\2\2\u00e8\u00e9\7?\2\2\u00e9B\3\2\2")
        buf.write("\2\u00ea\u00eb\7@\2\2\u00ebD\3\2\2\2\u00ec\u00ed\7@\2")
        buf.write("\2\u00ed\u00ee\7?\2\2\u00eeF\3\2\2\2\u00ef\u00f0\7\60")
        buf.write("\2\2\u00f0\u00f1\7\60\2\2\u00f1\u00f2\7\60\2\2\u00f2H")
        buf.write("\3\2\2\2\u00f3\u00f4\7?\2\2\u00f4\u00f5\7?\2\2\u00f5J")
        buf.write("\3\2\2\2\u00f6\u00f7\7]\2\2\u00f7L\3\2\2\2\u00f8\u00f9")
        buf.write("\7_\2\2\u00f9N\3\2\2\2\u00fa\u00fb\7*\2\2\u00fbP\3\2\2")
        buf.write("\2\u00fc\u00fd\7+\2\2\u00fdR\3\2\2\2\u00fe\u00ff\7.\2")
        buf.write("\2\u00ffT\3\2\2\2\u0100\u0104\t\2\2\2\u0101\u0103\t\3")
        buf.write("\2\2\u0102\u0101\3\2\2\2\u0103\u0106\3\2\2\2\u0104\u0102")
        buf.write("\3\2\2\2\u0104\u0105\3\2\2\2\u0105V\3\2\2\2\u0106\u0104")
        buf.write("\3\2\2\2\u0107\u0109\t\4\2\2\u0108\u0107\3\2\2\2\u0109")
        buf.write("\u010a\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2")
        buf.write("\u010b\u010c\3\2\2\2\u010c\u010d\b,\2\2\u010dX\3\2\2\2")
        buf.write("\u010e\u010f\13\2\2\2\u010f\u0110\b-\3\2\u0110Z\3\2\2")
        buf.write("\2\u0111\u0112\13\2\2\2\u0112\\\3\2\2\2\u0113\u0114\13")
        buf.write("\2\2\2\u0114^\3\2\2\2\5\2\u0104\u010a\4\b\2\2\3-\2")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    NOT = 20
    AND = 21
    OR = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    EQUAL = 28
    ASSIGN = 29
    NOT_EQUAL = 30
    LT = 31
    LE = 32
    GT = 33
    GE = 34
    CONCAT = 35
    STRCMP = 36
    LBRACKET = 37
    RBRACKET = 38
    LPARENT = 39
    RPARENT = 40
    COMMA = 41
    ID = 42
    WS = 43
    ERROR_CHAR = 44
    UNCLOSE_STRING = 45
    ILLEGAL_ESCAPE = 46

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'['", "']'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "EQUAL", "ASSIGN", "NOT_EQUAL", 
            "LT", "LE", "GT", "GE", "CONCAT", "STRCMP", "LBRACKET", "RBRACKET", 
            "LPARENT", "RPARENT", "COMMA", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", 
                  "ASSIGN", "NOT_EQUAL", "LT", "LE", "GT", "GE", "CONCAT", 
                  "STRCMP", "LBRACKET", "RBRACKET", "LPARENT", "RPARENT", 
                  "COMMA", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[43] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


