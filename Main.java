public class Main {



    
    // Function to add two numbers
    public static int add(int a, int b) {
        return a + b;
    }

    // Function to find factorial of a number
    public static int factorial(int n) {
        if (n <= 1)
            return 1;
        else
            return n * factorial(n - 1);
    }

    // Function to print a greeting message
    public static void greet(String name) {
        System.out.println("Hello, " + name + "!");
    }

    public static void main(String[] args) {
        System.out.println("Sum: " + add(5, 10));
        System.out.println("Factorial: " + factorial(5));
        greet("Prateek");
    }
}
