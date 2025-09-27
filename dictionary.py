dictionary = {

}
print(type(dictionary))
while True:
    print("mini dictionary app")
    print("1. add/update a word")
    print("2. retrieve a word defintion")
    print("3. delete a word")
    print("4. view all words")
    print("5. exit")
    choice = int(input("pick a number between 1 - 5 "))
    if choice == 1:
        new_word = input("enter the word ").strip()
        new_word_meaning = input("enter the word's definition ").strip()
        dictionary[new_word] = new_word_meaning
        print("The word {} has been added/updated successfully".format(new_word))
    
    elif choice == 2:
        new_word = input("what word do you want to see? ")
        if new_word in dictionary :
            print("{} : {}".format(new_word , dictionary[new_word]))
    
    elif choice == 3:
        delete_word = input("which word do you want to delete? ").strip()
        if delete_word in dictionary :
            del dictionary[delete_word]
            print(delete_word, "has been deleted.")
        
        else:
            print("the word is not in the dictionary.")
        
    elif choice == 4:
        if dictionary:
            print(dictionary)
    
        else:
            print("the dictionary is empty")
    
    elif choice == 5:
        print("we are closing the dictionary")
        break

    else:
        print("type a number between 1 and 5, retry.")
        


        
    

