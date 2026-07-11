import time
import random
def main():
    guess= []
    tries = []
    print("---------Welcome to Rock Paper Scissors---------")
    options = ("rock","paper","scissors")
    print("Let's Play:")
    while(True):
        user = input("Press Enter to start the game(q to quit): ")
        ans = random.choice(options)
        if(user.lower() == "q"):
            print("Thank you for your time.")
            break
        Guess = input("What's your guess: ")
        guess.append(Guess)
        print("Get ready:")
        if (Guess.lower() == ans):
            print("Congratulations!!!")
            print("You have guessed it right.")
            choose = input("Wanna play again?(Yes/No): ")
            if(choose.lower() == "no"):
                print("Thank you for playing.\nHope you had fun!")
                break
            else:
                continue
            
        else:
            print("You have guessed it wrong.")
            print(f"It's {ans}")
            choose = input("Wanna try again?(Yes/No): ")
            if (choose.lower() == "no"):
                print("Thank you for playing")
        
        
main()