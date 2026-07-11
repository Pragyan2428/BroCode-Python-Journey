def main():
    menu={
        "Rice": 60,
        "Wheat Flour": 45,
        "Milk": 58,
        "Bread": 35,
        "Eggs": 90,
        "Butter": 280,
        "Sugar": 48,
        "Salt": 22,
        "Cooking Oil": 165,
        "Tea": 140,
        "Coffee": 180,
        "Biscuits": 25,
        "Apples": 180,
        "Bananas": 70,
        "Tomatoes": 40
    }
    user = ""
    cart = []
    amt = 0
    total = 0
    
    print("-------Menu -------")
    for key,value in menu.items():
        print(f"{key} : ${value:^5}")
    print("-------------------")
    while(True):
        user = (input("What do you want to buy? ").lower()).title()
        if user in menu :
            amt = int(input("How many do you want to buy ? "))
            cart.append((user,amt))
            total += (amt * menu.get(user))
        else:
            print(f"{user} is not present in the menu.")
        choice = input("Do you want to buy another item? (yes/no): ").lower()

        if choice == "no":
            break
    print("\n========== RECEIPT ==========")

    for item, qty in cart:
        net = qty * menu[item]
        print(f"{item:<20} Qty: {qty:<3} Cost: ₹{net}")

    print("-" * 30)
    print(f"Total Amount: ${total}")
    
main()