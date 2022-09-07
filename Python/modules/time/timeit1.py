# CALCULATE PROGRAM LAPSED TIME

# Method 1 ################################
import timeit

print(timeit.timeit('"-".join(str(i) for i in range(10000))', number=5)) # number = 5 , number of items I want to run it.

# Method 2 ###############################
import timeit

var_start_time = timeit.default_timer() # returns seconds
n = "-".join(str(i) for i in range(10000))
var_elapsed_time = format(timeit.default_timer() - var_start_time, '.100f')

print(var_elapsed_time)

# Method 3 ###############################
import datetime

var_start_time = datetime.datetime.now() # returns seconds
n = "-".join(str(i) for i in range(10000))
# var_elapsed_time = (datetime.datetime.now() - var_start_time).total_seconds() # Displays in 00:00:00.000000 format
var_elapsed_time = (datetime.datetime.now() - var_start_time).total_seconds() # Displays in seconds

print(var_elapsed_time)
