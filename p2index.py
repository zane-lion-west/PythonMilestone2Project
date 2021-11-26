##Blackjack Card Game

#Imports
import random

##Create Deck Variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':1}


#Deck Check
class Card:
    
    def __init__(self, suits, ranks):
        self.suits = suits
        self.ranks = ranks
        self.values = values[ranks]
        
    def __str__(self):
        return(f"Card is {self.ranks} of {self.suits} with the value of: {self.values}")
    
#Create the Deck
class Deck:
    
    def __init__(self):
        self.allcards = []
        for suit in suits:
            for rank in ranks:
                #Create all the cards
                self.allcards.append(Card(suit, rank))
    
    #Shuffle the deck method
    def shuffle(self):
        random.shuffle(self.allcards)
      
    #Deal a card method  
    def dealone(self):
        return self.allcards.pop()
        
class Player:

    def __init__(self, name):
        self.name = name
        self.card_hand = []
    
    #Deal a card to the player    
    def add_card(self, new_card):
        self.card_hand.append(new_card)
        
    #Check hand    
    def __str__(self):
        for card in self.card_hand:
            return f"{self.name} has {card} in their hand"

class Hand:
    
    def __init__(self):
        self.cards = [] #Empty list for the plauer hand
        self.value = 0  #Check the values of the card hand
        self.aces = 0   #How many aces in the hand
    
    def add_card(self, card):
        #Pass card in from deck.deal()
        self.cards.append(card)
        self.value += values[card.ranks]
        

class Bank:
    
    def __init__(self, name):
        self.name = name
        #self.add_amount = add_amount
        #self.subtract_amount = subtract_amount
        self.total_amount = 0
        
    def add_cash(self, add_amount):
        self.total_amount += add_amount
        
    def deduct_cash(self, subtract_amount):
        if self.total_amount > subtract_amount:
            self.total_amount = self.total_amount - subtract_amount
        else:
            pass
            #return(f"Player {self.name} is bust! game over")
    
##Various misc functions

def card_hand_value(card_hand):
    total = 0
    for i in range(len(card_hand)):
        total += card_hand[i].values
    return total    

def y_or_no():
    while True:        
        a = input("Y or N : ").lower()
        if a == "y":
            return("Y")
            break        
        elif a == "n":
            return("N")
            break
        else:
            print("please type Y or N!")

#Create players
playername = ""
playercash = 0
computercash = 0

playername = input("What is your name? ")
    
while True:
    try:
        playercash = int(input("How much bank do you have? "))
    except:
        print("Please enter in a number above 0.")
    else:
        break
            
while True:
    try:
        computercash = int(input("How much bank does the computer have? "))
    except:
        print("Please enter in a number above 0.")
    else:
        break
            

playerone = Player(playername, playercash)

computerplayer = Player("Computer", computercash)

#Create Bank Accounts
playeronebank = Bank(playerone.name)
playeronebank.add_cash(add_amount=playercash)
computerbank = Bank(computerplayer.name)
computerbank.add_cash(add_amount=computercash)

#Create Deck        
newdeck = Deck()
newdeck.shuffle()

#print(len(newdeck.allcards))

# for card in newdeck.allcards:
    #  print(card)

def bet():   
    while True:
        try:
            return int(input("How much would you like to bet? "))
        except:
            print("Please enter in a number above 0.")
        else:
            break

player_bet = bet()
#playeronebank.deduct_cash(starting_bet)
    
def deal_cards():
    #Clear the decks
    playerone.card_hand.clear() 
    computerplayer.card_hand.clear()   
    
    #Deal for player
    playerone.add_card(newdeck.dealone())
    playerone.add_card(newdeck.dealone())
    
    print("Player one has the following cards:")
    for card in playerone.card_hand:
     print(card)
    
    print("\n")
    #Deal for dealer
    computerplayer.add_card(newdeck.dealone())
    computerplayer.add_card(newdeck.dealone())
 
    print("Computer has the following card:")
    print(computerplayer.card_hand[0])
    

def game_on():
    game_win = False
    round_win = False
    deal_again = False
            
    while game_win != True:    
        if playeronebank.total_amount <= 0:
            print("The house wins")
            game_win = True
        elif computerbank.total_amount <= 0:
            print(f"{playerone.name} wins!")
            game_win = True
        else:
            deal_cards()
            
            while round_win != True:
                                        
                while deal_again != True:
                    if card_hand_value(playerone.card_hand) == 21:
                        print(f"{playerone.name} wins this round")
                        playeronebank.add_cash(player_bet)
                        computerbank.deduct_cash(player_bet)
                        print(card_hand_value(f"{playerone.bank} is up to {card_hand_value(playerone.card_hand)}"))
                        print(card_hand_value(f"{computerplayer.name} is up to {card_hand_value(computerplayer.card_hand)}"))
                        round_win = True
                        deal_again = False
                                
                    elif card_hand_value(computerplayer.card_hand) == 21:
                        print(f"{computerplayer.name} wins this round")
                        computerbank.add_cash(player_bet)
                        playeronebank.deduct_cash(player_bet)
                        print(card_hand_value(f"{playerone.bank} is up to {card_hand_value(playerone.card_hand)}"))
                        print(card_hand_value(f"{computerplayer.name} is up to {card_hand_value(computerplayer.card_hand)}"))
                        round_win = True                    
                        deal_again = False
                                
                    elif card_hand_value(playerone.card_hand) > 21:
                        print(f"{playerone.name} is a bust")
                        computerbank.add_cash(player_bet)
                        playeronebank.deduct_cash(player_bet)
                        print(card_hand_value(f"{playerone.bank} is up to {card_hand_value(playerone.card_hand)}"))
                        print(card_hand_value(f"{computerplayer.name} is up to {card_hand_value(computerplayer.card_hand)}"))
                        round_win = True                    
                        deal_again = True
                        break 
                                        
                    elif card_hand_value(computerplayer.card_hand) > 21:
                        print(f"{computerplayer.name} is a bust")
                        playeronebank.add_cash(player_bet)
                        computerbank.deduct_cash(player_bet)
                        print(card_hand_value(f"{playerone.bank} is up to {card_hand_value(playerone.card_hand)}"))
                        print(card_hand_value(f"{computerplayer.name} is up to {card_hand_value(computerplayer.card_hand)}"))
                        round_win = True                    
                        deal_again = True
                        break
                                
                    elif card_hand_value(playerone.card_hand) < 21 and card_hand_value(computerplayer.card_hand) < 21:                
                        print(f"{playerone.name} you have a total of {(card_hand_value(playerone.card_hand))}")                
                        print(f"{playerone.name} would you like another card?")
                        answer = y_or_no()
                        if answer == "Y":
                            playerone.add_card(newdeck.dealone())
                            break
                        elif answer == "N":
                            deal_again = False                   
                        break
                                
                    elif card_hand_value(computerplayer.card_hand) < 21:                    
                        print(card_hand_value(f"{playerone.bank} is up to {card_hand_value(playerone.card_hand)}"))
                        print(card_hand_value(f"{computerplayer.name} is up to {card_hand_value(computerplayer.card_hand)}"))
                            
                    else:
                        print(card_hand_value(f"{playerone.bank} is up to {card_hand_value(playerone.card_hand)}"))
                        print(card_hand_value(f"{computerplayer.name} is up to {card_hand_value(computerplayer.card_hand)}"))
                        print("Some error happened")    
                    
            player_bet = bet()
        
game_on()
