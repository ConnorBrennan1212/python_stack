# Basic
for i in range(0, 151):
    print(i)

# multiples of 5 up to 1000
for i in range(0, 1001, 5):
    print(i)

# dojo way
for i in range (0, 101, 1):
    if i % 10 == 0:
        print("Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

#huge
huge = 0
for i in range (1, 500000, 2):
    huge = huge + i

# print(huge)

# countdown by fours
for i in range (2018, 0, -4):
    print(i)

# Flexible counter
lownum = 2
highnum = 100
mult = 3
for i in range (lownum, highnum+1):
    if i % 3 == 0:
        print(i)
