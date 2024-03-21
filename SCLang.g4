// Filename: SCLang.g4
grammar SCLang;

script         	: definition* ;

definition    	: conditionBlock? visibility actionBlock effectBlock? metaData?;

conditionBlock	: '@' logicExpr ;
visibility	: 'pub' | 'priv' ;
actionBlock	: entityGroup '.' method argsWrapper ;
effectBlock	: '->' logicExpr ;
metaData	: '{' metaBlock? '}' ;

logicExpr	: modifier? logicTerm ;
logicTerm	: attrib comparison? | '!' liveTerm '!' | '[' logicGroup? ']' ;
logicGroup	: logicOr ;
logicOr		: logicAnd ('|' logicAnd)* ;
logicAnd	: logicExpr ('&' logicExpr)* ;
liveTerm	: attrib comparison? | '[' logicGroup ']' ;
modifier	: '~' | '$' ;

comparison	: compareOp attrib (compareOp attrib)? ;
compareOp	: '!=' | '<' | '<=' | '>' | '>=' | '==' ;

entityRef	: entity | entityGroup ;
entityGroup	: '{' entityDef ('|' logicExpr)? '}' ;
entityDef	: entityType ':' entity ;
entityType      : entityClass | entityVariable | entityConstant ;
entityClass     : 'ent' '(' IDENTIFIER ')' ;
entityVariable  : 'var' '(' dataType ')' ;
entityConstant  : 'const' '(' dataType ')' ;
dataType	: 'Bool' | 'Float' | 'Int' | 'String' ;

attrib		: entityRef methodCall? ;
methodCall	: '.' method argsWrapper? ;
argsWrapper	: '(' argsList ')' ;
argsList	: argument (',' argument)* ;
argument	: logicExpr ;

metaBlock	: metaEntry (',' metaEntry)* ','? ;
metaEntry	: STRING ':' value ;
value		: NUMBER | STRING | 'True' | 'False' ;

entity		: IDENTIFIER ;
method		: IDENTIFIER ;

// Lexer rules
IDENTIFIER  	: [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER      	: [0-9]+ ('.' [0-9]+)? ;
STRING      	: '"' ( ~["\\] | '\\' . )* '"';
WS          	: [ \t\r\n]+ -> skip ; // Skip whitespace
COMMENT     	: '//' (~[ \r\n])* -> skip ; // Single-line comments
