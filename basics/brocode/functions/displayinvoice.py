def display_invoice(name,amount,date,month,year):
    print(f"Hello, {name}.")
    print(f"You have {amount}.")
    print(f"Your due date is {date}/{month}/{year}.")


def main():
    name = input("Enter your name: ")
    amt = int(input("Enter you amount: "))
    print("Enter the date : ")
    date= int(input("Date: "))
    month= input("Month: ")
    year= int(input("Year: "))
    
    
    display_invoice(name,amt,date,month,year)
main()