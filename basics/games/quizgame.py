def main():
    print("-----Welcome to the Quiz-----")
    score = 0
    question_bank = ["1. Which keyword is used to define a function in Python? ",
                     "2. Which of the following data types is immutable?",
                     "3. What is the output of the following code?",
                     "4. Which operator is used for exponentiation (power) in Python?",
                     "5. Which loop is used to iterate over a sequence in Python?"]
    answer_bank = ["A. function\nB. define\nC. def\nD. func",
              "A. function\nB. define\nC. def\nD. func",
              "A. <class 'float'>\nB. <class 'int'>\nC. <class 'str'>\nD. Integer",
              "A. ^\nB. *\nC. //\nD. **",
              "A. repeat loop\nB. do-while loop\nC. for loop\nD. until loop"]
    answer = ("C","D","B","D","C")
    guess = []
    choice = input("Press enter to start the game(Q to exit): ")
    name  = input("Enter your name : ")
    
    if(choice.lower() == "q" ):
        return
    
    else:                    
        for ques in range (len(question_bank)):
            print("-------------------------")
            print(f"{question_bank[ques]}" )
            print("-------------------------")

            print(f"{answer_bank[ques]}\n")            
            guess.append(input("What's you guess? "))
            guess[ques] = guess[ques].upper()
            if(guess[ques].upper()== answer[ques]):
                print("You have Guessed it right!.")
                score+=1
            else:
                print(f"Your Guess {guess[ques].upper()} is wrong.")
                print(f"The correct option is : {answer[ques]}.")
            print()
        print(f"Your score: {score}.")
        print(f"Your guesses :{guess}")
        print(f"Correct Answers :{answer}")
main()