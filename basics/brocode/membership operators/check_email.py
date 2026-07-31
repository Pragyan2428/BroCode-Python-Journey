def main():
    email = input("Enter you mail: ")
    if '@' and '.' in email:
        print("Your email is valid.")
    else:
        print("Your email is not valid.")

main()