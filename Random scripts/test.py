try:
    a = input('a=?:')
    b = input('b=?:')

    a = float(a)
    b = float(b)
    x = b / a

    print('Уравнение решено x =' + str(x))

except ZeroDivisionError:
    print('division by ZERO inposible')

except ValueError:
    print('write please numer')