grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: EOF;


//! --------------------------  Lexical structure ----------------------- //

/*
* hiện thực phần KeyWord và Operators và Separators và  Identifiers và Literal  và ERROR
* kiểm tra test case python/python3 run.py test LexerSuite
*/


// TODO KeyWord
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';

NOT: 'not';
AND: 'and';
OR: 'or';

// TODO Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '=';
ASSIGN: '<-';
NOT_EQUAL: '!=';
LT: '<';
LE: '<=';
GT: '>';
GE: '>=';
CONCAT: '...';
STRCMP: '==';

// TODO Separators
LBRACKET: '[';
RBRACKET: ']';
LPARENT: '(';
RPARENT: ')';
COMMA: ',';

// TODO Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;


// TODO Literal 
// ! STRING_LIT nhớ dùng python bỏ đi " " đầu và cuối và NUMBER_LIT
// STRING_LIT: '"'(~[\r\n\f\\'"] | '\\'[bfrnt'\\] | '\'"')* '"'{self.text = self.text[1:-1];};
STRING_LIT: '"'(~[\r\n\f\\'"] | VALID_SEQUENCE)* '"'{self.text = self.text[1:-1];};
fragment VALID_SEQUENCE: '\\' [bfrnt'\\] | '\'"';

NUMBER_LIT: DIGIT+ (DECIMAL | DECIMAL? EXPONENT?);
BOOL_LIT: TRUE | FALSE;

fragment DIGIT: [0-9];
fragment SIGN: [+-];
fragment EXPONENT: [eE] SIGN? DIGIT+;
fragment DECIMAL: '.' DIGIT*;

// NEWLINE COMMENTS WS
//! vì NEWLINE là kí tự kết thúc giống với ';' trong C nên lấy để xử lí bước sau
//! vì ngôn ngữ này COMMENTS chỉ 1 hàng không chung với mấng y biểu thức khác nên bắt để xử lí thứ tự các bước sau
//! COMMENTS lên lớp nghe thử thầy nói gì khônha vì này nén lỗi phần lexer cũng được mà nhưng thứ tự ngữ pháp và ở phần tiếp theo -> này tùy thầy thôi
NEWLINE: [\n]; // 
COMMENTS: '##' ~[\n\r\f]*; // Comments
WS : [ \t\r]+ -> skip ; // skip spaces, tabs


// TODO ERROR
//! hiện thực  UNCLOSE_STRING và ILLEGAL_ESCAPE code antlr và python tận dụng lại ý tưởng STRING_LIT
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"'(~[\r\n\f\\'"] | VALID_SEQUENCE)* {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE: '"' ( '\'' ~["] | '\\' ~[bfrnt'\\] | [\r\n\f\\'"])* '"' {raise IllegalEscape(self.text[1:])};



//!  -------------------------- end Lexical structure ------------------- //