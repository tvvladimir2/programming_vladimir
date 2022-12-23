# 4_14_longest_common_prefix
# SOLUTION: Check each letter of the first item for each other item
# CONS: O(n2) - quadratic time complexity.


def new_func(strs):
    prefix = ""
    firstWord = strs[0]
    truth = True
    letterNumber = 0

    for i in firstWord: # i = f, l, o, w, e, r
        for y in strs:
            if y[letterNumber] == i:
                truth = True
            else:
                truth = False
                break
        if truth == True:
            prefix += i
            letterNumber += 1
        else:
            break
    return prefix


strs = ["flower","flow","flight"]

result = new_func(strs)
print(result)


