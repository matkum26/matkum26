# a alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# encryption
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) 
            cipher_text += alphabet[new_position]
        else:
          
            cipher_text += letter
    print(f"The encoded text is: {cipher_text}")

# decryption
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift_amount)
            plain_text += alphabet[new_position]
        else:
           
            plain_text += letter
    print(f"The decoded text is: {plain_text}")

# User input
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number (1-25): "))

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print("Invalid input. Please choose 'encode' or 'decode'.")
