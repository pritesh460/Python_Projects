import random

print("Winning rules of the game ROCK PAPER SCISSORS are:\n" + "Rock vs Paper -> Paper wins \n" + "Rock vs Scissors -> Rock wins \n" + "Paper vs Scissors -> Scissors wins \n")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    choice = int(input("Enter your choice: "))

    while choice > 3 or choice < 1:
        choice = int(input("Enter a valide choice: "))
    
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissors"
    
    print('User choice is:', choice_name)
    print("Now it's Computer's Turn...")

    comp_choice = random.randint(1 ,3)

    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissors"

    print("coputer choice is:" ,comp_choice_name)
    print(choice_name ,"VS" ,comp_choice_name)

    if choice == comp_choice:
        result = "DROW"
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        result = "Paper"
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        result = "Rock"
    elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
        result = "Scissors"

    if result == "DROW":
        print("<== It's a tie! ==>")
    elif choice_name == result:
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

    print("Do you want play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
