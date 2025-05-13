def print_table():
    numbers = [[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20],
               [21, 22, 23, 24, 25]]

    for row in range(5):
        if row == 0:
            print("+---+---+---+---+---+")
        seperator = "|"

        for column in range(5):
            seperator += f"{numbers[row][column]:3}|"
        print(seperator)

        print("+---+---+---+---+---+")


print_table()

##########

print(f"Item: {'Apples':10} Price: {2.5:>6.3f}")
print(f"Item: {'Oranges':10} Price: {10.75:>6.3f}")

#########

num = 1000000

print(f"You have won {num:,} !!!!")


#######

accuracy = 0.98764
print(f"Accuracy is: {accuracy:.1%}")

########

r = int(input("enter your desired range: "))

for i in range(r + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

########

first_char = input("First character: ")
second_char = input("Second character: ")
size = int(input("Enter size: "))

for i in range(1, size + 1):
    print("-" * (i - 1), end="")
    if i % 2 == 1:
        print(first_char)
    else:
        print(second_char)


############

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")

########

set1 = set(map(int, input("Enter a number: ").split()))
set2 = set(map(int, input("Enter number: ").split()))

add_set = set1.union(set2)
diff_set = set1.difference(set2)
inter = set1.intersection(set2)

print("Add:", add_set)
print("Sub:", diff_set)
print("intersectriion:", inter)

#########


def foobar():
    for num in range(1, 21):
        if num % 4 == 0 and num % 3 == 0:
            print("foobar")
        elif num % 4 == 0:
            print("Foo")
        elif num % 3 == 0:
            print("Bar")
        else:
            print(num)


###########

def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == '+':
        print("Result:", num1 + num2)
    elif op == '-':
        print("Result:", num1 - num2)
    elif op == '*':
        print("Result:", num1 * num2)
    elif op == '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid operation!")


calculator()


###################

for i in range(5):
    if i % 2 == 0:
        print(14 * (i + 1))
    else:
        ans = 14 * (i + 1)
        print(f"\t{ans}")

####################

colors = ['green', 'blue', 'red', 'yellow', 'purple']

for i in range(len(colors)):
    print(" " * i + colors[i])
