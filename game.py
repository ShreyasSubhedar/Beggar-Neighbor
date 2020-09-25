from Deck import createDeck
from random import shuffle

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
        self.stk=[]
        self.chance=True
    def playOne(self):
        if len(player1.cards)!=0:
            top = player1.cards.pop()
            self.stk.append(top)
            self.chance =True
            shuffle(player1.cards)
            return top
        return "_"
    def playTwo(self):
        if len(player2.cards)!=0:
            top = player2.cards.pop()
            self.stk.append(top)
            self.chance=False
            shuffle(player2.cards)
            return top
        return "_"
    
    def winning_stk(self):
        if len(self.stk)>=2:
            c1 = self.stk[-1]
            c2 =self.stk[-2]
            if c1[-1]==c2[-1]:
                print("matching "+c1[-1])
                print("matching "+c2[-1])
                if self.chance==True:
                    player1.cards.extend(self.stk)
                    print(player1.name+" got all the cards")
                else:
                    player2.cards.extend(self.stk)
                    print(player2.name+" got all the cards")
                self.stk=[]
            

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
    if a == "--help": # Asking for manual
        manual()
        a=input()  # getting the input as --resume
    if a=="--resume":
        pass
    if chance==True: # player 1 chance
        print(player1.name+" chance "+str(len(player1.cards)) +" card/s left")
        card = game.playOne() 
        if card=="_":
            print(player2.name+" wins the game ")
            break
        print(card)
    else: # Player 2 Chance
        print(player2.name+" chance"+str(len(player2.cards)) +" card/s left")
        card =game.playTwo()
        if card=="_":
            print(player1.name+" wins the game ")
            break
        print(card)
    print("Cards on the table :- "+str(len(game.stk)))
        
    game.winning_stk()
    chance=(~chance)
    
    
    
