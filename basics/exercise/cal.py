import math
def arithmatic_calculator(operator):
    
    
    print("How many numbers do you want to calculate? ")
    size = int(input())
    number=[]
    for i in range(size):
        print(f"Please enter a valid number {i+1}: ")
        a = int(input())
        number.append(a)
        
    match operator:
        case 1:
            print("You have selected Addition.")
            sum=0
            for i in range(size):
                sum+=number[i]
            print(f"The sum is: {sum}")
        case 2:
            print("You have selected Subtraction.")
            sub=number[0]
            for i in range(1,size):
                sub-=number[i]
            print(f"The difference is: {sub}")
        case 3:
            print("You have selected Multiplication.")
            prod=1
            for i in range(size):
                prod*=number[i]
            print(f"The product is: {prod}")
        case 4:
            print("You have selected Division.")
            div=number[0]
            for i in range(1,size):
                div/=number[i]
            print(f"The quotient is: {div}")
        case 5:
            print("You have selected Square Root.")
            for i in range(size):
                sqrt=math.sqrt(number[i])
                print(f"The square root of {number[i]} is: {sqrt}")
        case 6:
            print("You have selected Power.")
            for i in range(size):
                print(f"Please enter the power for {number[i]}: ")
                power=int(input())
                pow=math.pow(number[i],power)
                print(f"{number[i]} raised to the power of {power} is: {pow}")
        case 7:
            print("You have selected Factorial.")
            for i in range(size):
                fact=math.factorial(number[i])
                print(f"The factorial of {number[i]} is: {fact}")
        case 8:
            print("You have selected Exponentiation.")
            for i in range(size):
                print(f"Please enter the exponent for {number[i]}: ")
                exp=int(input())
                exp_result=math.exp(number[i])
                print(f"The exponent of {number[i]} is: {exp_result}")
    
def main():
    print("Welcome to the Arithmetic Calculator")
    
    print("Select an operator:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Power")
    print("7. Factorial")
    print("8. Exponentiation")
    print("9. Exit")
    
    operator =int(input("Enter the operator number (1-9): "))
    if operator==9:
        print("Thank you for using the calculator. Goodbye!")
        return
    arithmatic_calculator(operator)

main()