def happy_birthday(user):
    while(user>0):
        print("Happy brithday")
        user-=1
def  main():
    user = int(input("Enter the number of happy birthdays:"))
    happy_birthday(user)
    
main()