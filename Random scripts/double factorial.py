def factor(mode = True):

    def sf(n):

        s = 1
        i = n
        while i > 1:
            s *= i
            i -= 1
        return s

    def df(x):
        s = 1
        i = x
        while i > 1:
            s *= i
            i -= 2
        return s

    if mode:
        return sf
    else:
        return df

print('5! =', factor()(5))
print('5! =', factor(True)(4))
print('5! =', factor(False)(10))