class Number:
    # constructor method to initialize the value
    # 1. constructor method
    # __init__ is a special method that is called when an object is created
    # self is a reference to the current instance of the class
    # it allows you to access the attributes and methods of the class in python
    # __value is a private attribute, it can only be accessed within the class
    # it is a convention to use double underscore before the attribute name to make it private
    # private attributes are not accessible from outside the class
    # this is a way to implement encapsulation in python
    # encapsulation is a way to restrict access to certain parts of an object
    # and to protect the integrity of the object
    # encapsulation is one of the four pillars of OOP (Object Oriented Programming)
    # the four pillars of OOP are: encapsulation, inheritance, polymorphism, and abstraction
    def __init__(self, value):
        self.__value = value

    # Getter method for value
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    @property
    def sign(self):
        if self.__value > 0:
            return "positive"
        elif self.__value < 0:
            return "negative"
        else:
            return "zero"

    # 2. property
    @property
    def parity(self):
        return "even" if self.__value % 2 == 0 else "odd"

    @property
    def primality(self):
        if self.__value <= 1:
            return "niether"
        for i in range(2, int(abs(self.__value) ** 0.5) + 1):
            if self.__value % i == 0:
                return "composite"
        return "prime"

    # dunder str how to show your object as a string

    def __str__(self):
        return (f"value: {self.value}, Sign: {self.sign}, "
                f"Parity: {self.parity}, Primality: {self.primality}")


# Get input from the user
try:
    user_input = int(input("Enter a number: "))
    num = Number(user_input)
    print(num)

    # Ask if the user wants to modify the value
    while True:
        response = input("\nChange the value? (y/n): ").strip().lower()
        if response == "y":
            new_value = int(input("Enter a new number: "))
            num.value = new_value
            print(num)
        elif response == "n":
            print("Thank you!")
            break
        else:
            print("Enter a valid response (y/n).")

except ValueError:
    print("Invalid input. Please enter a valid number.")
