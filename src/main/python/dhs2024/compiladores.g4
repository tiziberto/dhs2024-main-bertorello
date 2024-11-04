grammar compiladores;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

// INST : (LETRA | DIGITO | [- ,;{}()+=>] )+ '\n' ;

PA  : '(' ;
PC  : ')' ;
LLA : '{' ;
LLC : '}' ;
PYC : ';' ;
COMA : ',';
SUMA  : '+' ;
RESTA : '-' ;
MULT  : '*' ;
DIV   : '/' ;
MOD   : '%' ;

ASIG  : '=' ;
IGUAL : '==' ;
DISTINTO : '!=';
MIN : '<' ;
MINEQ : '<=' ;
MAY : '>' ;
MAYEQ : '>=';
AND : '&&' ; 
OR : '||' ;
NOT : '!' ;

NUMERO : DIGITO+ ;

INT   : 'int' ;
FLOAT : 'float';
BOOLEAN : 'bool';
DOUBLE : 'double';
CHAR : 'char';
STRING : 'String';
VOID : 'void';
WHILE : 'while' ;
FOR   : 'for' ;
IF    : 'if' ;
RETURN : 'return';
ELSE : 'else';

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

// Espacios en blanco
  WS : [ \t\n\r] -> skip;
  OTRO : . ;

  s : ID     {print("ID ->" + $ID.text + "<--") }         s
     | NUMERO {print("NUMERO ->" + $NUMERO.text + "<--") } s
     | WHILE  {print("WHILE ->" + $WHILE.text + "<--") }   s
     | OTRO   {print("Otro ->" + $OTRO.text + "<--") }     s
     | EOF
     ;

// si : s EOF ;

// s : PA s PC s
//   |
//   ;

programa : instrucciones EOF ;

// instruccion : INST {print($INST.text[:-1])};

tipodatofuncion:INT
              | DOUBLE
              | FLOAT
              | BOOLEAN
              | CHAR
              | VOID
              ;

tipodato: INT
        | DOUBLE
        | FLOAT
        | BOOLEAN
        | CHAR
        ;


declaracion : tipodato ID (COMA ID)*;

//listaDeclaraciones 
//    : ID (ASIG opal)? (COMA ID (ASIG opal)?)* ;

instruccion : declaracion PYC
            | iwhile
            | ifor
            | iif
            | bloque
            | asignacion PYC
            | func
            | return_call PYC
            | prototipofunc
            | llamadaFunc PYC
            ;

instrucciones : instruccion (instrucciones)*
              ;

asignacion : ID ASIG opal
           | ID ASIG llamadaFunc
           ;

llamadaFunc : ID PA listaExp PC ; 
listaExp : opal lista_parametros;
lista_parametros : COMA opal lista_parametros;



opal : exp 
     | exp operador exp
     ;


exp : term e ;

e   : SUMA  term e
    | RESTA term e
    |
    ;


term : factor t ;

t    : MULT factor t
     | DIV  factor t
     | MOD  factor t
     |
     ;

factor : NUMERO
       | ID
       | PA exp PC
       ;

iwhile : WHILE PA opal PC bloque
       ;

ifor : FOR PA init PYC opal PYC iteracion PC bloque;

init: ID ASIG NUMERO;
iteracion: asignacion
         | incremento
         | decremento
         ;

iif :  IF PA opal PC bloque
    |  IF PA opal PC bloque else
    ;

else : ELSE bloque
     | ELSE iif
     |
     ;

return_call : RETURN opal;

bloque : LLA instrucciones LLC ;

operador: DISTINTO 
        | IGUAL
        | MAY
        | MAYEQ
        | MINEQ
        | MIN
        ;

condicionales : '=='
              | '<'
              | '>'
              | '<='
              | '>='
              ;

iter : ID e;


prototipofunc: tipodatofuncion ID PA argumentos PC PYC;

func : tipodatofuncion ID PA argumentos PC bloque ;

argumentos: tipodato ID COMA argumentos
          | tipodato ID
          |
          ;

incremento: ID SUMA SUMA
          | SUMA SUMA ID
          ;
decremento: ID RESTA RESTA
          | RESTA RESTA ID
          ;