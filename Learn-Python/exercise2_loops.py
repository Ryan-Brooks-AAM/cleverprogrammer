#import time to slow counting so I can visualize the loop
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
        

print("Oh yea we forgot the explosion..")

x = 100
while x > 0:
    print(x)
    x -= 1
else:
    print("Kaboom.")
