import time
user_time = int(input("Enter the time(in seconds) : "))
print("Your time left is :")
for i in reversed(range(user_time+1)):
    sec = i%60
    min = (int)(i/60)%60
    hour = (int)(i/3600)
    time.sleep(1)
    print(f"{hour:02}:{min:02}:{sec:02}")
    
print("Time'Up!")