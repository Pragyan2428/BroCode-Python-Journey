#we would be making a game
def Madlibs():
    adj1=input("Enter an adjective(description): ")
    print(f"Today i went to a {adj1} zoo")
    adj2=input("Enter an adjective(description): ")
    print(f"Today i went to a {adj1} zoo and saw a {adj2} animal")
def main():
    print("----Welcome to The Games----")
    print("----Mad Libs Game----")
    print("Press Enter to start the game")
    val=input()
    if(val=="Enter"):
        print("Let's start the game")
        Madlibs()
    else:
        print("Please press Enter to start the game")
        main()
main()