from art import logo
from random import randint
from sys import exit

def guessing_game():
    '''this function contains the whole guessing game'''
    
    print(logo)

    #welcome user
    print('Welcome to the name guessing game!')
    print('I am thinking of a number between 1 and 100')

    def set_secret_num():
        '''this function uses the randint from the random module to
        generate a random number'''
        #set secret number
        secret_number = randint(1,100)
        #print secret number for debugging purposes
        print(f"The secret number is '{secret_number}'")
        return secret_number

    #store secret number in a variable
    secret_number = set_secret_num()

    #set difficulty
    difficulty = input("Choose your difficulty, type 'e' for easy or 'h' for hard: ").lower()

    def set_difficulty(difficulty_given):
        '''this function takes an argument 'difficulty'
        and returns the number of possible attempts'''
    
        if difficulty_given == 'e':
            attempts = 10
            print("you will get 10 attempts")
        elif difficulty_given == 'h':
            attempts = 5
            print("you will get 5 attempts")
        else:
            attempts = 7
            print("that wasn't hard or easy so you will get 7 attempts")

        return attempts
    
    attempts = set_difficulty(difficulty)

    def guess(attempts_given):
        '''this is the main function of the game, it takes the argument
        attempts and allows the player to guess based on how many attempts
        they have'''
        #take guesses
        while attempts_given > 0:
            print(f'You have {attempts_given} attempts to guess the number')
            guess = int(input('Guess a number: '))

            #check if there's a match
            if guess == secret_number:
                print(f'You got it, {guess} is the number I was thinking about. :)')
                exit() #ends program if there is a match

            else:#removes one possible attempt and gives a hint to the player
                attempts_given -= 1
                if guess > secret_number:
                    print('Too high!')
                else:
                    print('Too low!')
        #if there was no match after all possible attempts the player loses 
        print('Sorry, you did not guess my number :(')
    
    guess(attempts)

guessing_game()

    










