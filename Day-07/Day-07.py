#Hangman : ) 

#flowchart programming 
#start
#while loop to make it a continue effect
#word guess
#wrong guess
#then one step proceed to hanging
#correct guess
#then one step proceed to winning
#end

# word_list = ["ardvark", "baboon", "camel"]
# import random 

# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# # Use a list so we can replace underscores easily
# display = ["_"] * word_length
# print(" ".join(display))

# end_of_game = False

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     # Track if guess was correct
#     guess_correct = False

#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#             guess_correct = True

#     if guess_correct:
#         print("Right.")
#     else:
#         print("Wrong.")

#     print(" ".join(display))

#     # End game when all letters guessed
#     if "_" not in display:
#         end_of_game = True
#         print("You win!")

#=========================================================================#
import random

logo = """
 _                                            
| |                                           
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __ 
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""
print(logo)

stages = [
    """
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """
]

word_list = [
    "apple", "banana", "cherry", "grape", "orange", "strawberry", "watermelon", "mango", "papaya", "peach",
    "elephant", "tiger", "giraffe", "zebra", "kangaroo", "dolphin", "penguin", "eagle", "lion", "rabbit",
    "mountain", "river", "desert", "island", "forest", "valley", "ocean", "beach", "canyon", "volcano",
    "school", "pencil", "window", "garden", "pillow", "rocket", "planet", "galaxy", "comet", "asteroid",
    "bridge", "castle", "ladder", "mirror", "bucket", "hammer", "guitar", "violin", "drum", "candle"
]

chosen_word = random.choice(word_list)
placeholder = ["_"] * len(chosen_word)
corrected_letters = []
lives = 6
game_end = False

print("Word to guess: ", " ".join(placeholder))

while not game_end:
    guess = input("Guess a letter: ").lower()
    
    if guess in corrected_letters:
        print(f"You've already guessed {guess}")
        continue  # skip rest of loop if already guessed

    corrected_letters.append(guess)

    if guess in chosen_word:
        # update placeholder for all occurrences
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                placeholder[i] = guess
    else:
        lives -= 1
        print(f"Wrong guess! Lives remaining: {lives}")
        print(stages[lives])

    print("Word to guess: ", " ".join(placeholder))

    # check for win
    if "_" not in placeholder:
        print("Congratulations! You guessed the word correctly!")
        game_end = True

    # check for lose
    if lives == 0:
        print(f"You lose! The word was: {chosen_word}")
        game_end = True
