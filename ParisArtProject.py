import random

def ButtonPressed():
    ChanceInt = random.randint(1,1000)
    # Random number between 1 and 1000 to act as where in the range

    if ChanceInt <= 970:
        return "chances say you have been sexually assaulted."
    
    else:
        return "chances say you have not been sexually assaulted."
    
    # If the random integer is in the bottom 970 values (lower 97%), it will return "you have" string. Else, will return "you haven't" string.

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# This is the test loop if you wish to confirm that the chance of each reply is correct

"""
countN = 0
countY = 0
for i in range(0,100):
    if ButtonPressed() == "chances say you have not been sexually assaulted.":
        countN += 1

    else:
        countY += 1

print(f"{countN} haven't, and {countY} have.")

"""