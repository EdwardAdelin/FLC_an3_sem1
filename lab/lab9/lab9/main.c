#include <stdio.h>
#include <stdlib.h>
//add 2 num
void addWithPointers() {
    int a, b, sum;
    int *p1 = &a, *p2 = &b;
    printf("Ex1: Enter two numbers for summing up: ");
    scanf("%d %d", p1, p2);
    sum = *p1 + *p2;
    printf("Sum (using pointers): %d\n", sum);
}
// tãte operatii Pamantului
void computeOperations() {
    float num1, num2;
    printf("Enter two numbers for all calculations on Earth: ");
    scanf("%f %f", &num1, &num2);
    printf("Sum: %.2f\n", num1 + num2);
    printf("Difference: %.2f\n", num1 - num2);
    printf("Multiplication: %.2f\n", num1 * num2);
    if (num2 != 0) {
        printf("Division: %.2f\n", num1 / num2);
    } else {
        printf("Division: Sorry bro, can't make it (division by zero)\n");
    }
    printf("Mean: %.2f\n", (num1 + num2) / 2);
}
// even\odd checker
void checkEvenOdd(int num) {
    if (num % 2 == 0) {
        printf("%d is even.\n", num);
    } else {
        printf("%d is odd.\n", num);
    }
}
// square of a number
int computeSquare(int num) {
    return num * num;
}
// create, write, and read a text file
void fileOperations() {
    FILE *file;
    char filename[] = "output.txt";
    char text[100];
    //open, write
    file = fopen(filename, "w");
    if (file == NULL) {
        printf("Error opening file for writing.\n");
        return;
    }
    printf("Enter text to write to the file (type 'END' to finish):\n");
    while (1) {
        fgets(text, sizeof(text), stdin);
        if (strcmp(text, "END\n") == 0) break;
        fputs(text, file);
    }
    fclose(file);
    printf("File written successfully.\n");

    // read,print
    file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error opening file for reading.\n");
        return;
    }
    printf("\nContent of the file:\n");
    while (fgets(text, sizeof(text), file) != NULL) {
        printf("%s", text);
    }
    fclose(file);
}
//
int main() {
    int num;
    //
    addWithPointers();
    //
    computeOperations();
    //
    printf("\n--- Check Even or Odd Exercise---\n");
    printf("Enter a number: ");
    scanf("%d", &num);
    checkEvenOdd(num);
    //
    printf("\n--- Task 4: Square of a Num. ---\n");
    printf("Enter the number: ");
    scanf("%d", &num);
    printf("Square: %d\n", computeSquare(num));
    printf("Square (2nd call): %d\n", computeSquare(num));
    //
    printf("\n--- Task 5: File Operations ---\n");
    getchar(); // Clear buffer before file operations
    fileOperations();

    return 0;
}
