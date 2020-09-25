from random import shuffle

def createDeck():
    Deck = list()

    #Set a variable for faceValues
    cards = ['A','2','3','4','5','6','7','8','9','10', 'J', 'Q', 'K']
    for card in cards: # Adding numbers 
        for ctype in ['C','S','H','D']:  # There are 4 different suites
            Deck.append(card+"  "+ctype)

    shuffle(Deck) # Mixing results with shuffle
    return Deck # Return products
