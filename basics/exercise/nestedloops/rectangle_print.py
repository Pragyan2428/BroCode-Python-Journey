print("Let's , Print a rectangle !")
rows = int(input("Enter the rows of the rectangle: "))
cols = int(input("Enter the columns of the rectangle : "))
symbol =  input("Enter the symbol: ")
for x in range(rows):
    for y in range(cols):
        print(symbol,end=" ")
    print()