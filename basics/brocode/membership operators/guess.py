def main():
    word = "APPLE"
    guess =  input("Guess the letter: ").capitalize()
    
    if guess in word:
        print(f"The letter {guess} is in the word.")
    else:
        print(f"The letter {guess} is not found.")

main()