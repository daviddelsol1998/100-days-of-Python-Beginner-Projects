#debuggin is the process of removing bugs from your code
############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21):
#     #print(i) #the second argument passed to range() is not inclusive 
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# #dice_num = randint(1, 6) # randint is inclusive so error happens when it's 6
# dice_num = randint(0, 5) # since we are dealing with a list of 6 elements
# #if you use random.choice() the bug is prevented
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# #there is no conditional for before 1981
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994: #1994 is not included, easy fix
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))#can't compare str and integers
# if age > 18:
#     #it required indentation
#     print(f"You can drive at age {age}.")#this needs to be an f string

# #Print is Your Friend
# pages = 0
# print(f'pages before assignment {pages}')
# word_per_page = 0
# print(f'words before assignment {word_per_page}')
# pages = int(input("Number of pages: "))
# print(f'pages after assignment {pages}')
# word_per_page = int(input("Number of words per page: ")) #this is a typo comparison (false)
# print(f'words after assignment {word_per_page}')
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)#you need to append each item within the loop
#   print(b_list)

# mutate([1,2,3,5,8,13])