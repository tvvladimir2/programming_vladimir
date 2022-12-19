# 13. Roman to Integer

"""
class Solution:
    def romanToInt(self, s: str) -> int:
"""

s = "MCMXCIV"
s = "MCMXCIV"
s2 = s

a = "I"
b = "V"
c = "X"

loop_number = 0
total_number = 0
multiplier = 1
number_of_digits = 0

def letter_symbol_change():
    global a
    global b
    global c
    if a == "I":
        a = "X"
        b = "L"
        c = "C"
    elif a == "X":
        a = "C"
        b = "D"
        c = "M"
    elif a == "C":
        a = "M"
        b = "V"
        c = "X"

# Iteration cycle: Ones, Tens, Hundreds, Thousands, ...
while len(s2) > 0:
    if s2[-1] == a:
        loop_number += 1
        number_of_digits += 1
        if len(s2) > 1 and s2[-2] == a:
            loop_number += 1
            number_of_digits += 1
            if len(s2) > 2 and s2[-3] == a:
                loop_number += 1
                number_of_digits += 1
                if len(s2) > 3 and s2[-4] == b:
                    loop_number = loop_number + 5
                    number_of_digits += 1
            elif len(s2) > 2 and s2[-3] == b:
                loop_number = loop_number + 5
                number_of_digits += 1
        elif len(s2) > 1 and s2[-2] == b:
            loop_number = loop_number + 5
            number_of_digits += 1
    elif s2[-1] == b:
        loop_number += 5
        number_of_digits += 1
        if len(s2) > 1 and s2[-2] == a:
            loop_number -= 1
            number_of_digits += 1
    elif len(s2) > 1 and s2[-1] == c and s2[-2] == a:
            loop_number += 9
            number_of_digits += 2
    
    # Test total
    print("number of digits: ", number_of_digits)
    print("multiplier: ", multiplier)
    print("loop_number: ", loop_number)
    print("total number = ", total_number, "+ ", loop_number, "* ", multiplier)
    print("")
    total_number = total_number + loop_number * multiplier
    print("total number: ", total_number)


    # Prepare numbers and letters for the next itteration
    multiplier *= 10
    letter_symbol_change()
    loop_number = 0
    while number_of_digits > 0:
        s2 = s2[:-1]
        number_of_digits -= 1




