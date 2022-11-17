import random
from hangmanart import stages, logo
from hangmanWordList import word_List
word_List=["banana","man","libombo","simaltenous","dictionary",
"music","python","baboon","samsung","mealie","weed","manchester"]
print(logo)
chosen_word = random.choice(word_List)
lives = 6
#print(f"Psst, the solution is {chosen_word}")
display =[]
for _ in chosen_word:
    display += "_"

end_of_game = False
while not end_of_game:
    guess = input("Guess a Letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(chosen_word)):
        letter =chosen_word[position]
        if(letter == guess):
            display[position]= letter
        
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -=1
        if lives ==0:
            end_of_game=True
            print("You lose")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    print(stages[lives])