#include <stdio.h>

// Function to add two numbers
int add(int a, int b) {
    return a + b;
}

// Function to calculate factorial
int factorial(int n) {
    if (n <= 1)
        return 1;
    else
        return n * factorial(n - 1);
}

// Function to print a greeting
void greet(char name[]) {
    printf("Hello, %s!\n", name);
}

int main() {
    printf("Sum: %d\n", add(5, 10));
    printf("Factorial: %d\n", factorial(5));
    greet("Prateek");
    return 0;
}
