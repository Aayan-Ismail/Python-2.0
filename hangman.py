import random

def hangman():
    words = ["spiritual","resonance","weightless","iridiscence","propriety","contempt","malevolence","benevolence","radiance","anemic","avarice","brotschneidemaschine","Rindfleischetikettierungsüberwachungsaufgabenübertragungsgesetz"]

    question = input("do you want to play two player hangman, computer puts in correct letters?, type yes to accept, anything else to decline (you guess computer's words.) ")

    if question == "yes":
         secret_word = input("type a word for the other person to guess. ").lower()
         guesses = int(input("how many guesses would you like to give them? "))

         word_guess = secret_word
         max_attempts = guesses
         for i in range(500):
             print("no peeking.")
      
    else:
        print("welcome to your worst nightmare, these words are really evil, have fun guessing, one letter at a time (a tip would be type vowels first)")
        word_guess = random.choice(words)
        max_attempts = 8


    guessed_word = ["_"] * len(word_guess)
    attempts = 0
    score = 0

    guessed_letters = []

    print("length of the word is {}, the max score corresponds to this if the same letter doesnt repeat itself".format(len(word_guess)))
    print("Word:"," ".join(guessed_word))
    while attempts < max_attempts and "_" in guessed_word:
        guess = input("\nenter a letter ").lower()
        
        if len (guess) != 1 or not guess.isalpha():
            print("please enter a single valid letter")
            continue

        if guess in guessed_letters:
            print("your suffering from memory loss, or you did a typo, not good enough, try again and make sure you remember your letters")
            continue

        guessed_letters.append(guess)

        if guess in word_guess:
            print("correct guess, {} was in the word".format(guess))
            score += 1

            for i in range(len(word_guess)):
                if word_guess[i] == guess:
                    guessed_word[i] = guess
        
        else:
            attempts += 1
            print("you have guessed incorrectly, you have {} attempts left".format(max_attempts - attempts))
            score -= 1
        
        print("word-", " " .join(guessed_word))

    if "_" not in guessed_word:
        print("congratulations, you guessed the word which is {}".format(word_guess))
        print("your score was {}".format(score))
    
    else:
        print("game over, the word was {}, better luck next time pal".format(word_guess))
        print("your score was {}".format(score))

    
hangman()
