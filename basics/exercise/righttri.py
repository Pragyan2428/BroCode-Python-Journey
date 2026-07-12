import math
def main():
    print("Find the Hypotenuse: ")
    p=float(input("What's the perpendicular? "))
    b=float(input("What's the base? "))
    h=math.hypot(p, b)
    print(f"The hypotenuse is: {h}")
main()