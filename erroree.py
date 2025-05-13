def get_user_choice():
    valid_choices = [1, 2, 3, 4, 5]
    
    try:
        choice = int(input("Pick a number between 1 and 5: "))
        if choice in valid_choices:
            print(f"You chose {choice}. Good choice!")
        else:
            print("Warning: That number is not in the allowed choices (1-5). Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")

get_user_choice()