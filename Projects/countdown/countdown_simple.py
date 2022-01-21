import time

seconds = int(input("How many seconds to count?" + "\n" + "> "))

# Example 1
for x in range(seconds):
    print(str(seconds - x) + " seconds remaining")
    time.sleep(1)

print("\n" + "First part finished")
time.sleep(1)
print("Starting the second part" + "\n")
time.sleep(1)

# Example 2
for x in range(seconds):
    seconds -= 1
    print(str(seconds) + " seconds remaining... and counting...")
    time.sleep(1)
