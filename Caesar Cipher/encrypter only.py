'''Modified version of Caesar Cipher to be used as a feature for a password manager'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lenght_of_alphabet = len(alphabet)


#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#encrypter only
text = input("Type your message:\n").lower()


shift = lenght_of_alphabet + 1
while shift > lenght_of_alphabet:
    shift = int(input("Type the shift number:\n"))


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text_input, shift_amount):
    new_text = []
    lenght_of_alphabet = len(alphabet)
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    for letter in text_input:
        #keep spaces as they are
        if letter == ' ':
            new_text.append(' ')
        else:
            #grabs the position of the original letter of the alphabet
            position = alphabet.index(letter)
            #variable used to calculate if shift is possible
            tentative_shift = position + shift_amount
            #if possible, shift letters up otherwise shift them down
            #shifting up is only possible when the tentative shift is lower or equal to the lenght of the alphabet
            if tentative_shift <= lenght_of_alphabet:
                new_position = tentative_shift
            else:
                new_position = position - shift_amount

            #gets the new letter
            new_letter = alphabet[new_position]
            new_text.append(new_letter)
    
    print(f"your encrypted text is '{''.join(new_text)}'")



#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(text,shift)
