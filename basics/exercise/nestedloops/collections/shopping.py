def main():
    shopping_cart = []
    price = []
    quantity = []
    total_amount=0

    print("Welcome to our Store !")
    size=int(input("How many things you want to buy? "))
    for i in range(size):
        shopping_cart.append(input("Enter your item: "))
        price.append(int(input(f"What's the price of {shopping_cart[i]}? ")))
        quantity.append(int(input(f"How many {shopping_cart[i]} have you bought? ")))
        total_amount += price[i]*quantity[i]
        user = input("Do you want to add another item(Yes/No): ")
        user = user.lower()
        
        if(user == "no"):
            size = len(shopping_cart)
            break
        
    print(f"Items purchased: {shopping_cart} ")
    print(f"Prices of the {size} item(s) : {price}")
    print(f"Amount of each item: {quantity}")
    
    
    print("The below is the list of the the items you have purchased and their quantity along with their net cost:")
        
    for last in range(size):
        print(f"{last+1} . Item name : {shopping_cart[last]} Quantity: {quantity[last]} Net Price: {quantity[last]*price[last]} ")
    print(f"Net amount: {total_amount} ")

main()