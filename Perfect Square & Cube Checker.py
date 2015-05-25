"""
Our Aim is to check whether the  given "number" is a perfect square as well as a perfect cube or not.
"""
def cuber(num):  # Calculates whether the given number is a perfect cube or not.
    inte = int(round(num**(1/3.0000000)))
    if num == inte**3:
        return True
    else:
        return False

def squarer(num):  # Calculates whether the given number is a perfect square or not.
    inte = int(round(num**(1/2.0000000)))
    if num == inte**2:
        return True
    else:
        return False

def check(num):  # Our Aim.
    if cuber(num) == True and squarer(num) == True:
        print "%s satisfies BOTH." % num
    else:
        return False

"""
num = raw_input("Enter a number: ")
check(int(num))
"""  # Manual Printing through user input.

for num in range(0, 200000):  # Loop to calculate numbers which are both perfect cube and squares.
    check(int(num))

"""

Well, there's also another idea, instead of calculating both one half and one third powers and then making
both true, we could have calculated the one sixth power and make it true instead. One Calculation. Same Results.
Isn't it obvious!

~A. Pathak

"""
