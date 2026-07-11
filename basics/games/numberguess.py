import random

import time
def main():
    print("-----Welcome to the Number Guess Game-----")
    print("Define your limits: ")
    low = int(input("What is the lower limit of number you want to select from? "))
    high = int(input("What is the upper limit of number you want to select from? "))
    library = random.randint(low,high)
    guess = []
    count = 0
    while(True):
        print("You will get 3 seconds to guess.")
        query = input("Press Enter to continue (q to quit): ")
        if query.lower() == "q":
            print("Thank you!!")
            print(f"The correct answer is {library}")
            print(f"Tries : {count}")
            break
        print("Your time starts now: ")
        for i in range(3,0,-1):
            print(i)
            time.sleep(1)
        user = int(input("Guess: "))
        count+=1
        
        
        guess.append(user)
        

        difference = library - user
        
        if user == library:
            
            print("Congratulations, You have guessed it right!")
            print(f"You have guessed it on the {count} try.")
            
            break
        else:
            print("You have guessed it wrong.")
            choice = input("Wanna try again?(Yes/No): ")
            if(choice.lower() == "no"):
                print("Thank you !")
                print(f"The correct answer is {library}")
                print(f"Tries: {count}")
                break
            if(difference<0):
                print("You are ahead of the original number.")
            else:
                print("You are behind the original number.")
    extra = input("Do you wanna know your guesses? ")
    if(extra.lower() == "yes"):
        print(guess)
    else:
        print("Thank you for your time.")
main()