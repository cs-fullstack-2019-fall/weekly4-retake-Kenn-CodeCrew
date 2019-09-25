# Create a function that has a parameter of an integer array and returns only the positive numbers in the array. Call the function

def intArrayOnlyPositive(intArray):
    tempArray = []
    for eachElement in intArray:
        if(eachElement > 0):
            tempArray.append(eachElement)
    return tempArray

print(intArrayOnlyPositive([-43,213,-32,1,3,32,-23,-432]))
