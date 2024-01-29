# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u017e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\7\2X\n\2\f\2\16")
        buf.write("\2[\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3d\n\3\3\4\3\4")
        buf.write("\3\4\3\4\5\4j\n\4\3\5\3\5\3\5\5\5o\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\5\7y\n\7\3\7\3\7\5\7}\n\7\3\b\3\b\3\b")
        buf.write("\3\b\5\b\u0083\n\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\5\13\u0090\n\13\3\f\3\f\3\f\3\f\5\f\u0096")
        buf.write("\n\f\3\f\3\f\5\f\u009a\n\f\3\f\3\f\5\f\u009e\n\f\3\f\3")
        buf.write("\f\5\f\u00a2\n\f\3\r\3\r\3\r\5\r\u00a7\n\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\5\r\u00af\n\r\5\r\u00b1\n\r\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u00b7\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\5\17\u00c2\n\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\5\21\u00ca\n\21\3\21\3\21\3\21\3\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\5\22\u00d7\n\22\3\22\5\22\u00da")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\5\24\u00e6\n\24\3\25\3\25\3\25\3\26\5\26\u00ec\n\26\3")
        buf.write("\26\3\26\5\26\u00f0\n\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u00f9\n\27\3\27\3\27\3\30\3\30\3\30\3\31\3")
        buf.write("\31\3\31\3\32\3\32\3\32\5\32\u0106\n\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\5\34\u0110\n\34\3\34\3\34\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\5\36\u011f\n\36\3\37\3\37\3\37\3\37\3\37\5\37\u0126\n")
        buf.write("\37\3 \3 \3 \3 \3 \5 \u012d\n \3!\3!\3!\3!\3!\3!\7!\u0135")
        buf.write("\n!\f!\16!\u0138\13!\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u0140")
        buf.write("\n\"\f\"\16\"\u0143\13\"\3#\3#\3#\3#\3#\3#\7#\u014b\n")
        buf.write("#\f#\16#\u014e\13#\3$\3$\3$\5$\u0153\n$\3%\3%\3%\5%\u0158")
        buf.write("\n%\3&\3&\3&\3&\3&\3&\3&\3&\5&\u0162\n&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\5\'\u0169\n\'\3(\3(\3(\3(\3)\3)\5)\u0171\n)\3)")
        buf.write("\3)\3*\3*\3*\3*\3+\6+\u017a\n+\r+\16+\u017b\3+\2\5@BD")
        buf.write(",\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRT\2\7\3\2\5\7\5\2\36\36 $&&\3\2\27")
        buf.write("\30\3\2\31\32\3\2\33\35\2\u0188\2Y\3\2\2\2\4c\3\2\2\2")
        buf.write("\6i\3\2\2\2\bn\3\2\2\2\np\3\2\2\2\fu\3\2\2\2\16~\3\2\2")
        buf.write("\2\20\u0084\3\2\2\2\22\u0086\3\2\2\2\24\u008f\3\2\2\2")
        buf.write("\26\u0091\3\2\2\2\30\u00b0\3\2\2\2\32\u00b6\3\2\2\2\34")
        buf.write("\u00c1\3\2\2\2\36\u00c3\3\2\2\2 \u00c9\3\2\2\2\"\u00cf")
        buf.write("\3\2\2\2$\u00db\3\2\2\2&\u00e5\3\2\2\2(\u00e7\3\2\2\2")
        buf.write("*\u00eb\3\2\2\2,\u00f1\3\2\2\2.\u00fc\3\2\2\2\60\u00ff")
        buf.write("\3\2\2\2\62\u0102\3\2\2\2\64\u0109\3\2\2\2\66\u010c\3")
        buf.write("\2\2\28\u0113\3\2\2\2:\u011e\3\2\2\2<\u0125\3\2\2\2>\u012c")
        buf.write("\3\2\2\2@\u012e\3\2\2\2B\u0139\3\2\2\2D\u0144\3\2\2\2")
        buf.write("F\u0152\3\2\2\2H\u0157\3\2\2\2J\u0161\3\2\2\2L\u0168\3")
        buf.write("\2\2\2N\u016a\3\2\2\2P\u0170\3\2\2\2R\u0174\3\2\2\2T\u0179")
        buf.write("\3\2\2\2VX\7\60\2\2WV\3\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3")
        buf.write("\2\2\2Z\\\3\2\2\2[Y\3\2\2\2\\]\5\4\3\2]^\7\2\2\3^\3\3")
        buf.write("\2\2\2_`\5\6\4\2`a\5\4\3\2ad\3\2\2\2bd\5\6\4\2c_\3\2\2")
        buf.write("\2cb\3\2\2\2d\5\3\2\2\2ej\5\26\f\2fg\5\b\5\2gh\5T+\2h")
        buf.write("j\3\2\2\2ie\3\2\2\2if\3\2\2\2j\7\3\2\2\2ko\5\n\6\2lo\5")
        buf.write("\f\7\2mo\5\16\b\2nk\3\2\2\2nl\3\2\2\2nm\3\2\2\2o\t\3\2")
        buf.write("\2\2pq\7\t\2\2qr\7,\2\2rs\7\37\2\2st\5<\37\2t\13\3\2\2")
        buf.write("\2ux\5\20\t\2vy\7,\2\2wy\5\22\n\2xv\3\2\2\2xw\3\2\2\2")
        buf.write("y|\3\2\2\2z{\7\37\2\2{}\5<\37\2|z\3\2\2\2|}\3\2\2\2}\r")
        buf.write("\3\2\2\2~\177\7\n\2\2\177\u0082\7,\2\2\u0080\u0081\7\37")
        buf.write("\2\2\u0081\u0083\5<\37\2\u0082\u0080\3\2\2\2\u0082\u0083")
        buf.write("\3\2\2\2\u0083\17\3\2\2\2\u0084\u0085\t\2\2\2\u0085\21")
        buf.write("\3\2\2\2\u0086\u0087\7,\2\2\u0087\u0088\7\'\2\2\u0088")
        buf.write("\u0089\5\24\13\2\u0089\u008a\7(\2\2\u008a\23\3\2\2\2\u008b")
        buf.write("\u008c\7.\2\2\u008c\u008d\7+\2\2\u008d\u0090\5\24\13\2")
        buf.write("\u008e\u0090\7.\2\2\u008f\u008b\3\2\2\2\u008f\u008e\3")
        buf.write("\2\2\2\u0090\25\3\2\2\2\u0091\u0092\7\13\2\2\u0092\u0093")
        buf.write("\7,\2\2\u0093\u0095\7)\2\2\u0094\u0096\5\30\r\2\u0095")
        buf.write("\u0094\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\3\2\2\2")
        buf.write("\u0097\u00a1\7*\2\2\u0098\u009a\5T+\2\u0099\u0098\3\2")
        buf.write("\2\2\u0099\u009a\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u00a2")
        buf.write("\5\62\32\2\u009c\u009e\5T+\2\u009d\u009c\3\2\2\2\u009d")
        buf.write("\u009e\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a2\58\35\2")
        buf.write("\u00a0\u00a2\5T+\2\u00a1\u0099\3\2\2\2\u00a1\u009d\3\2")
        buf.write("\2\2\u00a1\u00a0\3\2\2\2\u00a2\27\3\2\2\2\u00a3\u00a6")
        buf.write("\5\20\t\2\u00a4\u00a7\7,\2\2\u00a5\u00a7\5\22\n\2\u00a6")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2")
        buf.write("\u00a8\u00a9\7+\2\2\u00a9\u00aa\5\30\r\2\u00aa\u00b1\3")
        buf.write("\2\2\2\u00ab\u00ae\5\20\t\2\u00ac\u00af\7,\2\2\u00ad\u00af")
        buf.write("\5\22\n\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af")
        buf.write("\u00b1\3\2\2\2\u00b0\u00a3\3\2\2\2\u00b0\u00ab\3\2\2\2")
        buf.write("\u00b1\31\3\2\2\2\u00b2\u00b3\5\34\17\2\u00b3\u00b4\5")
        buf.write("\32\16\2\u00b4\u00b7\3\2\2\2\u00b5\u00b7\3\2\2\2\u00b6")
        buf.write("\u00b2\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\33\3\2\2\2\u00b8")
        buf.write("\u00c2\5\36\20\2\u00b9\u00c2\5 \21\2\u00ba\u00c2\5\"\22")
        buf.write("\2\u00bb\u00c2\5,\27\2\u00bc\u00c2\5.\30\2\u00bd\u00c2")
        buf.write("\5\60\31\2\u00be\u00c2\5\62\32\2\u00bf\u00c2\5\64\33\2")
        buf.write("\u00c0\u00c2\58\35\2\u00c1\u00b8\3\2\2\2\u00c1\u00b9\3")
        buf.write("\2\2\2\u00c1\u00ba\3\2\2\2\u00c1\u00bb\3\2\2\2\u00c1\u00bc")
        buf.write("\3\2\2\2\u00c1\u00bd\3\2\2\2\u00c1\u00be\3\2\2\2\u00c1")
        buf.write("\u00bf\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\35\3\2\2\2\u00c3")
        buf.write("\u00c4\5\b\5\2\u00c4\u00c5\5T+\2\u00c5\37\3\2\2\2\u00c6")
        buf.write("\u00ca\7,\2\2\u00c7\u00c8\7,\2\2\u00c8\u00ca\5R*\2\u00c9")
        buf.write("\u00c6\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cb\3\2\2\2")
        buf.write("\u00cb\u00cc\7\37\2\2\u00cc\u00cd\5<\37\2\u00cd\u00ce")
        buf.write("\5T+\2\u00ce!\3\2\2\2\u00cf\u00d0\7\21\2\2\u00d0\u00d1")
        buf.write("\7)\2\2\u00d1\u00d2\5<\37\2\u00d2\u00d3\7*\2\2\u00d3\u00d4")
        buf.write("\5*\26\2\u00d4\u00d6\3\2\2\2\u00d5\u00d7\5&\24\2\u00d6")
        buf.write("\u00d5\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d9\3\2\2\2")
        buf.write("\u00d8\u00da\5(\25\2\u00d9\u00d8\3\2\2\2\u00d9\u00da\3")
        buf.write("\2\2\2\u00da#\3\2\2\2\u00db\u00dc\7\23\2\2\u00dc\u00dd")
        buf.write("\7)\2\2\u00dd\u00de\5<\37\2\u00de\u00df\7*\2\2\u00df\u00e0")
        buf.write("\5*\26\2\u00e0%\3\2\2\2\u00e1\u00e2\5$\23\2\u00e2\u00e3")
        buf.write("\5&\24\2\u00e3\u00e6\3\2\2\2\u00e4\u00e6\5$\23\2\u00e5")
        buf.write("\u00e1\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6\'\3\2\2\2\u00e7")
        buf.write("\u00e8\7\22\2\2\u00e8\u00e9\5*\26\2\u00e9)\3\2\2\2\u00ea")
        buf.write("\u00ec\5T+\2\u00eb\u00ea\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec")
        buf.write("\u00ed\3\2\2\2\u00ed\u00ef\5\34\17\2\u00ee\u00f0\5T+\2")
        buf.write("\u00ef\u00ee\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0+\3\2\2")
        buf.write("\2\u00f1\u00f2\7\f\2\2\u00f2\u00f3\7,\2\2\u00f3\u00f4")
        buf.write("\7\r\2\2\u00f4\u00f5\5<\37\2\u00f5\u00f6\7\16\2\2\u00f6")
        buf.write("\u00f8\5<\37\2\u00f7\u00f9\5T+\2\u00f8\u00f7\3\2\2\2\u00f8")
        buf.write("\u00f9\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\5\34\17")
        buf.write("\2\u00fb-\3\2\2\2\u00fc\u00fd\7\17\2\2\u00fd\u00fe\5T")
        buf.write("+\2\u00fe/\3\2\2\2\u00ff\u0100\7\20\2\2\u0100\u0101\5")
        buf.write("T+\2\u0101\61\3\2\2\2\u0102\u0105\7\b\2\2\u0103\u0106")
        buf.write("\5<\37\2\u0104\u0106\3\2\2\2\u0105\u0103\3\2\2\2\u0105")
        buf.write("\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108\5T+\2\u0108")
        buf.write("\63\3\2\2\2\u0109\u010a\5\66\34\2\u010a\u010b\5T+\2\u010b")
        buf.write("\65\3\2\2\2\u010c\u010d\7,\2\2\u010d\u010f\7)\2\2\u010e")
        buf.write("\u0110\5:\36\2\u010f\u010e\3\2\2\2\u010f\u0110\3\2\2\2")
        buf.write("\u0110\u0111\3\2\2\2\u0111\u0112\7*\2\2\u0112\67\3\2\2")
        buf.write("\2\u0113\u0114\7\24\2\2\u0114\u0115\5T+\2\u0115\u0116")
        buf.write("\5\32\16\2\u0116\u0117\7\25\2\2\u0117\u0118\5T+\2\u0118")
        buf.write("9\3\2\2\2\u0119\u011a\5<\37\2\u011a\u011b\7+\2\2\u011b")
        buf.write("\u011c\5:\36\2\u011c\u011f\3\2\2\2\u011d\u011f\5<\37\2")
        buf.write("\u011e\u0119\3\2\2\2\u011e\u011d\3\2\2\2\u011f;\3\2\2")
        buf.write("\2\u0120\u0121\5> \2\u0121\u0122\7%\2\2\u0122\u0123\5")
        buf.write("> \2\u0123\u0126\3\2\2\2\u0124\u0126\5> \2\u0125\u0120")
        buf.write("\3\2\2\2\u0125\u0124\3\2\2\2\u0126=\3\2\2\2\u0127\u0128")
        buf.write("\5@!\2\u0128\u0129\t\3\2\2\u0129\u012a\5@!\2\u012a\u012d")
        buf.write("\3\2\2\2\u012b\u012d\5@!\2\u012c\u0127\3\2\2\2\u012c\u012b")
        buf.write("\3\2\2\2\u012d?\3\2\2\2\u012e\u012f\b!\1\2\u012f\u0130")
        buf.write("\5B\"\2\u0130\u0136\3\2\2\2\u0131\u0132\f\4\2\2\u0132")
        buf.write("\u0133\t\4\2\2\u0133\u0135\5B\"\2\u0134\u0131\3\2\2\2")
        buf.write("\u0135\u0138\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137\3")
        buf.write("\2\2\2\u0137A\3\2\2\2\u0138\u0136\3\2\2\2\u0139\u013a")
        buf.write("\b\"\1\2\u013a\u013b\5D#\2\u013b\u0141\3\2\2\2\u013c\u013d")
        buf.write("\f\4\2\2\u013d\u013e\t\5\2\2\u013e\u0140\5D#\2\u013f\u013c")
        buf.write("\3\2\2\2\u0140\u0143\3\2\2\2\u0141\u013f\3\2\2\2\u0141")
        buf.write("\u0142\3\2\2\2\u0142C\3\2\2\2\u0143\u0141\3\2\2\2\u0144")
        buf.write("\u0145\b#\1\2\u0145\u0146\5F$\2\u0146\u014c\3\2\2\2\u0147")
        buf.write("\u0148\f\4\2\2\u0148\u0149\t\6\2\2\u0149\u014b\5F$\2\u014a")
        buf.write("\u0147\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2")
        buf.write("\u014c\u014d\3\2\2\2\u014dE\3\2\2\2\u014e\u014c\3\2\2")
        buf.write("\2\u014f\u0150\7\26\2\2\u0150\u0153\5F$\2\u0151\u0153")
        buf.write("\5H%\2\u0152\u014f\3\2\2\2\u0152\u0151\3\2\2\2\u0153G")
        buf.write("\3\2\2\2\u0154\u0155\t\5\2\2\u0155\u0158\5H%\2\u0156\u0158")
        buf.write("\5J&\2\u0157\u0154\3\2\2\2\u0157\u0156\3\2\2\2\u0158I")
        buf.write("\3\2\2\2\u0159\u0162\5P)\2\u015a\u0162\5L\'\2\u015b\u0162")
        buf.write("\7,\2\2\u015c\u015d\7)\2\2\u015d\u015e\5<\37\2\u015e\u015f")
        buf.write("\7*\2\2\u015f\u0162\3\2\2\2\u0160\u0162\5\66\34\2\u0161")
        buf.write("\u0159\3\2\2\2\u0161\u015a\3\2\2\2\u0161\u015b\3\2\2\2")
        buf.write("\u0161\u015c\3\2\2\2\u0161\u0160\3\2\2\2\u0162K\3\2\2")
        buf.write("\2\u0163\u0169\7.\2\2\u0164\u0169\7-\2\2\u0165\u0169\7")
        buf.write("\3\2\2\u0166\u0169\7\4\2\2\u0167\u0169\5N(\2\u0168\u0163")
        buf.write("\3\2\2\2\u0168\u0164\3\2\2\2\u0168\u0165\3\2\2\2\u0168")
        buf.write("\u0166\3\2\2\2\u0168\u0167\3\2\2\2\u0169M\3\2\2\2\u016a")
        buf.write("\u016b\7\'\2\2\u016b\u016c\5:\36\2\u016c\u016d\7(\2\2")
        buf.write("\u016dO\3\2\2\2\u016e\u0171\7,\2\2\u016f\u0171\5\66\34")
        buf.write("\2\u0170\u016e\3\2\2\2\u0170\u016f\3\2\2\2\u0171\u0172")
        buf.write("\3\2\2\2\u0172\u0173\5R*\2\u0173Q\3\2\2\2\u0174\u0175")
        buf.write("\7\'\2\2\u0175\u0176\5:\36\2\u0176\u0177\7(\2\2\u0177")
        buf.write("S\3\2\2\2\u0178\u017a\7\60\2\2\u0179\u0178\3\2\2\2\u017a")
        buf.write("\u017b\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017cU\3\2\2\2(Ycinx|\u0082\u008f\u0095\u0099\u009d\u00a1")
        buf.write("\u00a6\u00ae\u00b0\u00b6\u00c1\u00c9\u00d6\u00d9\u00e5")
        buf.write("\u00eb\u00ef\u00f8\u0105\u010f\u011e\u0125\u012c\u0136")
        buf.write("\u0141\u014c\u0152\u0157\u0161\u0168\u0170\u017b")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "'['", "']'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQUAL", "ASSIGN", "NOT_EQUAL", "LT", "LE", 
                      "GT", "GE", "CONCAT", "STRCMP", "LBRACKET", "RBRACKET", 
                      "LPARENT", "RPARENT", "COMMA", "ID", "STRING_LIT", 
                      "NUMBER_LIT", "BOOL_LIT", "NEWLINE", "COMMENTS", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_list_declared = 1
    RULE_declared = 2
    RULE_variables = 3
    RULE_implicit_var = 4
    RULE_keyword_var = 5
    RULE_implicit_dynamic = 6
    RULE_prim_type = 7
    RULE_array_declared = 8
    RULE_list_NUMBER_LIT = 9
    RULE_function = 10
    RULE_prameters_list = 11
    RULE_statement_list = 12
    RULE_statement = 13
    RULE_declaration_statement = 14
    RULE_assignment_statement = 15
    RULE_if_statement = 16
    RULE_elif_statement = 17
    RULE_elif_statement_list = 18
    RULE_else_statement = 19
    RULE_statement_block_if = 20
    RULE_for_statement = 21
    RULE_break_statement = 22
    RULE_continue_statement = 23
    RULE_return_statement = 24
    RULE_call_statement = 25
    RULE_func_call = 26
    RULE_block_statement = 27
    RULE_expression_list = 28
    RULE_expression = 29
    RULE_expression1 = 30
    RULE_expression2 = 31
    RULE_expression3 = 32
    RULE_expression4 = 33
    RULE_expression5 = 34
    RULE_expression6 = 35
    RULE_expression7 = 36
    RULE_literal = 37
    RULE_array_literal = 38
    RULE_array_element = 39
    RULE_index_operators = 40
    RULE_ignore = 41

    ruleNames =  [ "program", "list_declared", "declared", "variables", 
                   "implicit_var", "keyword_var", "implicit_dynamic", "prim_type", 
                   "array_declared", "list_NUMBER_LIT", "function", "prameters_list", 
                   "statement_list", "statement", "declaration_statement", 
                   "assignment_statement", "if_statement", "elif_statement", 
                   "elif_statement_list", "else_statement", "statement_block_if", 
                   "for_statement", "break_statement", "continue_statement", 
                   "return_statement", "call_statement", "func_call", "block_statement", 
                   "expression_list", "expression", "expression1", "expression2", 
                   "expression3", "expression4", "expression5", "expression6", 
                   "expression7", "literal", "array_literal", "array_element", 
                   "index_operators", "ignore" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    NUMBER=3
    BOOL=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    NOT=20
    AND=21
    OR=22
    ADD=23
    SUB=24
    MUL=25
    DIV=26
    MOD=27
    EQUAL=28
    ASSIGN=29
    NOT_EQUAL=30
    LT=31
    LE=32
    GT=33
    GE=34
    CONCAT=35
    STRCMP=36
    LBRACKET=37
    RBRACKET=38
    LPARENT=39
    RPARENT=40
    COMMA=41
    ID=42
    STRING_LIT=43
    NUMBER_LIT=44
    BOOL_LIT=45
    NEWLINE=46
    COMMENTS=47
    WS=48
    ERROR_CHAR=49
    UNCLOSE_STRING=50
    ILLEGAL_ESCAPE=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_declared(self):
            return self.getTypedRuleContext(ZCodeParser.List_declaredContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 84
                self.match(ZCodeParser.NEWLINE)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.list_declared()
            self.state = 91
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared(self):
            return self.getTypedRuleContext(ZCodeParser.DeclaredContext,0)


        def list_declared(self):
            return self.getTypedRuleContext(ZCodeParser.List_declaredContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_declared" ):
                return visitor.visitList_declared(self)
            else:
                return visitor.visitChildren(self)




    def list_declared(self):

        localctx = ZCodeParser.List_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_declared)
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.declared()
                self.state = 94
                self.list_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionContext,0)


        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = ZCodeParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declared)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.function()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.variables()
                self.state = 101
                self.ignore()
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


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def implicit_var(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_varContext,0)


        def keyword_var(self):
            return self.getTypedRuleContext(ZCodeParser.Keyword_varContext,0)


        def implicit_dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_dynamicContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = ZCodeParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variables)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.implicit_var()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.keyword_var()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                self.implicit_dynamic()
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


    class Implicit_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_var" ):
                return visitor.visitImplicit_var(self)
            else:
                return visitor.visitChildren(self)




    def implicit_var(self):

        localctx = ZCodeParser.Implicit_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_implicit_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(ZCodeParser.VAR)
            self.state = 111
            self.match(ZCodeParser.ID)
            self.state = 112
            self.match(ZCodeParser.ASSIGN)
            self.state = 113
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prim_type(self):
            return self.getTypedRuleContext(ZCodeParser.Prim_typeContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def array_declared(self):
            return self.getTypedRuleContext(ZCodeParser.Array_declaredContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_keyword_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_var" ):
                return visitor.visitKeyword_var(self)
            else:
                return visitor.visitChildren(self)




    def keyword_var(self):

        localctx = ZCodeParser.Keyword_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_keyword_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.prim_type()
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 116
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 117
                self.array_declared()
                pass


            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 120
                self.match(ZCodeParser.ASSIGN)
                self.state = 121
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_dynamicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_dynamic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_dynamic" ):
                return visitor.visitImplicit_dynamic(self)
            else:
                return visitor.visitChildren(self)




    def implicit_dynamic(self):

        localctx = ZCodeParser.Implicit_dynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_implicit_dynamic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(ZCodeParser.DYNAMIC)
            self.state = 125
            self.match(ZCodeParser.ID)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 126
                self.match(ZCodeParser.ASSIGN)
                self.state = 127
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prim_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_prim_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrim_type" ):
                return visitor.visitPrim_type(self)
            else:
                return visitor.visitChildren(self)




    def prim_type(self):

        localctx = ZCodeParser.Prim_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_prim_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
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


    class Array_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_NUMBER_LIT(self):
            return self.getTypedRuleContext(ZCodeParser.List_NUMBER_LITContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_declared" ):
                return visitor.visitArray_declared(self)
            else:
                return visitor.visitChildren(self)




    def array_declared(self):

        localctx = ZCodeParser.Array_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(ZCodeParser.ID)

            self.state = 133
            self.match(ZCodeParser.LBRACKET)
            self.state = 134
            self.list_NUMBER_LIT()
            self.state = 135
            self.match(ZCodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_NUMBER_LITContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_NUMBER_LIT(self):
            return self.getTypedRuleContext(ZCodeParser.List_NUMBER_LITContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_NUMBER_LIT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_NUMBER_LIT" ):
                return visitor.visitList_NUMBER_LIT(self)
            else:
                return visitor.visitChildren(self)




    def list_NUMBER_LIT(self):

        localctx = ZCodeParser.List_NUMBER_LITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_list_NUMBER_LIT)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(ZCodeParser.NUMBER_LIT)

                self.state = 138
                self.match(ZCodeParser.COMMA)
                self.state = 139
                self.list_NUMBER_LIT()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.match(ZCodeParser.NUMBER_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPARENT(self):
            return self.getToken(ZCodeParser.LPARENT, 0)

        def RPARENT(self):
            return self.getToken(ZCodeParser.RPARENT, 0)

        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def prameters_list(self):
            return self.getTypedRuleContext(ZCodeParser.Prameters_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ZCodeParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(ZCodeParser.FUNC)
            self.state = 144
            self.match(ZCodeParser.ID)
            self.state = 145
            self.match(ZCodeParser.LPARENT)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 146
                self.prameters_list()


            self.state = 149
            self.match(ZCodeParser.RPARENT)
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 150
                    self.ignore()


                self.state = 153
                self.return_statement()
                pass

            elif la_ == 2:
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 154
                    self.ignore()


                self.state = 157
                self.block_statement()
                pass

            elif la_ == 3:
                self.state = 158
                self.ignore()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prameters_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prim_type(self):
            return self.getTypedRuleContext(ZCodeParser.Prim_typeContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def prameters_list(self):
            return self.getTypedRuleContext(ZCodeParser.Prameters_listContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def array_declared(self):
            return self.getTypedRuleContext(ZCodeParser.Array_declaredContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_prameters_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrameters_list" ):
                return visitor.visitPrameters_list(self)
            else:
                return visitor.visitChildren(self)




    def prameters_list(self):

        localctx = ZCodeParser.Prameters_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_prameters_list)
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.prim_type()
                self.state = 164
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 162
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 163
                    self.array_declared()
                    pass


                self.state = 166
                self.match(ZCodeParser.COMMA)
                self.state = 167
                self.prameters_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.prim_type()
                self.state = 172
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 170
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 171
                    self.array_declared()
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = ZCodeParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_statement_list)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.statement()
                self.state = 177
                self.statement_list()
                pass
            elif token in [ZCodeParser.END]:
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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_statementContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ZCodeParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Call_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_statement)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.declaration_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 185
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 186
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 187
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 188
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 189
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 190
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_statement" ):
                return visitor.visitDeclaration_statement(self)
            else:
                return visitor.visitChildren(self)




    def declaration_statement(self):

        localctx = ZCodeParser.Declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_declaration_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.variables()
            self.state = 194
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 196
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 197
                self.match(ZCodeParser.ID)
                self.state = 198
                self.index_operators()
                pass


            self.state = 201
            self.match(ZCodeParser.ASSIGN)
            self.state = 202
            self.expression()
            self.state = 203
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LPARENT(self):
            return self.getToken(ZCodeParser.LPARENT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPARENT(self):
            return self.getToken(ZCodeParser.RPARENT, 0)

        def statement_block_if(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_block_ifContext,0)


        def elif_statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_statement_listContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Else_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(ZCodeParser.IF)
            self.state = 206
            self.match(ZCodeParser.LPARENT)
            self.state = 207
            self.expression()
            self.state = 208
            self.match(ZCodeParser.RPARENT)
            self.state = 209
            self.statement_block_if()
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 211
                self.elif_statement_list()


            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 214
                self.else_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LPARENT(self):
            return self.getToken(ZCodeParser.LPARENT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPARENT(self):
            return self.getToken(ZCodeParser.RPARENT, 0)

        def statement_block_if(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_block_ifContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_statement" ):
                return visitor.visitElif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elif_statement(self):

        localctx = ZCodeParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(ZCodeParser.ELIF)
            self.state = 218
            self.match(ZCodeParser.LPARENT)
            self.state = 219
            self.expression()
            self.state = 220
            self.match(ZCodeParser.RPARENT)
            self.state = 221
            self.statement_block_if()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_statementContext,0)


        def elif_statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_statement_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_statement_list" ):
                return visitor.visitElif_statement_list(self)
            else:
                return visitor.visitChildren(self)




    def elif_statement_list(self):

        localctx = ZCodeParser.Elif_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_elif_statement_list)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.elif_statement()
                self.state = 224
                self.elif_statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.elif_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def statement_block_if(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_block_ifContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = ZCodeParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(ZCodeParser.ELSE)
            self.state = 230
            self.statement_block_if()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_block_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_block_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_block_if" ):
                return visitor.visitStatement_block_if(self)
            else:
                return visitor.visitChildren(self)




    def statement_block_if(self):

        localctx = ZCodeParser.Statement_block_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_statement_block_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 232
                self.ignore()


            self.state = 235
            self.statement()
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 236
                self.ignore()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(ZCodeParser.FOR)
            self.state = 240
            self.match(ZCodeParser.ID)
            self.state = 241
            self.match(ZCodeParser.UNTIL)
            self.state = 242
            self.expression()
            self.state = 243
            self.match(ZCodeParser.BY)
            self.state = 244
            self.expression()

            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 245
                self.ignore()


            self.state = 248
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(ZCodeParser.BREAK)
            self.state = 251
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(ZCodeParser.CONTINUE)
            self.state = 254
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(ZCodeParser.RETURN)
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.ADD, ZCodeParser.SUB, ZCodeParser.LBRACKET, ZCodeParser.LPARENT, ZCodeParser.ID, ZCodeParser.STRING_LIT, ZCodeParser.NUMBER_LIT]:
                self.state = 257
                self.expression()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 261
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = ZCodeParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.func_call()
            self.state = 264
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPARENT(self):
            return self.getToken(ZCodeParser.LPARENT, 0)

        def RPARENT(self):
            return self.getToken(ZCodeParser.RPARENT, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = ZCodeParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(ZCodeParser.ID)

            self.state = 267
            self.match(ZCodeParser.LPARENT)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.LPARENT) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.NUMBER_LIT))) != 0):
                self.state = 268
                self.expression_list()


            self.state = 271
            self.match(ZCodeParser.RPARENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = ZCodeParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(ZCodeParser.BEGIN)
            self.state = 274
            self.ignore()
            self.state = 275
            self.statement_list()
            self.state = 276
            self.match(ZCodeParser.END)
            self.state = 277
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = ZCodeParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expression_list)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.expression()
                self.state = 280
                self.match(ZCodeParser.COMMA)
                self.state = 281
                self.expression_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expression)
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.expression1()
                self.state = 287
                self.match(ZCodeParser.CONCAT)
                self.state = 288
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression2Context,i)


        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def STRCMP(self):
            return self.getToken(ZCodeParser.STRCMP, 0)

        def NOT_EQUAL(self):
            return self.getToken(ZCodeParser.NOT_EQUAL, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def LE(self):
            return self.getToken(ZCodeParser.LE, 0)

        def GE(self):
            return self.getToken(ZCodeParser.GE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = ZCodeParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.expression2(0)
                self.state = 294
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.LE) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.GE) | (1 << ZCodeParser.STRCMP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 295
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.expression2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(ZCodeParser.Expression2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 308
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 303
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 304
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 305
                    self.expression3(0) 
                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 319
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 314
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 315
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 316
                    self.expression4(0) 
                self.state = 321
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 330
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 325
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 326
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 327
                    self.expression5() 
                self.state = 332
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = ZCodeParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expression5)
        try:
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.match(ZCodeParser.NOT)
                self.state = 334
                self.expression5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.ADD, ZCodeParser.SUB, ZCodeParser.LBRACKET, ZCodeParser.LPARENT, ZCodeParser.ID, ZCodeParser.STRING_LIT, ZCodeParser.NUMBER_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.expression6()
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


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def expression7(self):
            return self.getTypedRuleContext(ZCodeParser.Expression7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)




    def expression6(self):

        localctx = ZCodeParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expression6)
        self._la = 0 # Token type
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ADD, ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 339
                self.expression6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LBRACKET, ZCodeParser.LPARENT, ZCodeParser.ID, ZCodeParser.STRING_LIT, ZCodeParser.NUMBER_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.expression7()
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


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element(self):
            return self.getTypedRuleContext(ZCodeParser.Array_elementContext,0)


        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPARENT(self):
            return self.getToken(ZCodeParser.LPARENT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPARENT(self):
            return self.getToken(ZCodeParser.RPARENT, 0)

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = ZCodeParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expression7)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.array_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 346
                self.match(ZCodeParser.LPARENT)
                self.state = 347
                self.expression()
                self.state = 348
                self.match(ZCodeParser.RPARENT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 350
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_literal)
        try:
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.match(ZCodeParser.NUMBER_LIT)
                pass
            elif token in [ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.match(ZCodeParser.STRING_LIT)
                pass
            elif token in [ZCodeParser.TRUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 355
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [ZCodeParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 356
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [ZCodeParser.LBRACKET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 357
                self.array_literal()
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


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = ZCodeParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(ZCodeParser.LBRACKET)
            self.state = 361
            self.expression_list()
            self.state = 362
            self.match(ZCodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = ZCodeParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_array_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 364
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 365
                self.func_call()
                pass


            self.state = 368
            self.index_operators()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = ZCodeParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_index_operators)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(ZCodeParser.LBRACKET)
            self.state = 371
            self.expression_list()
            self.state = 372
            self.match(ZCodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ignore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




    def ignore(self):

        localctx = ZCodeParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_ignore)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 374
                    self.match(ZCodeParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 377 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[31] = self.expression2_sempred
        self._predicates[32] = self.expression3_sempred
        self._predicates[33] = self.expression4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




