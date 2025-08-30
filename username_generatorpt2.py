import random

def username(full_name):
    name_parts = full_name.split()
    if len(name_parts) < 2:
        return "Please enter your full name, which is your first and last name with a space inbetween"

    first_name = name_parts[0].lower()
    last_name = name_parts[-1].lower()

    randomruser6 = str(random.randint(-50,50))
    randomruser7= str(random.randint(-50,50))
    randomruser8 = str(random.randint(-50,50))
    

    #combination 1
    username1 = (first_name + last_name)
    username2 = (last_name + first_name)
    username3 = (first_name + first_name)
    username4 = (last_name + last_name)
    username5 = first_name[:3] + last_name[:3] + first_name[4:6] + last_name[4:6]
    username6 = (first_name + randomruser6 + last_name)
    username7 = (first_name + randomruser6 + last_name + randomruser7)
    username8 = (first_name + randomruser6 + last_name + randomruser8 + randomruser7)

    username = [username1 , username2 , username3 , username4 , username5 , username6 , username7 , username8]
    return random.choice(username)

while True:
    full_name = input("type your first and last name to generate a username, type exit to exit the generator. ")
    if full_name.lower() == "exit":
        break
    name = username(full_name)
    print(name)
    









