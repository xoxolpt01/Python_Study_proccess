def Fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
print('Fibonachi`s numbers:')
for i in range(1, 16):
    print(Fib(i), end = ' ')