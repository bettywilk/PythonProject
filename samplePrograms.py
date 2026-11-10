weightInPounds = float(input("please enter your weight in pounds:"))

print("\nYou weigh ", weightInPounds * .165, " on the moon.")

print("\n\nHello, World!")


tempFahrenheit = float(input("please enter your temperature in Fahrenheit:"))

print("\ntemperature in Kelvin is ", ((tempFahrenheit - 32) * (5 / 9) + 273.15))

print("\n\nHello, World!")


dailyCalories = float(input("please enter your calorie intake per day:"))

NumOfYears = float(input("\nhow many years will you consume those daily calories"))

print("\nPounds gained/lost ", ((dailyCalories - 2500) * 365 * NumOfYears / 3500, " in ", NumOfYears))

print("\n\nHello, World!")

# int gainLoss = (calories - 2500) * 365 * numOfYears/3500