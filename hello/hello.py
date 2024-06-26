import numpy as np

import numpy as np

def roll_dice():
    msg = "Roll a dice"
    print(msg)

    roll1 = np.random.randint(1,6)
    print("roll1 = ", roll1)

    roll2 = np.random.randint(1,6)
    print("roll2 = ", roll2)

    print(roll1 + roll2)

def print_hello():
    print("Hello")

# Call the function
roll_dice()

