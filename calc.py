def Add(a, b):
    return a + b


def Sub(a, b):
    return a - b


def Mul(a, b):
    return a * b


def Div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("The integer cannot be divided by zero!")


Calc = {"add": Add, "sub": Sub, "mul": Mul, "div": Div}


try:
    operation = input("Choose operation (add, sub, mul, div): ").strip()
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))

    if operation in Calc:
        result = Calc[operation](first, second)
        print(f"Result: {result}")
    else:
        print("Invalid operation.")

except ValueError:
    print("Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")
