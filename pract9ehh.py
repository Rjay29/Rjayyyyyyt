from abc import ABC, abstractmethod  # TODO: 1

# TODO: 2. Declare an abstract class named Appliance


class Appliance(ABC):

    def __init__(self, brand):
        self.brand = brand

    # TODO: 3. Define an abstract method named `operate`
    @abstractmethod
    def operate(self):
        pass

    def display_brand(self):  # TODO: 4
        print(f"Brand: {self.brand}")


# TODO: 5. Declare a subclass of Appliance named WashingMachine
class WashingMachine(Appliance):

    def __init__(self, brand, capacity):
        super().__init__(brand)  # TODO: 6
        self.capacity = capacity  # TODO: 7

    def operate(self):  # TODO: 8
        print(f"The {self.capacity}kg washing machine is washing clothes.")


# TODO: 9. Declare a subclass of Appliance named Refrigerator
class Refrigerator(Appliance):

    def __init__(self, brand, volume):
        super().__init__(brand)  # TODO: 10
        self.volume = volume  # TODO: 11

    def operate(self):  # TODO: 12
        print(f"The {self.volume}L refrigerator is cooling food.")


# TODO: 13. Declare a subclass of Appliance named Microwave
class Microwave(Appliance):

    def __init__(self, brand, power_level):
        super().__init__(brand)  # TODO: 14
        self.power_level = power_level  # TODO: 15

    def operate(self):  # TODO: 16
        print(f"The {self.power_level}W microwave is heating food.")


# === DRIVER CODE ===
print("Choose an appliance:")
print("1. Washing Machine")
print("2. Refrigerator")
print("3. Microwave")

choice = input("Enter the number of your choice: ")
appliance = None

if choice == "1":
    brand = input("Enter brand of the washing machine: ")
    capacity = input("Enter capacity (kg): ")
    appliance = WashingMachine(brand, capacity)

elif choice == "2":
    brand = input("Enter brand of the refrigerator: ")
    volume = input("Enter volume (liters): ")
    appliance = Refrigerator(brand, volume)

elif choice == "3":
    brand = input("Enter brand of the microwave: ")
    power_level = input("Enter power level (watts): ")
    appliance = Microwave(brand, power_level)  # TODO: 17

else:
    print("Invalid choice.")

# Display the results
if appliance:
    appliance.display_brand()
    appliance.operate()
