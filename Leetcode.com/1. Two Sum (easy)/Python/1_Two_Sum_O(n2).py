"""
1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]


Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
"""

nums = [5, 14, 18, 38, 54, 100, 102, 567]   # given list of integers
target = 52                                 # target score
exit = False                                # a variable for quitting the loops

# we have 8 elements in a list, range is equal to 8, we iterate 8 times
for i in range(len(nums)):

    # quit loop if target is found
    if exit == True:        
        break;

    # iterate until the the last number
    for j in range(i, len(nums)):

        # These x3 print statements are useless, can be deleted, only used for explaining how the loops work
        print("i is qual to: ", nums[i], ", j is equal to: ", nums[j])
        print("Index: ", i, ", plus index: ", j)
        print("")

        # Exit the two loops if target is found and print the results
        if nums[i] + nums[j] == target:
            print("The solution is: ", "i is qual to: ", nums[i], "j is equal to: ", nums[j])
            print("The solution is: ", "list index ", i, " plus list index: ", j)
            exit = True
            break;