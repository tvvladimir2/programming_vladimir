import time

var_start_time = time.time() # returns seconds
var_start_time = time.process_time() # Excludes sleep time
# var_start_time = time.time_ns() #Nano seconds per second, returns an integer

# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.
# Syntax: string.join(iterable)
# Documentation: https://www.w3schools.com/python/ref_string_join.asp
# myDict = {"name": "John", "country": "Norway"}
# mySeparator = "TEST"
# x = mySeparator.join(myDict)

n = "-".join(str(i) for i in range(10000))
time.sleep(2) # Show if time.process_time() excludes sleep time
# format.(x, '.yf')
# format function (not method) with a second parameter allowed to specialize the formatting of objects as strings.
# the results are rounded not truncated:
# The formatting string '.5f' means round to 5 places after the decimal point.
# This format function returns the formatted string. It does not change the parameters.
# As a complete statement in a program format(x, '.2f'), is useless: The '23.46' gets returned and thrown away, with no effect on x.
var_elapsed_time = format(time.time() - var_start_time, '.100f')
# 1 × 10^9"one times ten to the ninth power"
# var_elapsed_time = float(time.time_ns() - var_start_time/1e9)

print(n)
print(var_elapsed_time)
