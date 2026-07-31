def full_name(firstname,last_name):
    full_name = firstname+last_name
    print(f"Your full name :{firstname} {last_name}.")
    
def main():
    firstname = input("Enter your first name: ").capitalize()
    lastname = input("Enter your last name: ").capitalize()
    
    full_name(firstname,lastname)
main()