import math as m
from math import *
num = input('Факториал какого числа, Вы желаете вычислить?: ')

try:
    def my_factorial(n):
        x = 1
        mult = 1

        while x < n+1:

            mult *= x
            print('Факториал числа %d =' % x,mult)
            x += 1
        return mult

    num = int(num)
    my_factorial(num)

except TypeError:
    print("Вы ввели буквы в поле для чисел")

except ValueError:
    print("Вы ввели буквы в поле для чисел")