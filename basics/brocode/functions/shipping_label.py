def shipping_label(*args,**kwargs):
    print("Hello, ",end=" ")
    for arg in args:
        print(arg , end =" ")
        
    print()
    
    print("Your address :")
    print("Area: ",end=" ")
    if "street" in kwargs:
        print(f"{kwargs.get('area')},{kwargs.get('street')}")
    if "pobox" in kwargs:
        print(f"Pobox: {kwargs.get('pobox')}")
    if "area" in kwargs:
        print(f"{kwargs.get('area')}")
    
    
def main():
    
    shipping_label("Pragyan","Singh",
                   area="Avas-Vikas 3",
                   street = "Lig 3146" ,
                   city = "Kanpur",
                   pobox = "ptanhi",
                   state="Uttar Pradesh",
                   pincode=1234)
    
main()