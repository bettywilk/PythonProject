import random

# Global game state variables
miles_to_go = 2000
food_supply = 500  # in pounds
health = 5  # out of 5
current_day = 1
party_members = ["You", "Sarah", "John"] # Example party members

def display_status():
    """Prints the current game status."""
    print(f"\n--- Day {current_day} Status ---")
    print(f"Miles to Oregon: {miles_to_go}")
    print(f"Food Supply: {food_supply} lbs")
    print(f"Health: {health}/5")
    print(f"Party Members: {', '.join(party_members)}")
    print("-------------------------")

def travel():
    """Simulates traveling on the trail."""
    global miles_to_go, food_supply, current_day, health

    miles_traveled = random.randint(30, 60)
    days_passed = random.randint(3, 7)
    food_consumed = len(party_members) * 5 * days_passed # 5 lbs per person per day

    miles_to_go -= miles_traveled
    food_supply -= food_consumed
    current_day += days_passed

    print(f"\nYou traveled {miles_traveled} miles over {days_passed} days.")
    print(f"Food consumed: {food_consumed} lbs.")

    # Random events during travel
    if random.random() < 0.1: # 10% chance of illness
        health -= 1
        print("One of your party members fell ill! Health decreased.")
    if random.random() < 0.05 and food_supply < 100: # 5% chance of finding food if low
        found_food = random.randint(20, 50)
        food_supply += found_food
        print(f"You found {found_food} lbs of food!")

def rest():
    """Simulates resting to regain health."""
    global health, current_day
    days_rested = random.randint(2, 5)
    health_gained = 1 if health < 5 else 0 # Max health is 5

    health = min(5, health + health_gained)
    current_day += days_rested

    print(f"\nYou rested for {days_rested} days.")
    if health_gained > 0:
        print("Your party feels more refreshed. Health increased.")

def hunt():
    """Simulates hunting for food."""
    global food_supply, current_day
    days_hunting = random.randint(2, 5)
    food_hunted = random.randint(80, 120)

    food_supply += food_hunted
    current_day += days_hunting

    print(f"\nYou spent {days_hunting} days hunting and gathered {food_hunted} lbs of food.")

def check_game_over():
    """Checks for game over conditions."""
    if health <= 0:
        print("\nYour party's health dropped to zero. Game Over!")
        return True
    if food_supply <= 0:
        print("\nYou ran out of food. Your party starved. Game Over!")
        return True
    if current_day > 365 and miles_to_go > 0: # Example: End of year, not reached destination
        print("\nWinter arrived before you reached Oregon. Game Over!")
        return True
    return False

def check_win():
    """Checks for winning condition."""
    if miles_to_go <= 0:
        print("\nCongratulations! You reached Oregon!")
        return True
    return False

def main_game_loop():
    """Main loop for the Oregon Trail game."""
    print("Welcome to the Python Trail!")
    print("Your goal is to reach Oregon before winter sets in!")

    while not check_game_over() and not check_win():
        display_status()
        print("\nWhat would you like to do?")
        print("1. Travel")
        print("2. Rest")
        print("3. Hunt")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            travel()
        elif choice == '2':
            rest()
        elif choice == '3':
            hunt()
        elif choice == '4':
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_game_loop()