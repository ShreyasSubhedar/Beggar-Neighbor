from random import shuffle

def createDeck():
    Deck = []

    #Set a variable for faceValues
    cards = ['🅰️','2','3','4','5','6','7','8','9','10' '🇯', '🤴', '🤴']
    for card in cards: # Adding numbers 
        for ctype in ['♠','♣️','♥️','♦️']:  # There are 4 different suites
            Deck.append(card+ctype)

    shuffle(Deck) # Mixing results with shuffle
    return Deck # Return products


# Set a player class
class Player:
    def __init__(self,cards = []):     #__init__ is the constructor for a class
      self.cards = cards

    def __str__(self):       #__str__ will return a human readable string
      currentHand = " "

      for card in self.hand:
          currentHand  += str(card) + " "

      #Set a variable for finalStatus, and then return it
      finalStatus = currentHand + "score " + str(self.score)
      return finalStatus



# Create card Deck 
cardDeck = createDeck()

# Distribute the cards for player 1
firstPlayer =cardDeck[:,len(cardDeck)//2]

# Distribute the cards for player 2
secondPlayer = cardDeck[len(cardDeck)//2,:]

# creating Player 1

playerOne = Player(firstPlayer)