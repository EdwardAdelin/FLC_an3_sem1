#include <stdio.h>
#include <string.h>
//search element of array
int searchElement(int arr[], int size, int x) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == x) {
            return 1; // Element found
        }
    }
    return 0; // Element not found
}
//2D arrays adder
void addMatrices(int arr1[2][2], int arr2[2][2], int sum[2][2]) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            sum[i][j] = arr1[i][j] + arr2[i][j];
        }
    }
}
//check if two 2D arrays are equal
int areMatricesEqual(int arr1[2][2], int arr2[2][2]) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            if (arr1[i][j] != arr2[i][j]) {
                return 0; // Not equal
            }
        }
    }
    return 1; // Equal
}
//length of a string
int stringLength(char str[]) {
    int length = 0;
    while (str[length] != '\0') {
        length++;
    }
    return length;
}
//find word and display its index
void searchWord(char str[], char word[]) {
    char *pos = strstr(str, word);
    if (pos != NULL) {
        printf("word '%s' found at index %ld.\n", word, pos - str);
    } else {
        printf("word '%s' not found.\n", word);
    }
}
//palindrome string
int isPalindrome(char str[]) {
    int length = strlen(str);
    for (int i = 0; i < length / 2; i++) {
        if (str[i] != str[length - i - 1]) {
            return 0;
        }
    }
    return 1;
}

int main() {
    // Test Exercise 1
    int arr[] = {1, 2, 3, 4, 5};
    int x = 5;
    if (searchElement(arr, 5, x)) {
        printf("%d present in array.\n", x);
    } else {
        printf("%d not present in array.\n", x);
    }

    // Test Exercise 2
    int arr1[2][2] = {{1, 2}, {3, 4}};
    int arr2[2][2] = {{5, 6}, {7, 8}};
    int sum[2][2];
    addMatrices(arr1, arr2, sum);
    printf("Sum matr.:\n");
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            printf(" %d ", sum[i][j]);
        }
        printf("\n");
    }

    // Test Exercise 3
    if (areMatricesEqual(arr1, arr2)) {
        printf("equal matrices\n");
    } else {
        printf("not equal matrices\n");
    }

    // Test Exercise 4
    char str[] = "Bombastic";
    printf("Length string: %d\n", stringLength(str));

    // Test Exercise 5
    char ex[] = "FILS is part of UNSTPB. I am a student at FILS. Gud lac kido!";
    searchWord(ex, "FILS");

    // Test Exercise 6
    char palindromeStr[] = "pufuleti";
    if (isPalindrome(palindromeStr)) {
        printf("string '%s' is a palindrome.\n", palindromeStr);
    } else {
        printf("string '%s' is not a palindrome.\n", palindromeStr);
    }

    return 0;
}
