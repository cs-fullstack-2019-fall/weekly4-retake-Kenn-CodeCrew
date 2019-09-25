# Create a Puppy class. It should have properties name and color. Create a program that will ask a user to enter the name, then the color of a puppy until they enter 'q' to quit. Put each entry in an array.

class Puppy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"{self.name} is {self.color}"

puppyArray = []
userPuppyName = input("Enter the name of a puppy")
userPuppyColor = input("Enter the color of a puppy")

while(userPuppyName != 'q' and userPuppyColor!= 'q'):
    tempObject = Puppy(userPuppyName, userPuppyColor)
    puppyArray.append(tempObject)
    userPuppyName = input("Enter the name of a puppy")
    userPuppyColor = input("Enter the color of a puppy")

# You don't have to add this part. I wanted to check to see if the array was correct
for eachElement in puppyArray:
    print(eachElement)
