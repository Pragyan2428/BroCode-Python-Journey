# Return : this is a statement which basically return back the value to caller.
def add (x,y):
    z=x+y
    return z
def subs (x,y):
    if(x>y):
        z=x-y
    else:
        z=y-x
    return z
def multiply (x,y):
    z=x*y
    return z
def divide (x,y):
    if(x>y):
        z=x/y
    else:
        z=y/x
    return z


def main():
    a =int(input("Enter the First number: "))
    b =int(input("Enter the Second number: "))
    print(add(a,b))
    print(subs(a,b))
    print(divide(a,b))
    print(multiply(a,b))
    
    
main()
