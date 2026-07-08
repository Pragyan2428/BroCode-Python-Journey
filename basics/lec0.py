#Ask user for the name
name=input("What's your name? ")

#says hello to the user
print("Hello,",name+"!")
sal=input("How much do you earn? ")
#calculates the tax
tax=0.2*float(sal)
print(f"You have to pay {tax:,} as tax.")

print(f"{tax:,}")#helps to format the number with commas as thousands separators
z=round(float(sal)+float(tax))
print(f"Total amount: {z:,}")