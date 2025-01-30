r = int(input("enter your desired range: "))

for i in range(r + 1):
    if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")  # prints "FizzBuzz"
    elif i % 3 == 0:
      print("Fizz")  # prints "Fizz"
    elif i % 5 == 0:
      print("Buzz")  # prints "Buzz"
    else:
      print(i)  # prints the number