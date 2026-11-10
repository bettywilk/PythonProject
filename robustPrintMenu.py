'''
Here is a simple, robust Python program to create a menu-driven application. This program demonstrates how to display a menu, take user input, and
execute corresponding actions.
'''
def option_one():
    print("You selected Option 1: Perform Action 1.")

def option_two():
    print("You selected Option 2: Perform Action 2.")

def option_three():
    print("You selected Option 3: Perform Action 3.")

def display_menu():
    print("\n=== Main Menu ===")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")

def main():
    while True:
        display_menu()
        # Get user input
        choice = int(input("Enter your choice (1-4): "))

        # Handle menu options
        if choice == 1:
            option_one()
        elif choice == 2:
            option_two()
        elif choice == 3:
            option_three()
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break
        else:
             print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
