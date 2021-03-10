alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo




def caesar(plain_text,shift_amount, disposition_instruction):
  cipher_text = ""
  for letter in plain_text:
    if not letter.isalpha():
        cipher_text += letter
    else:
        position = alphabet.index(letter)
        if disposition_instruction == 'encode':
            new_position = position + shift_amount
        elif disposition_instruction == 'decode':
            new_position = position - shift_amount
        cipher_text += alphabet[new_position]
  print(f"The {disposition_instruction}d text is {cipher_text}")

print(logo)

cipher_in_use = True

while cipher_in_use:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text= input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))
    if shift == 26:
        shift = 4895
    if shift > 26:
        shift = shift % 26



    caesar(plain_text = text ,shift_amount = shift, disposition_instruction = direction)
    

    again = input("Would you like to use the cipher again? (Y/N) ").lower()
    if again == 'n':
        cipher_in_use = False
        print('Goodbye!')