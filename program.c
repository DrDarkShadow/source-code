#include <stdio.h>
#include <stdbool.h>

// Function to find the maximum element in an array
int findMax(int arr[], int size) {
    int max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max)
            max = arr[i];
    }
    return max;
}

// Function to calculate the length of a string manually
int stringLength(char str[]) {
    int length = 0;
    while (str[length] != '\0') {
        length++;
    }
    return length;
}

// Function to check if a number is prime
bool isPrime(int n) {
    if (n <= 1)
        return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main() {
    int nums[] = {5, 12, 3, 19, 7};
    int size = sizeof(nums) / sizeof(nums[0]);
    
    printf("Maximum number: %d\n", findMax(nums, size));
    
    char name[] = "Prateek";
    printf("Length of '%s': %d\n", name, stringLength(name));
    
    int number = 17;
    if (isPrime(number))
        printf("%d is a prime number.\n", number);
    else
        printf("%d is not a prime number.\n", number);

    return 0;
}
