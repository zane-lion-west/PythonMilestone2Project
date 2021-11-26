##Blackjack Card Game

#Imports
import random
game_on = True

##Create Deck Variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


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
        
        #Track aces
        if card.ranks == 'Ace':
            self.aces += 1
            

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Bank:
    
    def __init__(self, name, total_amount=100):
        self.name = name
        self.total_amount = total_amount
        self.bet = 0
        
    def add_cash(self):
        self.total_amount += self.bet
        
    def deduct_cash(self):
        self.total_amount -= self.bet


def take_bet(cash):
    while True:
        
        try:
            cash.bet = int(input("How much cash would you like to bet?"))
        except:
            print("Sorry please provide a correct amount of cash")
        else:
            if cash.bet > cash.total_amount:
                print(f"Sorry you do not have enought cash, you only have {cash.total_amount}")
            else:
                break

def add_card_hand(deck, hand):
    single_card = deck.dealone()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand, game_on):
    
    while True:
        x = input('Hit or Stand? Please enter either h or s')
        
        if x[0].lower() == 'h':
            add_card_hand(deck, hand)
            
        elif x[0].lower() == 's':
            print('Player stands, dealers turn')
            game_on = False
            return game_on
        
        else:
            print("Please enter either h or s")
            continue
        break
    
def show_some_cards(player, dealer):
    #show one of the dealers cards
    
    print("\n Dealers current hand: ")
    print("first card hidden")
    print(dealer.cards[1])
                   
    #Show the players cards
    print(" \n Players current hand:")
    for card in player.cards:
        print(card)
        
def show_all_cards(player, dealer):
    
    #Dealers cards and value
    print(" \n Dealers Hand:")
    for card in dealer.cards:
        print(card)
    print(f"Value of dealers hand is {dealer.value}")
    
    #Players cards and value
    print(" \n Players Hand:")
    for card in player.cards:
        print(card)
    print(f"Value of dealers hand is {player.value}")
    
def player_busts(player, dealer, cash):
    print("Player Busts!")
    cash.deduct_cash()
    
def dealer_busts(player, dealer, cash):
    print("Dealer Busts, player wins!")
    cash.add_cash()
    
def dealer_wins(player, dealer, cash):
    print("Player Busts, dealer wins!")
    cash.deduct_cash()
    
def player_wins(player, dealer, cash):
    print("Player wins!")
    cash.add_cash()

def push(player, dealer):
    print("Player and dealer are a tie! PUSH")
    
### GAME LOGIC ###
while True:
    print("Welcome to 21")

    #Create and shuffle the deck
    new_deck = Deck()
    new_deck.shuffle()

    #Deal hands
    player_hand = Hand()
    player_hand.add_card(new_deck.dealone())
    player_hand.add_card(new_deck.dealone())

    dealer_hand = Hand()
    dealer_hand.add_card(new_deck.dealone())
    dealer_hand.add_card(new_deck.dealone())

    #Set up the players Bank
    player_name = input("What is your name?")
    player_cash = 0
    while True:
        try:
            player_cash = int(input("How much bank do you have? "))
        except:
            print("Please enter in a number above 0.")
        else:
            break

    player_bank = Bank(player_name, player_cash)

    #Ask the player for their bet amount
    take_bet(player_bank)

    #Show cards but keep one of the dealers hidden
    show_some_cards(player_hand, dealer_hand)


    while game_on: 
        #Prompt player to hit or stand
        hit_or_stand(new_deck, player_hand, game_on)
        
        #Show cards but keep on eof the dealers hand cards hidden
        show_some_cards(player_hand, dealer_hand)
        
        #If player's hand exceeds 21, run player_busts() and break out of the loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_bank)
            break    
        
    #If player hasnt hit bust, play the dealers hand until the dealer reaches 17
    if player_hand.value <= 21:
        
        while dealer_hand.value < player_hand.value:
            add_card_hand(new_deck,dealer_hand)
            
        #Show all the cards that
        show_all_cards(player_hand,dealer_hand)
        
        #Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_bank)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_bank)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_bank)
        else:
            push(player_hand,dealer_hand)
            
    #Inform player of their total bank
    print(f" Players total bank is {player_bank.total_amount}")

    #Play again?
    new_game = input("Would you like to play another hand? y/n")

    if new_game[0].lower == "y":
        game_on = True
        continue
    else:
        print("thanks for playing!")
        break