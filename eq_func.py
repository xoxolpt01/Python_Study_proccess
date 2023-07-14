def paired(a):
    s = 0

    for i in range(1, a+1):
        s += 2
        k = print(s)
    return k

#!!!
new_def = paired
print(paired(10))
print()
print(new_def(16))