from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    def caeser_cipher(start_text, shift_amount, cipher_direction):
            cipher_string = ""
            for char in start_text:
                if char in alphabet:
                    msg_index = alphabet.index(char)
                    if cipher_direction == "encode":
                        cipher_index = (msg_index + shift_amount) % 26
                    elif cipher_direction == "decode":
                        cipher_index = (msg_index - shift_amount) % 26
                    cipher_letter = alphabet[cipher_index]
                    cipher_string += cipher_letter
                else:
                    cipher_string += char
            print(f"The {cipher_direction}d message is '{cipher_string}'")

    caeser_cipher(start_text=text,shift_amount=shift, cipher_direction=direction)
    
    #Asking user if they want to continue
    ask_user = input("Do you want to continue or quit? Type 'Y' to continue or 'N' to quit\n")
    if ask_user == "N":
        should_continue = False