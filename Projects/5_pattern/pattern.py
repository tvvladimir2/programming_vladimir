# Tutorial from
# https://www.youtube.com/watch?v=k8SXsT5TLxQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=32
# #23 Python Tutorial for Beginners | Printing Patterns in Python
# In this video we will see:
# - Printing patterns
# - Using loop
# - For loop

# print("324234243", end="MUSIC")
# print("sfdsdfadasd")
# \n

# Method 1 #######################
print("# # # #" + "\n" + "# # # #" + "\n" +"# # # #" + "\n" +"# # # #" + "\n")

# Method 2 #######################
for i in range(4):
    print("# # # #")

# Method 3 #######################
for j in range(4):
    for i in range(4):
        print("# ", end="")
    print(" ")

#Exercise 1 #######################
# Print the following:
#
# #
# # #
# # # #
for j in range(4):
    for i in range(j+1):
        print("# ", end="")
    print(" ")
# j=0, i=1
# j=1, i=2
# j=2, i=3
# j=3, i=4

#Exercise 2 #######################
# Print the following:
# # # #
# # #
# #
#
for j in range(4):
    for i in range(4-j):
        print("# ", end="")
    print(" ")

# j=0, i=4
# j=1, i=3
# j=2, i=2
# j=3, i=1
