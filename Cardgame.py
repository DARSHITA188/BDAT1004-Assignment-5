import random

class Card:

    suit_names = ["HEARTS", "DIMONDS", "CLUBS", "SPADES"]
    rank_names = ["A", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def show(self):
        print("{} of {}".format(self.rank,self.suit))

class Deck:
    
    def __init__(self):
        self.card = []
        self.build()

    def build(self):
        for suit in ["HEARTS", "DIMONDS", "CLUBS", "SPADES"]:
            for rank in range(1,14):
                self.card.append(Card(suit,rank))

    def show(self):
        for card in self.card:
            card.show()

    def shuffle(self):
        for i in range(len(self.card)-1,0,-1):
            r=random.randint(0,i)
            self.card[i],self.card[r] = self.card[r],self.card[i]

    def draw(self,deck):
        self.hand.append(deck.drawCard())
        return self
        
    def drawCard(self):
        return self.card.pop()

class Player1:

    def __init__(self,name):
        self.name = name
        self.hand = []

    def draw(self,deck):
        self.hand.append(deck.drawCard())
        return self

    def showh(self):
        for card in self.hand:
            card.show()


deck = Deck()
deck.shuffle()

card = deck.drawCard()
card.show()

Darshita = Player1("Hii")
Darshita.draw(deck)
Darshita.showh()

print("Woah")


    
