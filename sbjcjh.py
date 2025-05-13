print("Welcome to the Engineering Materials Manager!")

materials = {
    "Steel": {"Density": 7850, "Strength": 250, "Thermal Conductivity": 50},
    "Aluminum": {"Density": 2700, "Strength": 150, "Thermal Conductivity": 205},
    "Copper": {"Density": 8960, "Strength": 210, "Thermal Conductivity": 385}
}

print("1. Add a new material")
print("2. Edit a material property")
print("3. Delete a material")

choice = input("What do you want to do? Pick 1-3: ")

if choice == '1':
    name = input("Enter material name: ")
    density = float(input("Enter density (kg/m³): "))
    strength = float(input("Enter strength (MPa): "))
    conductivity = float(input("Enter thermal conductivity (W/m·K): "))
    materials[name] = {"Density": density, "Strength": strength,
                       "Thermal Conductivity": conductivity}
    print(f"Added {name}!")

elif choice == '2':
    name = input("Enter material name to edit: ")
    if name in materials:
        prop = input(
            "Enter property to edit (Density/Strength/Thermal Conductivity): ")
        if prop in materials[name]:
            new_value = float(input(f"Enter new value for {prop}: "))
            materials[name][prop] = new_value
            print(f"Updated {name}'s {prop}!")
        else:
            print("Invalid property.")
    else:
        print("Material not found.")

elif choice == '3':
    name = input("Enter material name to delete: ")
    if name in materials:
        del materials[name]
        print(f"Deleted {name}!")
    else:
        print("Material not found.")
else:
    print("Invalid choice, try again.")
1
