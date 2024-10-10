import random
import hangman_arts
import word_list

end_of_game = False
chosen_word = random.choice(word_list.words)
print(hangman_arts.logo)
lives = 6   

# print(f"solution is {chosen_word}")
#Create blank space
display = ['_'] * len(chosen_word)
print(display)

while not end_of_game:
    #Gusse letter
    guesse = input("Guess a letter? ").lower()
    if guesse in display:
        print(f"You've already guessed {guesse}")

    #Check gussed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guesse == letter:
            display[position] = letter

    if guesse not in chosen_word:
        print(f"You guessed {guesse}, but it's not in this word, You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
            print(f"Your word is {chosen_word}")    

    print(f"{''.join(display)}")

    if "_" not in display:
        print("You Win!")
        end_of_game = True
    
    print(hangman_arts.stages[lives])
