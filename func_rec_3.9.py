
def rec_1(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2

    else:
        return rec_1(n-1)+rec_1(n-3)


for k in range(0,10):
    print(rec_1(k))