


def fib(n):
    k = 0
    f_0 = 0
    f_1 = 1
    ls = []
    while k < n:
        f_n = f_1 + f_0
        f_0 = f_1
        f_1 = f_n

        k += 1
        ls.append(f_n)
    ls.pop(-2)
    return ls

print(fib(6))
