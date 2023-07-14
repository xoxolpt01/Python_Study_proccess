def ex3_11(n):
    if  n == 0 or n == 1:
        return 1
    elif n == 2:
        return 6
    else:

        return ex3_11(n -1)+ex3_11(n-2)+ ex3_11(n-3)

for i in range(0,10):
    print(ex3_11(i))