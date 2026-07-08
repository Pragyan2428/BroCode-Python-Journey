import math
def main():
    pi=math.pi
    radius=float(input("Enter the radius of the circle:"))
    circumference=round(2*pi*radius, 2)
    sq_r=math.pow(radius, 2)
    area=round(pi*sq_r, 2)
    print(f"The circumference of the circle is: {circumference}")
    print(f"The area of the circle is: {area}")

main()