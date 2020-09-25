from Deck import createDeck
# Set a player class
class Player:
    def __init__(self,cards,name):     #__init__ is the constructor for a class
      self.cards = cards
      self.name= name
# Game steps 
class Game:
    def __init__(self,player):
        self.player = player
    
    def play(self):
        top = player.cards.pop()
        return top


# Create card Deck 
cardDeck = createDeck()

# Distribute the cards for player 1
cards =cardDeck[0:len(cardDeck)//2]

# creating Player 1
name1=input("Please enter your name Player 1 :  ")
player1 = Player(cards,name1)


# Distribute the cards for player 1
cards =cardDeck[len(cardDeck)//2:]

# creating Player 2
name2=input("Please enter your name Player 2 :  ")
player2 = Player(cards,name2)

#Starting the game



