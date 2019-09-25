# Ask the user to enter a number to add to a total. Keep asking the user to enter a number until they enter 0. Afterward, print the total of all numbers entered.

userInput = input("Enter a number to add to a total")
total = 0

while(userInput != "0"):
    total = total + int(userInput)
    userInput = input("Enter aother number to add to the total")
print("The total is " + str(total))