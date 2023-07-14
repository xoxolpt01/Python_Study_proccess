
try:
    a = input('a=?:')
    b = input('b=?:')

    a = float(a)
    b = float(b)
    x = b/a

    print('Уравнение решено x ='+str(x))

except:
    if type(a) and type(b) == str:

        print('Введены некорректные символы')
    elif int(a) == 0:
        print('деление на "0" невозможно')


#Второй метод обработки данных (более эффективнее)
"""

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
"""