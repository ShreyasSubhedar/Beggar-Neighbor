from Deck import createDeck


def manual():
    print(f"Beggar My Neighbor, a card game suitable for small children that’s also known as Beat Your Neighbor Out of Doors and\nStrip Jack Naked, is a very simple game, requiring no strategy or planning at all. \nThe objective of the game is to win all the cards from the other players.")
    print("Get the top card on the game if its matches with oppoents all the cards on the stacks are yours")
# Set a player class


class Player:
    def __init__(self, cards, name):  # __init__ is the constructor for a class
        self.cards = cards
        self.name = name
# Game steps


class Game:
    def __init__(self, player1,player2):
        self.player1 = player1
        self.player2 = player2

    def playOne(self):
        top = player1.cards.pop()
        return top
    def playTwo(self):
        top = player2.cards.pop()
        return top


# Create card Deck
cardDeck = createDeck()

# Distribute the cards for player 1
cards = cardDeck[0:len(cardDeck)//2]

# creating Player 1
name1 = input("Please enter your name Player 1 :  ")
player1 = Player(cards, name1)


# Distribute the cards for player 1
cards = cardDeck[len(cardDeck)//2:]

# creating Player 2
name2 = input("Please enter your name Player 2 :  ")
player2 = Player(cards, name2)

# Starting the game
a = ""
chance=True
game= Game(player1,player2)
while a != '--quit':
    a = input()
    if a == "--help":
        manual()
        a=input()
    if a=="--resume":
        pass
    if chance==True:
        print(player1.name+" chance")
        print(game.playOne())
    else:
        print(player2.name+" chance")
        print(game.playTwo())
    
    chance=(~chance)
    
    
