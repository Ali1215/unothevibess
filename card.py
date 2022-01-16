#print("guys this is gonna be harder than I thought")
#https://www.kaggle.com/vatsalparsaniya/uno-cards?select=Wild.jpg

class card:
    def __init__(self, color, number):
        self.color=color
        self.number=number
    
    def __str__(self):
        return "Color: " + self.color + " Number: " + str(self.number)

    def __eq__(self, other):
        if isinstance(other, card):
            return ((self.number==other.number) and (self.color==other.color))
        return False
