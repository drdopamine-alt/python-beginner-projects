import time 
import winsound 
s = int(input("Enter your time in second: "))
while s > 0:
    m = s//60
    sec = s%60
    print(f'{m}:{sec}')
    time.sleep(1) # Time handling 
    s -= 1
print("Time's up!")
winsound.Beep(500,500)