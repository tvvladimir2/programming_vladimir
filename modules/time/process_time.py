# Python program to show time by process_time()
import time
from time import process_time       # in seconds
from time import process_time_ns    # in nanoseconds
# Start the stopwatch / counter

# Start timer in seconds or nanoseconds
# t1_start = process_time() # seconds
t1_start = process_time_ns() # in nanoseconds

# execute code to test processing time, any code
x = 0
for i in range(0,1000000):
    x+=1

# Stop the stopwatch / counter
t1_stop = process_time_ns()

# Display total time
print(t1_start, " Start time")
print(t1_stop, " Stop time")
print("Elapsed processing time", t1_stop-t1_start)
