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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u018e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$")
        buf.write("\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+")
        buf.write("\7+\u011b\n+\f+\16+\u011e\13+\3,\3,\3,\7,\u0123\n,\f,")
        buf.write("\16,\u0126\13,\3,\3,\3,\3-\3-\3-\3-\5-\u012f\n-\3.\3.")
        buf.write("\3/\6/\u0134\n/\r/\16/\u0135\3/\3/\5/\u013a\n/\3/\5/\u013d")
        buf.write("\n/\5/\u013f\n/\3\60\3\60\3\61\3\61\3\62\3\62\5\62\u0147")
        buf.write("\n\62\3\62\6\62\u014a\n\62\r\62\16\62\u014b\3\63\3\63")
        buf.write("\7\63\u0150\n\63\f\63\16\63\u0153\13\63\3\64\3\64\5\64")
        buf.write("\u0157\n\64\3\65\3\65\3\66\3\66\3\66\3\66\7\66\u015f\n")
        buf.write("\66\f\66\16\66\u0162\13\66\3\67\6\67\u0165\n\67\r\67\16")
        buf.write("\67\u0166\3\67\3\67\38\38\38\39\39\39\79\u0171\n9\f9\16")
        buf.write("9\u0174\139\39\39\39\59\u0179\n9\39\39\3:\3:\3:\7:\u0180")
        buf.write("\n:\f:\16:\u0183\13:\3:\3:\3:\3;\3;\3;\3;\3;\5;\u018d")
        buf.write("\n;\2\2<\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27")
        buf.write("-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%")
        buf.write("I&K\'M(O)Q*S+U,W-Y\2[\2]._\2a\2c\2e\2g/i\60k\61m\62o\63")
        buf.write("q\64s\65u\2\3\2\20\5\2C\\aac|\6\2\62;C\\aac|\t\2))^^d")
        buf.write("dhhppttvv\7\2\f\f\16\17$$))^^\3\2\62;\4\2--//\4\2GGgg")
        buf.write("\3\2\f\f\4\2\f\f\16\17\5\2\13\13\17\17\"\"\3\3\f\f\3\2")
        buf.write("^^\3\2))\3\2$$\2\u019b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2]\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\3w\3\2\2\2\5|\3\2\2\2\7")
        buf.write("\u0082\3\2\2\2\t\u0089\3\2\2\2\13\u008e\3\2\2\2\r\u0095")
        buf.write("\3\2\2\2\17\u009c\3\2\2\2\21\u00a0\3\2\2\2\23\u00a8\3")
        buf.write("\2\2\2\25\u00ad\3\2\2\2\27\u00b1\3\2\2\2\31\u00b7\3\2")
        buf.write("\2\2\33\u00ba\3\2\2\2\35\u00c0\3\2\2\2\37\u00c9\3\2\2")
        buf.write("\2!\u00cc\3\2\2\2#\u00d1\3\2\2\2%\u00d6\3\2\2\2\'\u00dc")
        buf.write("\3\2\2\2)\u00e0\3\2\2\2+\u00e4\3\2\2\2-\u00e8\3\2\2\2")
        buf.write("/\u00eb\3\2\2\2\61\u00ed\3\2\2\2\63\u00ef\3\2\2\2\65\u00f1")
        buf.write("\3\2\2\2\67\u00f3\3\2\2\29\u00f5\3\2\2\2;\u00f7\3\2\2")
        buf.write("\2=\u00fa\3\2\2\2?\u00fd\3\2\2\2A\u00ff\3\2\2\2C\u0102")
        buf.write("\3\2\2\2E\u0104\3\2\2\2G\u0107\3\2\2\2I\u010b\3\2\2\2")
        buf.write("K\u010e\3\2\2\2M\u0110\3\2\2\2O\u0112\3\2\2\2Q\u0114\3")
        buf.write("\2\2\2S\u0116\3\2\2\2U\u0118\3\2\2\2W\u011f\3\2\2\2Y\u012e")
        buf.write("\3\2\2\2[\u0130\3\2\2\2]\u0133\3\2\2\2_\u0140\3\2\2\2")
        buf.write("a\u0142\3\2\2\2c\u0144\3\2\2\2e\u014d\3\2\2\2g\u0156\3")
        buf.write("\2\2\2i\u0158\3\2\2\2k\u015a\3\2\2\2m\u0164\3\2\2\2o\u016a")
        buf.write("\3\2\2\2q\u016d\3\2\2\2s\u017c\3\2\2\2u\u018c\3\2\2\2")
        buf.write("wx\7v\2\2xy\7t\2\2yz\7w\2\2z{\7g\2\2{\4\3\2\2\2|}\7h\2")
        buf.write("\2}~\7c\2\2~\177\7n\2\2\177\u0080\7u\2\2\u0080\u0081\7")
        buf.write("g\2\2\u0081\6\3\2\2\2\u0082\u0083\7p\2\2\u0083\u0084\7")
        buf.write("w\2\2\u0084\u0085\7o\2\2\u0085\u0086\7d\2\2\u0086\u0087")
        buf.write("\7g\2\2\u0087\u0088\7t\2\2\u0088\b\3\2\2\2\u0089\u008a")
        buf.write("\7d\2\2\u008a\u008b\7q\2\2\u008b\u008c\7q\2\2\u008c\u008d")
        buf.write("\7n\2\2\u008d\n\3\2\2\2\u008e\u008f\7u\2\2\u008f\u0090")
        buf.write("\7v\2\2\u0090\u0091\7t\2\2\u0091\u0092\7k\2\2\u0092\u0093")
        buf.write("\7p\2\2\u0093\u0094\7i\2\2\u0094\f\3\2\2\2\u0095\u0096")
        buf.write("\7t\2\2\u0096\u0097\7g\2\2\u0097\u0098\7v\2\2\u0098\u0099")
        buf.write("\7w\2\2\u0099\u009a\7t\2\2\u009a\u009b\7p\2\2\u009b\16")
        buf.write("\3\2\2\2\u009c\u009d\7x\2\2\u009d\u009e\7c\2\2\u009e\u009f")
        buf.write("\7t\2\2\u009f\20\3\2\2\2\u00a0\u00a1\7f\2\2\u00a1\u00a2")
        buf.write("\7{\2\2\u00a2\u00a3\7p\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5")
        buf.write("\7o\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7\7e\2\2\u00a7\22")
        buf.write("\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa\7w\2\2\u00aa\u00ab")
        buf.write("\7p\2\2\u00ab\u00ac\7e\2\2\u00ac\24\3\2\2\2\u00ad\u00ae")
        buf.write("\7h\2\2\u00ae\u00af\7q\2\2\u00af\u00b0\7t\2\2\u00b0\26")
        buf.write("\3\2\2\2\u00b1\u00b2\7w\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4")
        buf.write("\7v\2\2\u00b4\u00b5\7k\2\2\u00b5\u00b6\7n\2\2\u00b6\30")
        buf.write("\3\2\2\2\u00b7\u00b8\7d\2\2\u00b8\u00b9\7{\2\2\u00b9\32")
        buf.write("\3\2\2\2\u00ba\u00bb\7d\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd")
        buf.write("\7g\2\2\u00bd\u00be\7c\2\2\u00be\u00bf\7m\2\2\u00bf\34")
        buf.write("\3\2\2\2\u00c0\u00c1\7e\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3")
        buf.write("\7p\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6")
        buf.write("\7p\2\2\u00c6\u00c7\7w\2\2\u00c7\u00c8\7g\2\2\u00c8\36")
        buf.write("\3\2\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb\7h\2\2\u00cb ")
        buf.write("\3\2\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce\7n\2\2\u00ce\u00cf")
        buf.write("\7u\2\2\u00cf\u00d0\7g\2\2\u00d0\"\3\2\2\2\u00d1\u00d2")
        buf.write("\7g\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5")
        buf.write("\7h\2\2\u00d5$\3\2\2\2\u00d6\u00d7\7d\2\2\u00d7\u00d8")
        buf.write("\7g\2\2\u00d8\u00d9\7i\2\2\u00d9\u00da\7k\2\2\u00da\u00db")
        buf.write("\7p\2\2\u00db&\3\2\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de")
        buf.write("\7p\2\2\u00de\u00df\7f\2\2\u00df(\3\2\2\2\u00e0\u00e1")
        buf.write("\7p\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3\7v\2\2\u00e3*\3")
        buf.write("\2\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7")
        buf.write("\7f\2\2\u00e7,\3\2\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea")
        buf.write("\7t\2\2\u00ea.\3\2\2\2\u00eb\u00ec\7-\2\2\u00ec\60\3\2")
        buf.write("\2\2\u00ed\u00ee\7/\2\2\u00ee\62\3\2\2\2\u00ef\u00f0\7")
        buf.write(",\2\2\u00f0\64\3\2\2\2\u00f1\u00f2\7\61\2\2\u00f2\66\3")
        buf.write("\2\2\2\u00f3\u00f4\7\'\2\2\u00f48\3\2\2\2\u00f5\u00f6")
        buf.write("\7?\2\2\u00f6:\3\2\2\2\u00f7\u00f8\7>\2\2\u00f8\u00f9")
        buf.write("\7/\2\2\u00f9<\3\2\2\2\u00fa\u00fb\7#\2\2\u00fb\u00fc")
        buf.write("\7?\2\2\u00fc>\3\2\2\2\u00fd\u00fe\7>\2\2\u00fe@\3\2\2")
        buf.write("\2\u00ff\u0100\7>\2\2\u0100\u0101\7?\2\2\u0101B\3\2\2")
        buf.write("\2\u0102\u0103\7@\2\2\u0103D\3\2\2\2\u0104\u0105\7@\2")
        buf.write("\2\u0105\u0106\7?\2\2\u0106F\3\2\2\2\u0107\u0108\7\60")
        buf.write("\2\2\u0108\u0109\7\60\2\2\u0109\u010a\7\60\2\2\u010aH")
        buf.write("\3\2\2\2\u010b\u010c\7?\2\2\u010c\u010d\7?\2\2\u010dJ")
        buf.write("\3\2\2\2\u010e\u010f\7]\2\2\u010fL\3\2\2\2\u0110\u0111")
        buf.write("\7_\2\2\u0111N\3\2\2\2\u0112\u0113\7*\2\2\u0113P\3\2\2")
        buf.write("\2\u0114\u0115\7+\2\2\u0115R\3\2\2\2\u0116\u0117\7.\2")
        buf.write("\2\u0117T\3\2\2\2\u0118\u011c\t\2\2\2\u0119\u011b\t\3")
        buf.write("\2\2\u011a\u0119\3\2\2\2\u011b\u011e\3\2\2\2\u011c\u011a")
        buf.write("\3\2\2\2\u011c\u011d\3\2\2\2\u011dV\3\2\2\2\u011e\u011c")
        buf.write("\3\2\2\2\u011f\u0124\7$\2\2\u0120\u0123\5[.\2\u0121\u0123")
        buf.write("\5Y-\2\u0122\u0120\3\2\2\2\u0122\u0121\3\2\2\2\u0123\u0126")
        buf.write("\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125")
        buf.write("\u0127\3\2\2\2\u0126\u0124\3\2\2\2\u0127\u0128\7$\2\2")
        buf.write("\u0128\u0129\b,\2\2\u0129X\3\2\2\2\u012a\u012b\7^\2\2")
        buf.write("\u012b\u012f\t\4\2\2\u012c\u012d\7)\2\2\u012d\u012f\7")
        buf.write("$\2\2\u012e\u012a\3\2\2\2\u012e\u012c\3\2\2\2\u012fZ\3")
        buf.write("\2\2\2\u0130\u0131\n\5\2\2\u0131\\\3\2\2\2\u0132\u0134")
        buf.write("\5_\60\2\u0133\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135")
        buf.write("\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u013e\3\2\2\2")
        buf.write("\u0137\u013f\5e\63\2\u0138\u013a\5e\63\2\u0139\u0138\3")
        buf.write("\2\2\2\u0139\u013a\3\2\2\2\u013a\u013c\3\2\2\2\u013b\u013d")
        buf.write("\5c\62\2\u013c\u013b\3\2\2\2\u013c\u013d\3\2\2\2\u013d")
        buf.write("\u013f\3\2\2\2\u013e\u0137\3\2\2\2\u013e\u0139\3\2\2\2")
        buf.write("\u013f^\3\2\2\2\u0140\u0141\t\6\2\2\u0141`\3\2\2\2\u0142")
        buf.write("\u0143\t\7\2\2\u0143b\3\2\2\2\u0144\u0146\t\b\2\2\u0145")
        buf.write("\u0147\5a\61\2\u0146\u0145\3\2\2\2\u0146\u0147\3\2\2\2")
        buf.write("\u0147\u0149\3\2\2\2\u0148\u014a\5_\60\2\u0149\u0148\3")
        buf.write("\2\2\2\u014a\u014b\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c")
        buf.write("\3\2\2\2\u014cd\3\2\2\2\u014d\u0151\7\60\2\2\u014e\u0150")
        buf.write("\5_\60\2\u014f\u014e\3\2\2\2\u0150\u0153\3\2\2\2\u0151")
        buf.write("\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152f\3\2\2\2\u0153")
        buf.write("\u0151\3\2\2\2\u0154\u0157\5\3\2\2\u0155\u0157\5\5\3\2")
        buf.write("\u0156\u0154\3\2\2\2\u0156\u0155\3\2\2\2\u0157h\3\2\2")
        buf.write("\2\u0158\u0159\t\t\2\2\u0159j\3\2\2\2\u015a\u015b\7%\2")
        buf.write("\2\u015b\u015c\7%\2\2\u015c\u0160\3\2\2\2\u015d\u015f")
        buf.write("\n\n\2\2\u015e\u015d\3\2\2\2\u015f\u0162\3\2\2\2\u0160")
        buf.write("\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161l\3\2\2\2\u0162")
        buf.write("\u0160\3\2\2\2\u0163\u0165\t\13\2\2\u0164\u0163\3\2\2")
        buf.write("\2\u0165\u0166\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167")
        buf.write("\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0169\b\67\3\2\u0169")
        buf.write("n\3\2\2\2\u016a\u016b\13\2\2\2\u016b\u016c\b8\4\2\u016c")
        buf.write("p\3\2\2\2\u016d\u0172\7$\2\2\u016e\u0171\5[.\2\u016f\u0171")
        buf.write("\5Y-\2\u0170\u016e\3\2\2\2\u0170\u016f\3\2\2\2\u0171\u0174")
        buf.write("\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write("\u0178\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0176\7\17\2")
        buf.write("\2\u0176\u0179\7\f\2\2\u0177\u0179\t\f\2\2\u0178\u0175")
        buf.write("\3\2\2\2\u0178\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a")
        buf.write("\u017b\b9\5\2\u017br\3\2\2\2\u017c\u0181\7$\2\2\u017d")
        buf.write("\u0180\5[.\2\u017e\u0180\5Y-\2\u017f\u017d\3\2\2\2\u017f")
        buf.write("\u017e\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f\3\2\2\2")
        buf.write("\u0181\u0182\3\2\2\2\u0182\u0184\3\2\2\2\u0183\u0181\3")
        buf.write("\2\2\2\u0184\u0185\5u;\2\u0185\u0186\b:\6\2\u0186t\3\2")
        buf.write("\2\2\u0187\u0188\7^\2\2\u0188\u018d\n\4\2\2\u0189\u018d")
        buf.write("\n\r\2\2\u018a\u018b\t\16\2\2\u018b\u018d\n\17\2\2\u018c")
        buf.write("\u0187\3\2\2\2\u018c\u0189\3\2\2\2\u018c\u018a\3\2\2\2")
        buf.write("\u018dv\3\2\2\2\27\2\u011c\u0122\u0124\u012e\u0135\u0139")
        buf.write("\u013c\u013e\u0146\u014b\u0151\u0156\u0160\u0166\u0170")
        buf.write("\u0172\u0178\u017f\u0181\u018c\7\3,\2\b\2\2\38\3\39\4")
        buf.write("\3:\5")
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
    STRING_LIT = 43
    NUMBER_LIT = 44
    BOOL_LIT = 45
    NEWLINE = 46
    COMMENTS = 47
    WS = 48
    ERROR_CHAR = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51

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
            "LPARENT", "RPARENT", "COMMA", "ID", "STRING_LIT", "NUMBER_LIT", 
            "BOOL_LIT", "NEWLINE", "COMMENTS", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", 
                  "ASSIGN", "NOT_EQUAL", "LT", "LE", "GT", "GE", "CONCAT", 
                  "STRCMP", "LBRACKET", "RBRACKET", "LPARENT", "RPARENT", 
                  "COMMA", "ID", "STRING_LIT", "VALID_ESCAPE", "VALID_SEQUENCE", 
                  "NUMBER_LIT", "DIGIT", "SIGN", "EXPONENT", "DECIMAL", 
                  "BOOL_LIT", "NEWLINE", "COMMENTS", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "INVALID_ESCAPE" ]

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
            actions[42] = self.STRING_LIT_action 
            actions[54] = self.ERROR_CHAR_action 
            actions[55] = self.UNCLOSE_STRING_action 
            actions[56] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1];
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             
            	tmp = self.text[1:].split("\n")[0]
            	tmp = tmp.split("\r")[0]
            	self.text = tmp
            	raise UncloseString(self.text)

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text[1:])
     


