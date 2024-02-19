"---------------------------------------------------------------------------------------------------------------------------------------"

import random, os
from gpiozero import Button
from time import sleep

BtnInput = Button(2)
# The integer passed into the function is the GPIO pin the button is connected to

"---------------------------------------------------------------------------------------------------------------------------------------"

def InputPressed():
    ChanceInt = random.randint(1,1000)
    # Random number between 1 and 1000 to act as where in the range

    if ChanceInt <= 970:
        os.system("lp SadFaceImage.png")
    
    else:
        os.system("lp SmileyFaceImage.png")
    # Prints the correct image for the result... MAKE SURE IMAGE FILES IN SAME DIR AS .PY!!!!!!
    
    # If the random integer is in the bottom 970 values (lower 97%), it will return False, otherwise it returns True

"---------------------------------------------------------------------------------------------------------------------------------------"

BtnInput.when_released = InputPressed

"---------------------------------------------------------------------------------------------------------------------------------------"

try:
    while True:
        sleep(0.1)
        # This is so the CPU doesn't overload when left idle

except KeyboardInterrupt:
    # KeyboardInterrupt is activated on the press of ctrl+C (sometimes ctrl+Z)
    print("User has terminated program.")

"---------------------------------------------------------------------------------------------------------------------------------------"
