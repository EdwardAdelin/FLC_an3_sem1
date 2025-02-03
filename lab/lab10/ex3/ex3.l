%{
#include <stdio.h>
#include <string.h>

FILE *output;
%}

%%

new    { fprintf(output, "old"); }
[^ \t\n]+ { fprintf(output, "%s", yytext); }

%%

int yywrap() {
    return 1;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (input == NULL) {
        perror("Error opening input file");
        return 1;
    }

    output = fopen("output.txt", "w");
    if (output == NULL) {
        perror("Error opening output file");
        fclose(input);
        return 1;
    }

    yyin = input;

    yylex();

    fclose(input);
    fclose(output);

    return 0;
}
