grammar ZCode;

@lexer::header {
## MSSV: 2113623
from lexererr import *
}

options {
	language=Python3;
}


// declared
program: NEWLINE* list_declared EOF;

list_declared: declared list_declared | declared;
declared:  function | variables ignore;

/* Variable declaration */
variables: implicit_var | keyword_var | implicit_dynamic; 
implicit_var: VAR ID ASSIGN expression;
keyword_var: prim_type (ID | array_declared) (ASSIGN expression)?;
implicit_dynamic: DYNAMIC ID (ASSIGN expression)?;
prim_type: BOOL | NUMBER | STRING;

/* array declaration */
array_declared: ID (LBRACKET list_NUMBER_LIT RBRACKET);
list_NUMBER_LIT: NUMBER_LIT (COMMA list_NUMBER_LIT) | NUMBER_LIT;

/* function declaration */
function: FUNC ID LPARENT prameters_list? RPARENT (ignore? return_statement | ignore? block_statement | ignore);
prameters_list: prim_type (ID | array_declared) COMMA prameters_list
				| prim_type (ID | array_declared);

/* Statement */
statement_list: statement statement_list | ;
statement: declaration_statement | assignment_statement 
            | if_statement | for_statement 
            | break_statement | continue_statement 
            | return_statement  | call_statement | block_statement;

declaration_statement: variables ignore;
assignment_statement: (ID | ID index_operators) ASSIGN expression ignore;

if_statement: (IF LPARENT expression RPARENT statement_block_if) (elif_statement_list)? (else_statement)?;
elif_statement: ELIF LPARENT expression RPARENT statement_block_if;
elif_statement_list: elif_statement elif_statement_list | elif_statement;
else_statement: ELSE statement_block_if;
statement_block_if: (ignore? statement ignore?);

for_statement: FOR ID UNTIL expression BY expression (ignore? statement);
break_statement: BREAK ignore;
continue_statement: CONTINUE ignore;
return_statement: RETURN (expression | ) ignore;

call_statement: func_call ignore;
func_call: ID (LPARENT expression_list? RPARENT);

block_statement: BEGIN ignore statement_list END ignore;


/* Expression */
expression_list: expression COMMA expression_list | expression;
expression: expression1 CONCAT expression1 | expression1;
expression1: expression2 (EQUAL | STRCMP | NOT_EQUAL | LT | GT | LE | GE) expression2 | expression2;
expression2: expression2 (AND | OR) expression3 | expression3;	
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: NOT expression5 | expression6;
expression6: SUB expression6 | expression7;
expression7: array_element | literal | ID | (LPARENT expression RPARENT) | func_call;



/* Value */
literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_literal;
array_literal: LBRACKET expression_list RBRACKET;
array_element: (ID | func_call) index_operators;
index_operators: (LBRACKET expression_list RBRACKET);

/* Ignore */
ignore: NEWLINE+;

//! -------------------------- end Syntax analysis ----------------------- //

//! --------------------------  Lexical structure ----------------------- //

/* KeyWord */
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

/* Operators */
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

/* Separators */
LBRACKET: '[';
RBRACKET: ']';
LPARENT: '(';
RPARENT: ')';
COMMA: ',';

/* Identifiers */
ID: [a-zA-Z_][a-zA-Z0-9_]*;


/* Literal */
// STRING
STRING_LIT: '"'(VALID_SEQUENCE | VALID_ESCAPE)* '"'{self.text = self.text[1:-1];};
fragment VALID_ESCAPE: '\\' [bfrnt'\\] | '\'"';
fragment VALID_SEQUENCE: ~[\r\n\f\\"];

//NUMBER
NUMBER_LIT: DIGIT+ (DECIMAL | DECIMAL? EXPONENT?);

fragment DIGIT: [0-9];
fragment SIGN: [+-];
fragment EXPONENT: [eE] SIGN? DIGIT+;
fragment DECIMAL: '.' DIGIT*;

//BOOLEAN
BOOL_LIT: TRUE | FALSE;

// NEWLINE COMMENTS WS
NEWLINE: [\n]; // Newline
COMMENTS: '##' ~[\n\r\f]* -> skip; // Comments
WS : [ \t\r]+ -> skip ; // skip spaces, tabs


/* ERROR */
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' (VALID_SEQUENCE | VALID_ESCAPE)* ('\r\n' | '\n' | EOF) { 
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[1:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"' (VALID_SEQUENCE | VALID_ESCAPE)* INVALID_ESCAPE {raise IllegalEscape(self.text[1:])};
fragment INVALID_ESCAPE: [\r\f\\] | '\\' ~[bfrnt'\\];



//!  -------------------------- end Lexical structure ------------------- //