#this is a console game copy of http://www.higherlowergame.com/
#import logos and accounts and the clear method from replit
import random
from art import logo, vs
from profiles import accounts
from module_clear import clear
#import choice to randomly pick an account
from random import choice

#variable that holds score
score = 0

#variable that will hold the winner of each round
winner = {}

#variable that determine whether this is the first round
first_round = True


#grabs an account from the list and returns it
def grab_account():
    profile = choice(accounts)
    return profile



#game that runs and updates screen while user is alive
def game():
    '''this function does not take arguments,
    it contains the full game'''

    print(logo)
    
    #print a score if it's greater than one
    global score

    if score > 0:
        print(f'You are right!, your current score is {score}')
    else:
        pass
    

    #assign accounts to A and B
    if first_round:
        a = grab_account()
        b = grab_account()
    else:
        a = winner
        b = grab_account()

    #check if a == b, if it is pick a different one
    while a == b:
        b = grab_account()
    
    def generate_sentence(letter):
        name = letter['name']
        description = letter['description']
        country = letter['country']

        return f'{name}, a {description}, from {country}'


    #assign sentences to a and b
    a_sentence = generate_sentence(a)
    b_sentence = generate_sentence(b)

    #used for testing
    a_followers = a['follower_count']
    b_followers = b['follower_count']

    #allow the user to compare
    print(f'Compare A: {a_sentence} {a_followers}')
    print(vs)
    print(f'Againts B: {b_sentence} {b_followers}')

    

    #holds the player's guess on who has more followers on instagram
    #input check for guess
    unvalid_answer = True

    while unvalid_answer:
        guess = input("Who has more followers? Type 'a' or 'b': ").lower()
        if guess == 'a' or guess == 'b':
            unvalid_answer = False

    #compares if the user guess is true, in other words who has more followers
    def compare_followers(guess,other_letter):
        global winner
        global first_round
        if guess['follower_count'] < other_letter['follower_count']:
            print('Sorry, you were wrong')
            return False
        else:
            winner = guess
            first_round = False
            clear()
            return True

    #calls compare followers and determine if the player hasn't failed yet
    if guess == 'a':
        alive = compare_followers(a,b)
    else:
        alive = compare_followers(b,a)

    #if alive add 1 to the score and call game again
    if alive:
        score += 1
        game()

game()

    

