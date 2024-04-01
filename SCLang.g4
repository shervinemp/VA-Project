// Filename: SCLang.g4
grammar SCLang;

script         	: definition* ;
definition    	: conditionBlock? visibility actionBlock effectBlock? metaData? ;

conditionBlock	: '@' logicExpr ;
visibility	: 'pub' | 'priv' ;
actionBlock	: entityGroup '.' method argsWrapper ;
effectBlock	: '->' logicExpr ;
metaData	: '{' metaBlock? '}' ;

logicExpr	: logicMod? logicTerm ;
logicTerm	: attrib comparison? | '[' logicGroup? ']' ;
logicGroup	: logicOr ;
logicOr		: logicAnd ('|' logicAnd)* ;
logicAnd	: logicExpr ('&' logicExpr)* ;
logicMod	: '~' ;

comparison	: compareOp attrib ;
compareOp	: '!=' | '<' | '<=' | '>' | '>=' | '==' ;

entityRef	: entity | entityGroup ;
entityGroup	: '{' entityDef ('|' logicExpr)? '}' ;
entityDef	: entityType ':' entity ;
entityType      : entityClass | entityVar ;
entityClass     : 'ent' '(' IDENTIFIER ')' ;
entityVar	: 'var' '(' dataType ')' ;
dataType	: 'Bool' | 'Float' | 'Int' | 'String' ;

attrib		: attribMod? entityRef methodCall? ;
methodCall  : '.' method argsWrapper? ;
attribMod	: '$' | '!' ;
argsWrapper	: '(' argsList ')' ;
argsList	: argument (',' argument)* ;
argument	: logicExpr ;

metaBlock	: metaEntry (',' metaEntry)* ','? ;
metaEntry	: string ':' value ;

value		: number | string | bool ;
number		: NUMBER ;
string		: STRING ;
bool		: 'True' | 'False' ;

entity		: IDENTIFIER ;
method		: IDENTIFIER ;

// Lexer rules
IDENTIFIER  	: [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER      	: [0-9]+ ('.' [0-9]+)? ;
STRING      	: '"' ( ~["\\] | '\\' . )* '"';
WS          	: [ \t\r\n]+ -> skip ; // Skip whitespace
COMMENT     	: '//' (~[ \r\n])* -> skip ; // Single-line comments
MACRO		: '#' (~[ \r\n])* -> skip ;
