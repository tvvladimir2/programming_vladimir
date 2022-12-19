# 9. Palindrome Number
# Solution: Calculate amount of digits in the integer. Find each digit at the front and move it backwards.
# Cons: Uses Math module function.


import math

input1 = 123456654321
medium1 = input1
output1 = 0

# Determine how many digits in 'medium1'
input1Digits = int(math.log10(medium1))+1    # 6

for i in range((input1Digits)):

    # Find the first number
    # Round numbers down to the nearest integer
    x = math.floor(medium1/10**(input1Digits-1))
    print("digit = ", x)

    # Manipulate the output
    output1 += x * 10**i
    print("output1 = ", output1)

    # Manipulate the medium1
    medium1 -= x * 10**(input1Digits-1)
    print("medium1 = ", medium1)

    # Manipulate the 'input1Digits'
    input1Digits -= 1
    print("input1Digital = ", input1Digits)
    print("")

if input1 == output1:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")





""""
PROBLEM DESCRIPTION
---------------------
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.


Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 
Constraints:

-231 <= x <= 231 - 1

 
Follow up:

Could you solve it without converting the integer to a string?
"""

