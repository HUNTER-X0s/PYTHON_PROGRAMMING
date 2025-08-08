# THE PERFECT GUESS

# We are going to write a program that generates a random number and asks the user to guess it.

# if the player's guess is higher than the actual number, the program displays "lower number please" when the user guesses the correct number, the program displays the number of  guesses the player used to arrive at te number.

from random import randint

while True:
    
    computerNo = randint(1,100)

    print("🎮 Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 100 \n  You have 10 attempts.")

    guesses = 0
    userNo =  -1

    while(userNo != computerNo):  

        if(guesses >= 10):
            print(f"Too many attempts! The correct number was {computerNo}. Better luck next time.")
            break

        try:
            userNo = int(input("Guess a number between (1-100): "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue 

        if(userNo < 1 or userNo > 100):
            print("⚠️  Please enter a number between 1 and 100.")
            continue

        guesses += 1
        attempts_left = 10 - guesses

        if(userNo > computerNo):
            print(f"Lower number please.\nAttempts left: {attempts_left}")
            
        elif(userNo < computerNo):
            print(f"Higher number please.\nAttempts left: {attempts_left}")

        else:
            print("HOORAYY!! \n You have entered the correct number!!" + "\n" + f"You have guessed the number {computerNo} correctly in {guesses} attempts")
            break   

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! 👋")
        break
    

