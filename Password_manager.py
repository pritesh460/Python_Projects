import random
import string

passwowords = {}

#load exiting password file
try:
    with open("passwords.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwowords[website] = pwd
except:
    pass

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%&"
    passwoword = "".join(random.choice(chars) for _ in range(8))
    return passwoword

while True:
    print("\n-----PERSONAL PASSWORD MANAGER APP-----")
    print("1. Save Password")
    print("2. View Password")
    print("3. Generate Password")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Save Password

    if choice == "1":
        site = input("enter website: ")
        pwd = input("enter password: ")

        passwowords[site] = pwd

        with open("passwords.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")
        
        print("saved!")

    # View Password
    elif choice == "2":
        if not passwowords:
            print("No data")
        else:
            for site, pwd in passwowords.items():
                print(site, ":", pwd)

    # Generate Password
    elif choice == "3":
        print("Generated password:",generate_password())

    # Exit
    elif choice == "4":
        print("Ok bye...")
        break
    else:
        print("In-valid input")