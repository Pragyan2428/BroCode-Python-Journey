def main():
    country={"USA":"Washington D.C.",
             "INDIA": "Delhi",
             "CHINA": "Beijing",
             "RUSSIA": "Moscow"
    }
    
    print(country)
    print(country.get("INDIA"))#This way we can get the value from the dictionary using the key
    print(country.get("Delhi"))#prints none as we can only get the value not key (other way around)
main()