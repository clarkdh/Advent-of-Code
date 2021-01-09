#Opening input file
f = open("input.txt", "r")

#initalizing arrays
low = []
high = []

for x in f:
    #Increment for midpoint case
    i = 0

    #Adding low values to low array and checking each value against high array
    if int(x) > 1010:
        high.append(int(x))
        for y in low:
            if int(x) + y == 2020:
                print(str(x) + ' ' + str(y) + ' ' + str(int(x)*y))
                break
    
    #Adding high values to high array and checking each value against low array
    if int(x) < 1010:
        low.append(int(x))
        for j in high:
            if int(x) + j == 2020:
                print(str(x) + ' ' + str(j) + ' ' + str(int(x)*j))
                break
    
    #Checking midpoint condition        
    else:
        i += 1
        if i == 2:
            print(1910*1910)
            break

#Closing input file
f.close()