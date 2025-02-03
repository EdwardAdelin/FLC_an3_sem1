%{
#undef yywrap
#define yywrap() 1
#define YY_INPUT(buf, result, max_size) \
    { \
    int c = getchar(); \
    result = (c == EOF) ? YY_NULL : (buf[0] = c, 1); \
    }

%}

%%

(he|she|it|they|we|I|you|him|her|them|us|me|my|mine|his|hers|its|ours|theirs) {
    printf("'%s' is a pronoun.\n", yytext);
}

(pray|run|sleep|drive|play|eat|cry|write|speak|hit) {
    printf("'%s' is a verb.\n", yytext);
}

(happy|big|small|beautiful|fast|slow|quiet|loud|bright|dark) {
    printf("'%s' is an adjective.\n", yytext);
}

(dog|cat|car|house|tree|book|school|computer|friend|city) {
    printf("'%s' is a noun.\n", yytext);
}

(in|on|at|by|with|under|over|between|through|during) {
    printf("'%s' is a preposition.\n", yytext);
}

[0-9] { 
    printf("'%s' is a digit.\n", yytext);
}

[aAeEiIoOuU]   { printf("The letter '%c' is a vowel.\n", yytext[0]); }

.               { /* Ignore other characters or print them as not matching */ }

%%

int main() {
    yylex();
    return 0;
}