# Ask the user to enter their age. Check if they entered a value between 0 and 125. If valid, print "REAL AGE". If invalid print “NOT A REAL AGE!!!”

userAge = int(input("Enter your age"))

if(userAge >= 0 and userAge <= 125):
    print("REAL AGE")
else:
    print("NOT A REAL AGE")
