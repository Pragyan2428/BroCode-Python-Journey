def username(username):
    Name = name(username)
    Spaces = spaces(username)
    Digits = digits(username)
    
    if Name and Spaces and Digits:
        print("Username is valid.")
    else:
        print("Username is not valid.")

def name(username):
    length = len(username)
    if length >12:
        print("Username should be of 12 characters or less .")
        return False
    return True

def spaces(username):
    space = username.count(" ")
    if space > 0:
        print("Username should not contain spaces. ")
        return False
    return True
    
def digits(username):
    digit = username.isdigit()
    if digit >0:
        print("The Username should not contain digits. ")
        return False
    return True
def main():
    user_name = input("Enter your username: ")
    username(user_name)

main()