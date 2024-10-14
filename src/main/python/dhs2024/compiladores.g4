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

MIN : '<' ;
MINEQ : '<=' ;
MAY : '>' ;
MAYEQ : '>=';
AND : '&&' ; 
OR : '||' ;
NOT : '!=' ;

NUMERO : DIGITO+ ;

INT   : 'int' ;
FLOAT : 'float';
BOOLEAN : 'bool';
DOUBLE : 'double';
CHAR : 'char';
VOID : 'void';
WHILE : 'while' ;
FOR   : 'for' ;
IF    : 'if' ;

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

WS : [ \t\n\r] -> skip;
// OTRO : . ;

// s : ID     {print("ID ->" + $ID.text + "<--") }         s
//   | NUMERO {print("NUMERO ->" + $NUMERO.text + "<--") } s
//   | WHILE  {print("WHILE ->" + $WHILE.text + "<--") }   s
  // | OTRO   {print("Otro ->" + $OTRO.text + "<--") }     s
  // | EOF
  // ;

// si : s EOF ;

// s : PA s PC s
//   |
//   ;

programa : instrucciones EOF ;

instrucciones : instruccion instrucciones
              |
              ;

// instruccion : INST {print($INST.text[:-1])};
instruccion : declaracion
            | iwhile
            // | ifor
            // | iif
            | bloque
            | asignacion PYC
            ;

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


declaracion : tipodato ID PYC;

asignacion : ID ASIG opal ;

opal : exp ; // completar


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

iwhile : WHILE PA ID PC instruccion ;

bloque : LLA instrucciones LLC ;

prototipofunc: tipodatofuncion ID PA argumentos PC PYC;

func: prototipofunc bloque;

argumentos: tipodato ID COMA argumentos
          | tipodato ID
          |
          ;

// ifor : FOR PA init PYC cond PYC iter PC instruccion ;
// init : ;
// cond : ;
// iter : ;


