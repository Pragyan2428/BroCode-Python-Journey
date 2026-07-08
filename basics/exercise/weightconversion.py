def country(val):
    if val == "india":
        print("You are from India.")
        weight =float(input("What's your weight in kg? "))
        return weight
    elif val == "usa":
        print("You are from USA.")
        weight = float(input("What's your weight in pounds? "))
        return weight
    elif val == "uk":
        print("You are from UK.")
        weight = float(input("What's your weight in stones? "))
        return weight
    else:
        print("We are not available in your country.")

def weight_converter(weight,country,scale):
    if country == "india":
        
        if scale == "pounds":
            print(f"Your weight in pounds is: {round(weight * 2.20462)}")
        elif scale == "stones":
            print(f"Your weight in stones is: {round(weight * 0.157473)}")
        else:
            print(f"Your weight in kg is: {round(weight)}")
    elif country == "usa":
        if scale == "kg":
            print(f"Your weight in kg is: {round(weight * 0.453592)}")
        elif scale == "stones":
            print(f"Your weight in stones is: {round(weight * 0.0714286)}")
        else:
            print(f"Your weight in pounds is: {round(weight)}")
    elif country == "uk":
        if scale == "kg":
            print(f"Your weight in kg is: {round(weight * 6.35029)}")
        elif scale == "pounds":
            print(f"Your weight in pounds is: {round(weight * 14)}")
        else:
            print(f"Your weight in stones is: {round(weight)}")

def main():
    choice = input("Where are you from? ")
    
    user_input = choice.lower()
    
    weight = country(user_input)

    user_scale = input("In which scale do you want to convert your weight? (kg, pounds, stones): ")
    
    weight_converter(weight, user_input, user_scale)
    
    print("Thank you for using the weight converter!")
    
main()