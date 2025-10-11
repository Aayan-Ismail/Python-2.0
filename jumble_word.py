import random
import time

text = open("dictionary.txt")
word_list = [text]


def jumble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return "".join(word_list)

def get_hint(word):
    return "The first letter of the word is {}".format(word[0].upper()) 

def play():
    score = 0
    rounds = int(input("how many rounds do you want to play for? "))
    print("hello, have fun with scrambling")
    for i in range(1,rounds + 1):
        word = random.choice(word_list)
        scramble_word = jumble_word(word)
        print("round {}".format(i))
        print("here is the scrambled word {}".format(scramble_word))
        
        user_choice = input("do you want a hint?, enter yes or no ").lower()

        if user_choice == "yes":
            print(get_hint(word))
        
        guess = input("guess the word ").lower()

        while not guess.isalpha:
            print("please enter letters only")
            guess = input("guess the word ").lower()


            if guess == word:
                score += 1
                print("good job, guessed correct word, increased the score")
            
            else:
                print("{} was your guess, the correct word was {}".format(guess,word))
        
    print("the score is {} in {} round(s)".format(score,rounds))

    if score == rounds:
        print("you are a geek")

play()

    

