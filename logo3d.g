grammar logo3d;

root : func+ EOF ;

func : PROC VAR '(' ( | asig ( ',' asig)*) ')' IS blInstr END ;

blInstr : instr+ ;

instr : 
    VAR EQ asig                                                 #Asignacio
    | IN VAR                                                    #Entrada
    | OUT asig                                                  #Sortida
    | IF cond THEN blInstr ( | ELSE blInstr) END                #BlocIfElse
    | WHILE cond DO blInstr END                                 #BlocWhile
    | FOR VAR FROM asig TO asig DO blInstr END                  #BlocFor
    | VAR '(' ( | asig (',' asig)*) ')'                         #Funcions
    | instrTurtle                                               #Tortuga
    ;
    
asig :
    asig ('*' | '/') asig       #MultDiv
    | asig ('+' | '-') asig     #SumaResta
    |'(' asig ')'               #Parentesi
    | VAR                       #Variable
    | INT                       #Valor
    ;

cond : 
    asig '==' asig              #Igual
    | asig '!=' asig            #Diferent
    | asig '<' asig             #Menysque
    | asig '>' asig             #Mesque
    | asig '<=' asig            #MenysEq
    | asig '>=' asig            #MesEq
    ;
    
instrTurtle :
    'color' '(' asig ',' asig ',' asig ')'  #Color
    | 'left' '(' asig ')'                   #Left
    | 'right' '(' asig ')'                  #Right
    | 'up' '(' asig ')'                     #Up
    | 'down' '(' asig ')'                   #Down
    | 'forward' '(' asig ')'                #Forward
    | 'backward' '(' asig ')'               #Backward
    | 'hide' '(' ')'                        #Hide
    | 'show' '(' ')'                        #Show
    | 'home' '(' ')'                        #Home
    | 'radius' '(' asig ')'                 #Radius
    ;
    
    
EQ : ':=' ;
IN : '>>' ;
OUT : '<<' ;
IF : 'IF' ;
THEN : 'THEN' ;
ELSE : 'ELSE' ;
WHILE: 'WHILE' ;
FOR: 'FOR' ;
FROM: 'FROM' ;
TO: 'TO' ;
DO: 'DO' ;
PROC: 'PROC' ;
IS: 'IS' ;
END: 'END' ;

INT: [0-9]+ ('.' [0-9]+)? ;
VAR : [a-zA-Z0-9_]+ ;

CMT: '//' ~ [\r\n]* -> skip;
WS : [ \n\r]+ -> skip;
