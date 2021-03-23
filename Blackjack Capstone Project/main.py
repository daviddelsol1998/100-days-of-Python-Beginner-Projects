from art import logo
from random import choice

#this program was written 100% by me

def blackjack():
    '''this module does not take any arguments, it's the blackjack game'''
    print(logo)

    #holds the deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    #holds player cards
    player_cards = []

    #holds computer cards
    computer_cards = []

    alive = True
    
    def get_card(entity):
        '''this function deals a card from the deck either to computer or player'''
        #choose random card
        new_card = choice(cards)
        
        #handle ace case (what to do if the card is 11)
        if new_card == 11:
            if sum(entity) + new_card > 21:
                new_card = 1
            else:
                pass # keep 11
        else:
            pass # keep any other value

        entity.append(new_card)

    #deal cards first round
    get_card(player_cards)#player's first card
    get_card(player_cards)#player's second card

    get_card(computer_cards)#computer's first card
    get_card(computer_cards)#computer's second card

    #repeat this cycle while the user is alive
    while alive:
        print(f'\tyour cards: {player_cards}, current score: {sum(player_cards)}')
        print(f"\tcomputer's first card: {computer_cards[0]}")

        #ask if the player wants another card:
        continue_playing = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if continue_playing == 'y':
            get_card(player_cards)#player's new card
            #print(f'\tyour cards: {player_cards}, current score: {sum(player_cards)}')
            #check if user has over 21 cards
            if sum(player_cards) > 21:
                print(f'\tcomputer cards: {computer_cards}')
                print(f'\tyour cards: {player_cards}')
                print('you lose :(')
                alive = False
        else: # when user stops drawing
            #check if computer has reached 17
            while sum(computer_cards) < 17:
                #computer keeps drawing cards until reaching 17
                get_card(computer_cards)#computer's new card
            
            #print totals
            print(f'\tcomputer cards: {computer_cards}, total: {sum(computer_cards)}')
            print(f'\tyour cards: {player_cards}, total: {sum(player_cards)}')

            #check if it's a draw
            if sum(player_cards) == sum(computer_cards):
                print("It's a draw")
                alive = False
    

            #check who won
            if sum(computer_cards) > 21 or sum(player_cards) > sum(computer_cards):
                print('you win!')
                alive = False
            else:
                print('you lose :(')
                alive = False
    
    if alive == False:
        play_the_game()
    

    


def play_the_game():
    '''begin the game'''
    play = input('Do you want to play a game of Blackjack/21? (y/n): ').lower()
    if play == 'y':
        blackjack()
    elif play == 'n':
        print('Goodbye!')


play_the_game()

    



