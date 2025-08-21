list_of_task = []

while True:
    choice = int(input("Enter 1 to view task, 2 to create a task, 3 to delete a task and 4 to exit: "))

    if choice == 1:
        for i in list_of_task:
            print(i)
    
    elif choice == 2:
        task = input("Enter the task you want to add: ")
        list_of_task.append(task)
        print("Task " + task + " added.")
    
    elif choice == 3:
        print(list_of_task)
        task = input("type the task you want to delete ")
        list_of_task.remove(task)
        print(task, " has been removed.")
    
    elif choice == 4:
        print("Now we are exiting the to-do-list")
        break
    else:
        print("you have entered an invalid response, please enter the numbers 1, 2, 3 and 4 for the respones above.")
