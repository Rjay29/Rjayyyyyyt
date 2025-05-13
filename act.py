def fibonacci(n):
    if n < 0:
        return "Invalid input. Please enter a non-negative integer."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def squared_fibonacci(n):
    return fibonacci(n) ** 2


num = int(input("Enter a position: "))

if num < 0:
    print("Invalid input. Please enter a non-negative integer.")
else:
    print(f"Fibonacci number at position {num}: {fibonacci(num)}")
    print(f"Squared Fibonacci of {num}: {squared_fibonacci(num)}")
