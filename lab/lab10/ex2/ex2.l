%{
#include <stdio.h>

int line_number = 1;  // Initialize line counter
%}

%%

^(.*)$ { 
    // Match a line and its content
    printf("%d: %s\n", line_number++, yytext);
}

.|\n { /* Ignore unmatched characters */ }

%%

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    // Open the file for reading
    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("Error opening file");
        return 1;
    }

    // Assign the input stream to FLEX
    yyin = file;

    // Start processing
    yylex();

    fclose(file);  // Close the file
    return 0;
}

int yywrap() {
    return 1;
}
