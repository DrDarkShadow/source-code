// Function to add two numbers
function add(a, b) {
    return a + b;
}

// Function to calculate factorial
function factorial(n) {
    return n <= 1 ? 1 : n * factorial(n - 1);
}

// Function to greet a person
function greet(name) {
    console.log(`Hello, ${name}!`);
}

// Example usage
console.log("Sum:", add(5, 10));
console.log("Factorial:", factorial(5));
greet("Prateek");
