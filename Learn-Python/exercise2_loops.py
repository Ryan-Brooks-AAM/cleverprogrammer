#import time for sleep
import time

i = int(100)

while i >= 0:
    if i > 5:
        print(i)
        time.sleep(0.3)
    if i <= 5 and i > 0:
        print(f"{i}!!!!")
        time.sleep(1)
    if i == 0:
        print("Happy New Years!!!")
    i = i - 1
        
