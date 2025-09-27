import random

grid = []

def create_grid():
    for i in range(5):
        row = []
        for j in range(5):
            row.append("|")
        grid.append(row)

    return grid

def treasure_mark():
    row = random.randint(0,4)
    column = random.randint(0,4)

    return row,column

def trail(treasure_row,treasure_column,guess_row,guess_column):
    
    if guess_row < treasure_row:
        return "move down"
    
    elif treasure_row < guess_row:
        return "move up"
    
    elif treasure_column < guess_column:
        return "move left"
    
    elif guess_column < treasure_column:
        return "move right"
    
    return "congratulations!, you have found the treasure."

def game():
    grid = create_grid()
    treasure_row,treasure_column = treasure_mark()
    print("try find the treasure, hints given when you guess where it is and fail.")
    attempts = 0

    while True:
        print("\n current grid:")
        for row in grid:
            print(" ".join(row)) 
        
        #exception handling
        try:
            guess_row = int(input("enter a number that will guess what row the treasure is on. "))
            guess_column = int(input("enter a number that guesses what column. "))
            grid[guess_row][guess_column] = "X"

        except ValueError:
            print("invalid input, please enter the numbers between 0-4.")
            continue
            
        if guess_row not in range(5) or guess_column not in range(5):
            print("invalid input, please chouse a number between 0-4")
            continue

        attempts += 1

        if guess_row == treasure_row and guess_column == treasure_column:
            print("congratulations you found the treasure in {} attempts".format(attempts))
            break

        else:
            hint = trail(treasure_row,treasure_column,guess_row,guess_column)
            print("the hint is {}".format(hint))     

game()       
            

        





    