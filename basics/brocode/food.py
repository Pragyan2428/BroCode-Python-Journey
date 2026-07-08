def main():
    response = input("Do you want food? ")
    
    user_response = response.lower()
    
    if response==user_response:
        print("You said yes!")
    else:
        print("Thank you for your response.")