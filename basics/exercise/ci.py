import math
name = input("What's your name? ")
print(f"Hello , {name}")

principle = 0
rate = 0
time = 0
result = 0
n = 12
while(principle<=0):
    principle = float(input("How much is the principle amount? "))
    if(principle<=0):
        print("Principle amount cannot be less than or equal to zero.")
        
while(rate<=0):
    rate = float(input("How much is the interest rate amount? "))
    if(rate<=0):
        print("Rate amount cannot be less than or equal to zero.")
while(time<=0):
    time = float(input("How much is the time ? "))
    if(time<=0):
        print("Time amount cannot be less than or equal to zero.")
        
rate=float((rate)/(100*n))
rate  = float(math.pow(1+rate,n*time))
result = principle*rate
print(f"Your final amount is {result:^10.2f}")