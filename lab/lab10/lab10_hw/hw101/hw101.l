%{
#include <stdio.h>

%}

%%

(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/[0-9]{4} {
    printf("Valid date format: %s\n", yytext); 
}

.|\n { 
    /* Ignoră caracterele care nu sunt parte din formatul datei */
}

%%

int main() {
    printf("Enter a date (DD/MM/YYYY): ");
    yylex();
    return 0;
}
int yywrap() {
    return 1;  // Returnează 1 pentru a semnala că procesarea a fost terminată.
}

