secNumber = 6
userGuess = int(input("enter a guess between 1 and 10: "))
while(userGuess > 10 or userGuess < 1):
    userGuess = int(input("Guess not valid please enter another guess "))

while(userGuess != secNumber):
    if(userGuess < secNumber):
        print("guess is too low")
    elif(userGuess > secNumber):
        print("guess is too high")
    userGuess= int(input("Please enter another choice: "))
    while (userGuess > 10 or userGuess < 1):
        userGuess = int(input("Guess not valid please enter another guess "))

print("you guessed it")
