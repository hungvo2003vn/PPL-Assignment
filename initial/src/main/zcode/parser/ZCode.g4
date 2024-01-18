grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

// program: EOF;

// declared
program: list_declared EOF;

list_declared: declared list_declared | declared;

declared:  VAR ID ASSIGN expression NEWLINE | ignore;

/* Variable declaration */
array_element: ID (LBRACKET expression_list RBRACKET);

/* Statement */
func_call: ID (LPARENT expression_list? RPARENT);

//TODO hiện thực phần Expression và Value dùng cách viết đệ quy
//* cuối của expression bao gồm ID, literal, (), gọi hàm   */

//! Expression
expression_list: expression COMMA expression_list | expression;
expression: expression1 CONCAT expression1 | expression1;
expression1: expression2 (EQUAL | STRCMP | NOT_EQUAL | LT | GT | LE | GE) expression2 | expression2;
expression2: expression2 (AND | OR) expression3 | expression3;	
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: NOT expression5 | expression6;
expression6: SUB expression6 | expression7;
expression7: expression7 (LBRACKET expression_list RBRACKET) | expression8;
expression8: literal | ID | (LPARENT expression RPARENT) | func_call;



//! Value
literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_literal;
array_literal: LBRACKET expression_list? RBRACKET;


// kí tự bỏ qua
ignore: (COMMENTS | NEWLINE)+;


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
UNCLOSE_STRING: '"' (VALID_SEQUENCE | VALID_ESCAPE)* ('\r\n' | '\n' | EOF) { 
	tmp = self.text[1:].split("\n")[0]
	tmp = tmp.split("\r")[0]
	self.text = tmp
	raise UncloseString(self.text)
};
ILLEGAL_ESCAPE: '"' (VALID_SEQUENCE | VALID_ESCAPE)* INVALID_ESCAPE {raise IllegalEscape(self.text[1:])};
fragment INVALID_ESCAPE: '\\' ~[bfrnt'\\] | ~'\\' | [']~["];



//!  -------------------------- end Lexical structure ------------------- //