%{
#include <stdio.h>
#include <stdlib.h>
%}

/* Regex */
url     ((http|https):\/\/|www\.)[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)+(:[0-9]+)?(\/[^\s]*)?

%%
{url}   { printf("Valid URL: %s\n", yytext); }
.|\n    { printf("Invalid input: %s\n", yytext); }
%%

int main() {
    printf("Enter a string to check if it is a valid URL:\n");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
