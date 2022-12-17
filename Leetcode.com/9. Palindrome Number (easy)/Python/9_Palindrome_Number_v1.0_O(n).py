# 9. Palindrome Number
# Solution: Convert integer to a string and use slice() method to reverse the string.
# Cons: We are not allowed to convert to a string



input1 = 121211

if input1 < 0:
    print("This is not a palindrome")
else:
    # Convert to a string
    string1 = str(input1)   # O(n1)

    # The function 'slice' does a slice for each of your string's n suffixes is doing O(n) work.
    string1 = string1[::-1] # O(n)

    # Convert back to an integer as an 'output'
    output1 = int(string1)  # O(n1)

    # Compare both the input and output
    if output1 == input1:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")





""""
PROBLEM DESCRIPTION
--------------------
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