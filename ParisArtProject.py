import random
from gpiozero import Button

BtnInput = Button(2)
# The integer passed into the function is the GPIO pin the button is connected to

def ButtonPressed():
    ChanceInt = random.randint(1,1000)
    # Random number between 1 and 1000 to act as where in the range

    if ChanceInt <= 970:
        return True
    
    else:
        return False
    
    # If the random integer is in the bottom 970 values (lower 97%), it will return False, otherwise it returns True
    
BtnInput.when_released = ButtonPressed
