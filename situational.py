import random

def cooking_simulation():
    while True:
        name=input("What is your name")
        print(f" hello {name}")
        print(" Welcome to the Cooking Guess Game!")
        print("You are making pancakes. Guess how they will turn out:")
        
        guess = input("Will they be (1) Perfect, (2) Burnt, or (3) Undercooked? Enter 1, 2, or 3: ")
        
        if guess not in ["1", "2", "3"]:
            print(" Invalid choice! Please enter 1, 2, or 3.")
            continue  
        
        print(" You start cooking the pancakes...")
        
        actual_outcome = random.choice(["1", "2", "3"])  
        
        outcomes = {
            "1": " They are golden brown and fluffy! Perfect!",
            "2": " Oh no! You left them too long. They're burnt!",
            "3": " Oops! They're still raw inside. Undercooked!"
        }
        
        print(f"\n Actual result: {outcomes[actual_outcome]}")
        
        if guess == actual_outcome:
            print("You guessed it right!")
        else:
            print("Better luck next time!")

        play_again = input(" Do you want to try again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print(" Thanks for playing! See you next time!")
            break  

cooking_simulation()

