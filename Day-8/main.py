import arts

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p',
 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h', 
 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_number, cipher_direction):
    end_text = ""
    if cipher_direction == "encode":
        shift_number *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_number
            end_text += alphabet[new_position]
        else:
            end_text += char    
    print(f"Here's the {direction}d result: {end_text}")
    
print(arts.logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number:\n")) 
    shift = shift % 26

    caesar(start_text = text, shift_number = shift, cipher_direction = direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Bye Bye") 