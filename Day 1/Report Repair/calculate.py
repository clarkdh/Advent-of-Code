#Opening input file
f = open("input.txt", "r")

#Initializing arrays
numbers = []
checker = []

#Adding Numbers to Arrays
for x in f:
    numbers.append(int(x))
    if(int(x) < (2020/3)):
        checker.append(int(x))

#Chechking smaller numbers against both other numbers
for x in checker:
    for y in numbers:
        for z in numbers:
            if (x+y+z) == 2020:
                print (x*y*z)
                break