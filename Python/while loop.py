# WHILE LOOPS

# A loop is a construct.
# A while loop is used to repeat a block of code multiple times.
# The while loop is used in cases when the number of iterations is not known and depends on some calculations and conditions in the code block of the loop.

# SYNTAX STRUCTURE
while Condition:    # expression that returns True or False
    statement 1     # /Body starts. Statements are executed as long as the condition is true
    statement 2     # loop statement must be properly indented
    ...
    statement n     # /Body of statements stops
else:               # Else block is optional
    statement(s)    # execute only when while loop executes normally

# BREAK STATEMENT
while True:
    if x == 0:
        break       # break a while loop prematurely
    else:
        continue    # jumps back to the top of the loop to the next itteration

# INFINITE LOOPS
while True:
    print('forever')

# Example: Count from 1 to 5:
i = 1
while i <=5:
    print(i)
    i += 1      # need to accrument i manually
