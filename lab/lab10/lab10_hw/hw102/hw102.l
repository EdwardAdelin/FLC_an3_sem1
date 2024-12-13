%{
#include <stdio.h>
%}

%%

[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,} {
    printf("Valid email address: %s\n", yytext);
}

. {
    printf("Invalid input: %s\n", yytext);
}

%%

int main() {
    printf("Enter strings to check for email addresses:\n");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}