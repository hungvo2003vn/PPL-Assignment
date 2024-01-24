grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}


// declared
program: (COMMENTS NEWLINE | NEWLINE)* list_declared EOF;

list_declared: declared list_declared | declared;
declared:  function | variables ignore;

/* Variable declaration */
variables: implicit_var | keyword_var | implicit_dynamic; 
implicit_var: VAR ID ASSIGN expression;
keyword_var: prim_type (ID | array_declared) (ASSIGN expression)?;
implicit_dynamic: DYNAMIC ID (ASSIGN expression)?;
prim_type: BOOL | NUMBER | STRING;

/* array */
array_element: array_element index_operators | (ID | func_call) index_operators;
index_operators: (LBRACKET expression_list RBRACKET);
array_declared: ID (LBRACKET list_NUMBER_LIT RBRACKET);
list_NUMBER_LIT: NUMBER_LIT (COMMA list_NUMBER_LIT) | NUMBER_LIT;

/* function declaration */
function: FUNC ID LPARENT prameters_list? RPARENT (ignore? return_statement | ignore? block_statement | ignore);
prameters_list: prim_type (ID | array_declared) COMMA prameters_list
				| prim_type (ID | array_declared)
				| DYNAMIC ID;

/* Statement */
statement_list: statement statement_list | statement;
statement: declaration_statement | assignment_statement 
            | if_statement | for_statement 
            | break_statement | continue_statement 
            | return_statement  | call_statement | block_statement;

declaration_statement: variables ignore;
assignment_statement: (ID | array_element) ASSIGN expression ignore;

if_statement: (IF expression statement_block_if) (elif_statement_list)? (else_statement)?;
elif_statement: ELIF expression statement_block_if;
elif_statement_list: elif_statement elif_statement_list | elif_statement;
else_statement: ELSE statement_block_if;
statement_block_if: (ignore? statement ignore?);

for_statement: FOR ID UNTIL expression BY expression (ignore statement);
break_statement: BREAK ignore;
continue_statement: CONTINUE ignore;
return_statement: RETURN expression ignore;

call_statement: (
	ID (LPARENT expression_list? RPARENT) | non_returned_func
) ignore;
func_call: ID (LPARENT expression_list? RPARENT) | returned_func;
returned_func: readNumber | readBool | readString;
non_returned_func: writeNumber | write | writeString;
readNumber: 'readNumber' LPARENT RPARENT;
writeNumber: 'writeNumber' LPARENT expression RPARENT;
readBool: 'readBool' LPARENT RPARENT;
write: 'write' LPARENT expression RPARENT;
readString: 'readString' LPARENT RPARENT;
writeString: 'writeString' LPARENT expression RPARENT;

block_statement: BEGIN ignore statement_list? END ignore;


/* Expression */
expression_list: expression COMMA expression_list | expression;
expression: expression1 CONCAT expression1 | expression1;
expression1: expression2 (EQUAL | STRCMP | NOT_EQUAL | LT | GT | LE | GE) expression2 | expression2;
expression2: expression2 (AND | OR) expression3 | expression3;	
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: NOT expression5 | expression6;
expression6: SUB expression6 | expression7;
expression7: expression7 (LBRACKET expression_list RBRACKET) | expression8;
expression8: array_element | literal | ID | (LPARENT expression RPARENT) | func_call;



/* Value */
literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_literal;
array_literal: LBRACKET list_literal? RBRACKET;
list_literal: literal COMMA list_literal | literal;

/* Ignore */
ignore: NEWLINE (COMMENTS NEWLINE | NEWLINE)*;

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