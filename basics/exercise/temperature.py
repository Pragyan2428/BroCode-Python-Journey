def temp_cal(fromconvert, temp, toconvert):
    user = fromconvert.lower()
    to = toconvert.lower()

    if user == "kelvin":
        if to == "celsius":
            result = temp - 273.15
            return result
        elif to == "fahrenheit":
            result = (temp - 273.15) * 9/5 + 32
            return result
        elif to == "kelvin":
            return temp
        else:
            return "Invalid conversion."

    elif user == "celsius":
        if to == "kelvin":
            result = temp + 273.15
            return result
        elif to == "fahrenheit":
            result = (temp * 9/5) + 32
            return result
        elif to == "celsius":
            return temp
        else:
            return "Invalid conversion."

    elif user == "fahrenheit":
        if to == "celsius":
            result = (temp - 32) * 5/9
            return result
        elif to == "kelvin":
            result = (temp - 32) * 5/9 + 273.15
            return result
        elif to == "fahrenheit":
            return temp
        else:
            return "Invalid conversion."

    else:
        return "Invalid temperature scale."
        
def main():
    choice1 = input("What do you want to choose (celsius/kelvin/faherenhite)?\n ")
    
    temp=float(input("Enter the temperature in Celsius: "))
    
    choice2 = input("In which temperature do you want to convert?\n ")
    
    result = temp_cal(choice1 , temp , choice2)
    
    print(f"Your desired output : {result}")
    
main()