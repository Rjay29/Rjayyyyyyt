# List to store materials
materials = []


def add_material():
    # Collect material details and store in a dictionary
    material = {
        "Name": input("Enter material name: "),
        "Type": input("Enter material type: "),
        "Usage": input("Enter material usage: "),
        "Source": input("Enter material source: "),
        "Supplier": input("Enter material supplier: "),
        "Year": input("Enter manufacturing year: ")
    }

    # Add to the list
    materials.append(material)

    # Show the table automatically
    display_table()


def display_table():
    print("\nEnhanced Material Information Log")
    print(f"{'Material Name':<20}|{'Type':<20}|{'Usage':<20}|{'Source':<20}|{'Supplier':<20}|{'Manufacturing Year':<20}")
    print("." * 125)

    for mat in materials:
        print(f"{mat['Name']:<20}|{mat['Type']:<20}|{mat['Usage']:<20}|{mat['Source']:<20}|{mat['Supplier']:<20}|{mat['Year']:<20}")


# Call function once to input data and show the table
add_material()
