# 9. Palindrome Number
# Solution: Используем деление от остатка начиная с последней цифры



input1 = 12321
middle1 = input1
output1 = 0

if input1 < 0:
    print("not a palindrome")
elif input == 0:
    print("palindrome")

while middle1 >= 1:
    output1 = output1*10 + middle1 % 10
    middle1 = round(middle1 / 10, 0)

if output1 == input1:
    print("palindrome")
else:
    print("not a palindrome")





""""
PROBLEM DESCRIPTION
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


