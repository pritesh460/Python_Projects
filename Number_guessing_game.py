import random

print("Hi ! welcome to number guessing game \nYou have 7 chances to guess the number. Let's start")

low = int(input("Enter Lower bound:"))
high = int(input("Enter Upper bound:"))

print(f"\nYou have 7 chancen to guess the number between {low} and {high}.")

num = random.randint(low ,high)

ch = 7
gc = 0

while gc < ch:
    gc += 1
    guess = int(input("Enter your guess:"))

    if guess == num:
        print(f"Correct! The number is {num}. \nYou guessed it in {gc} attempts")
        break
    elif gc >= ch and guess != num:
        print(f"sorry! The number was {num}. Better luck next time.")
    elif guess > num:
        print("Too high! Try a lower number.")
    elif guess < num:
        print("Too low! Try a higher number.") 