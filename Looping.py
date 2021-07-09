import time
# import sys

a=1000

def main():
    global a
    a += 1
    print(a)
    time.sleep(1)
    if a==1005:
        return
        # sys.exit()
    main()

main()

print('first part finished')

while a<=1009:
    a += 1
    print (a)
    time.sleep(0.5)
