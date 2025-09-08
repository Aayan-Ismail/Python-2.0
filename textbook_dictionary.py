textbooks = {
"physics textbook": 10,
"math textbook" : 100,
"irish textbook": "free",
"latin textbook": 150,
"german textbook": 100,
"french textbook": 100,
"english textbook": 100,
"geograhy textbook": 100,
"history textbook": 100,
"religion textbook": 100,
"sphe textbook": 100,
"cspe textbook": 100,
}

while True:
    print("welcome, this is the shop with the following textbooks and their prices.")
    print(textbooks)
    print("type 1 to edit an existing textbook's price.")
    print("type 2 to create a new textbook, also updating the list of textbooks.")
    print("type 3 to check if a certain textbook is in the shop, if it is, the price of the textbook will be listed.")
    print("type 4 to end.")
    
    choice = int(input("type a number between 1 and 4 "))

    if choice == 1:
        textbook = input("name the textbook that you would like to edit the price of. ")
        if textbook in textbooks:
            new_textbook = int(input("what is the new price for the textbook? "))
            textbooks[textbook] = new_textbook
            print(textbook+"'s price has been updated.")
        else:
            print("this textbook is not in the shop")

    if choice == 2:
        textbook = input("type the name of the textbook you would like to add")
        textbook_price = int(input("type the price of the textbook you would like to add "))
        textbooks[textbook] = textbook_price
        user_textbook = textbooks['textbook']
        print(textbook, "has been added to the shop.")
    
    if choice == 3:
        textbook = input("type the name of the textbook ")
        if textbook in textbooks:
            print(textbooks[textbook])
        
        else:
            print("this textbook is either not in the shop or you misspelt it, try a different name?")
    if choice == 4:
        print("the shop is closing, thank you and goodbye.")
        break
    
    else:
        print("please type a number between 1 and 4.")

    





   