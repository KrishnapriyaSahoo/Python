import time
my_time=int(input("Enter the time in seconds:"))
for x in range(my_time,0,-1):
    seconds=x%60
    minutes=int(x/60)%60
    hours=int(x/3600)
    print(f"00:{minutes:02}:{seconds:02}")#2 means after:2 numbers will show like 03,15,etc  if seconds:01 then numbers will be 3,5,etc
    time.sleep(1)
print("TIME'S UP!")
