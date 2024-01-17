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
// STRING
STRING_LIT: '"'(VALID_SEQUENCE | VALID_ESCAPE)* '"'{self.text = self.text[1:-1];};
fragment VALID_ESCAPE: '\\' [bfrnt'\\] | '\'"';
fragment VALID_SEQUENCE: ~[\r\n\f\\'"];

//NUMBER
NUMBER_LIT: DIGIT+ (DECIMAL | DECIMAL? EXPONENT?);

fragment DIGIT: [0-9];
fragment SIGN: [+-];
fragment EXPONENT: [eE] SIGN? DIGIT+;
fragment DECIMAL: '.' DIGIT*;

//BOOLEAN
BOOL_LIT: TRUE | FALSE;

// NEWLINE COMMENTS WS
NEWLINE: [\n]; // 
COMMENTS: '##' ~[\n\r\f]*; // Comments
WS : [ \t\r]+ -> skip ; // skip spaces, tabs


// TODO ERROR
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' (VALID_SEQUENCE | VALID_ESCAPE)* ('\r\n' | '\n' | EOF) { raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE: '"' ( (VALID_SEQUENCE | VALID_ESCAPE)? INVALID_ESCAPE )* '"' {raise IllegalEscape(self.text[1:])};
fragment INVALID_ESCAPE: '\\' ~[bfrnt'\\] | ~'\\' | ~[']["];



//!  -------------------------- end Lexical structure ------------------- //