# Create the class Boardgame with name, price, pieceCount, and publisher properties/attributes. Create a class method that will change the price of the book. Outside of the class, create three objects of the class Boardgame. Print the three boardgame objects using the newly created objects.


class Boardgame:
    def __init__(self, name, price, pieceCount, publisher):
        self.name = name
        self.price = price
        self.pieceCount = pieceCount
        self.publisher = publisher

    def changeBookPrice(self, newPrice):
        self.price = newPrice

    def __str__(self):
        return self.name

game1 = Boardgame("Cards", 5, 52, "A ton of people")
game2 = Boardgame("Chess", 15, 41, "Some People")
game3 = Boardgame("Checkers", 10, 41, "A couple people")

print(game1)
print(game2)
print(game3)
