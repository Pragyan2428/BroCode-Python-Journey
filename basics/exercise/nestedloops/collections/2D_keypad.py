print("--- This is your Keypad ---")
keypad = ((1 , 2 , 3),
          (4 , 5 , 6),
          (7 , 8 , 9),
          ("*" , 0 , "#"))
for row in keypad:
    for keys in row:
        print(f"{keys:^5}", end="")
    print()