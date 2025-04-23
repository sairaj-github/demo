def fibonacci(n):
    if n <= 0:
        return "Input must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Print Fibonacci series up to n terms
def print_fibonacci_series(terms):
    if terms <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci series:")
        for i in range(1, terms + 1):
            print(fibonacci(i), end=" ")

# Example usage
n_terms = int(input("Enter the number of terms: "))
print_fibonacci_series(n_terms)

# Fibonacci series using a for loop
def fibonacci_series_for_loop(terms):
    if terms <= 0:
        print("Please enter a positive integer.")
        return
    a, b = 0, 1
    print("\nFibonacci series using for loop:")
    for _ in range(terms):
        print(a, end=" ")
        a, b = b, a + b

# Example usage
fibonacci_series_for_loop(n_terms)