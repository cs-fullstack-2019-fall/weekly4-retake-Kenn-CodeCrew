# Create a function that’s passed three integer numbers. Print the sum of the first two numbers and return the product of the second two numbers.

def productOfSecondNumbers(number1, number2, number3):
    print("The sum of the first two is " + str(number1 + number2))
    return number2 * number3

print(productOfSecondNumbers(5, 3, 1))