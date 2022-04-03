from itertools import permutations

my_string = 'grisha'

result = permutations(my_string)

print(result)
print('Number of variations is: ', len(list(result)))
print(list(result))

# a = 6**6
# print(a)
