// reference solution for CS 425/825 projects
lexer grammar BlaiseLexer;

//
// keywords
//

BEGIN     : 'BEGIN';
CALL      : 'CALL';
DO        : 'DO';
ELSE      : 'ELSE';
END       : 'END';
IF        : 'IF';
PROCEDURE : 'PROCEDURE';
THEN      : 'THEN';
VAR       : 'VAR';
WHILE     : 'WHILE';


//
// separators
//

LPAREN    : '(';
RPAREN    : ')';
COMMA     : ',';
SEMICOLON : ';';
DOT       : '.';


//
// operators
//

MULT   : '*';
DIV    : '/';
PLUS   : '+';
MINUS  : '-';
NE     : '<>';
EQ     : '=';
LT     : '<';
GT     : '>';
LTE    : '<=';
GTE    : '>=';
ASSIGN : ':=';


//
// literals
//

NUMBER
	: [1-9] [0-9]*
	| '0'
	;


//
// identifiers
//

ID
	: [a-zA-Z] [a-zA-Z0-9]*
	;


//
// whitespace
//

WS
	: [ \t\r\n\f]+ -> skip
	;


// a 'match all' class so there are no lexer errors (parser will signal error)
ERR_CHAR
	: .
	;
