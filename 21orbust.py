# Authors: Ryan and Nolan
# 21 or Bust


# importing
import os
import random 

decks = input("Enter number of decks to use: ")

# user choses # of decks
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*(int(decks)*4)

# initial scores
wins = 0
losses = 0

# deck being delt
def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"   
        if card == 13:card = "K"     # identifying certain cards
        if card == 14:card = "A"
        hand.append(card)
    return hand

# user has option to play again
def play_again():
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        game()
    else:
        print("Have a good one")
        exit()

# your total hand
def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total+= 10
        elif card == "A":
            if total >= 11: total+= 1
            else: total+= 11
        else: total += card
    return total

# user has option to hit
def hit(hand):
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"  # setting up card value
    hand.append(card)
    return hand

# clears the screen, also looked up how to do this
def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealer, player):
    clear()
# looked up colors in puython to be more creative
    print("\n    WELCOME TO 21 OR BUST!\n") # used /n to create a new line
    print("-"*30+"\n")
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
    print("-"*30+"\n")
    print("The dealer has a " + str(dealer) + " for a total of " + str(total(dealer)))
    print(("You have a " + str(player + " for a total of " + str(total(player)))))

def blackjack(dealer, player):   # embodies the blackjack rule
    global wins
    global losses   # stores number of losses and wins
    if total(player) == 21:
        print_results(dealer, player)
        print ("Congratulations! You got 21 \n")
        wins += 1
        play_again()
    elif total(dealer) == 21:  # emplies the blackjack rule
        print_results(dealer, player)
        print ("Tough luck, the dealer got 21\n")
        losses += 1
        play_again()


def score(dealer, player):
        # total score and how scoring works
        global wins
        global losses
        if total(player) == 21:
            print_results(dealer, player)
            print ("You got 21!\n")
            wins += 1
        elif total(dealer) == 21:
            print_results(dealer, player)
            print ("Dealer got 21\n")
            losses += 1
        elif total(player) > 21:
            print_results(dealer, player)
            print ("You busted, you lose \n")
            losses += 1
        elif total(dealer) > 21:
            print_results(dealer, player)
            print ("Dealer busts, you win \n")
            wins += 1
        elif total(player) < total(dealer):
            print_results(dealer, player)
            print ("You lose\n")
            losses += 1
        elif total(player) > total(dealer):
            print_results(dealer, player)
            print ("You win\n")
            wins += 1

def game():   # defining game 
    global wins
    global losses
    choice = 0
    clear()
    print("\n    WELCOME TO 21 OR BUST!\n")
    print("-"*30+"\n")
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
    print("-"*30+"\n")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print ("The dealer is showing a " + str(dealer_hand[0]))
    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
    blackjack(dealer_hand, player_hand)
    quit=False
    while not quit:
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        # used [] so user only has to type one letter
        if choice == 'h':
            hit(player_hand)
            print(player_hand)
            print("Hand total: " + str(total(player_hand)))
            if total(player_hand)>21:
                print('You busted')
                losses += 1
                play_again()
        elif choice=='s':
            while total(dealer_hand)<17:
                hit(dealer_hand)
                print(dealer_hand)
                if total(dealer_hand)>21:
                    print('Dealer busts, you win!')
                    wins += 1
                    play_again()
            score(dealer_hand,player_hand)
            play_again()
        elif choice == "q":
            print("Have a good one")
            quit=True
            exit()

# prevents parts of code from being run when modules are imported
if __name__ == "__main__":
   game()