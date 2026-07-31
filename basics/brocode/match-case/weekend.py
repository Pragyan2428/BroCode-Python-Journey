def is_weekend(day):
    match day:
        case 1:
            pass
        case _:
            #default case or a wild card.
def main():
    day = input("Enter the day of the week: ")
    is_weekend(day)
    
main()