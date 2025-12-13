print("Hello welcome to mey game guess the number")
import random
number = random.randint(1, 100)
guess = None
attempts = 1000
while guess != number and attempts > 0:
    guess = int(input("Enter your guess between 1 and 100: "))
    attempts -= 1
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number} correctly!")
        break
    print(f"You have {attempts} attempts left.")
if attempts == 0:
    print(f"Sorry, you've run out of attempts. The correct number was {number}.")
print("Thank you for playing! Goodbye!")