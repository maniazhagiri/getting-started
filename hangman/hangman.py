import random
from hman import lives
from words import word_list

random_word = random.choice(word_list)
#print(random_word)
word_len = len(random_word)
word_blank=""
for i in range(word_len):
    word_blank += "_"
print(word_blank)

game_over = False
guess_list = []
stage = 6
while not game_over:
    guess = input("Please guess the letter : ").lower()
    guess_letter = ""
    if guess in guess_list:
        print("this letter already guessed, please try different letter")
    for letter in random_word:
        if letter == guess:
            guess_letter += letter
            guess_list.append(guess)
        elif letter in guess_list:
            guess_letter += letter
        else:
            guess_letter += "_"
    print(guess_letter)

    if guess not in random_word:
        stage -= 1
        if stage == 0:
            game_over = True
            print("you lose")
    elif "_" not in guess_letter:
        game_over=True
        print("you win")

    print(lives[stage])

