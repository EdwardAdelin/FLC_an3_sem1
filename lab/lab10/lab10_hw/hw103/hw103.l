%{
#include <stdio.h>
%}

%%

\/\/[^\n]*            { }
\/\*([^*]|\*+[^*/])*\*+\/  { }

.|\n                   { ECHO; }

%%

int main() {
    yylex();
    return 0;
}

int yywrap(){
return 1;

}
