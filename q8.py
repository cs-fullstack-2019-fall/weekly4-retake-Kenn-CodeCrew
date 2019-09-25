# Create a function that takes a string array and returns a string array with the letter 's' at the end of each element. Call the function.

def stringArrayWithS(stringArray):
    tempStringArray = []
    for eachElement in stringArray:
        tempStringArray.append(eachElement + "s")
    return tempStringArray

print(stringArrayWithS(["Kenn", "Kevin", "Erin", "Thomas"]))
