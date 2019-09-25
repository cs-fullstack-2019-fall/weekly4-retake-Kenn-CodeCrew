# Create an array of 4 names. Print one string that has all of the arrays separated by commas.

arrayOfNames = ["Kenn", "Kevin", "Erin", "Thomas"]
stringOfNames = ""

for eachElement in arrayOfNames:
    stringOfNames = stringOfNames + eachElement + ", "

print(stringOfNames)
