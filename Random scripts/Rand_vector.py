import copy
from random import *

"""
прога расчитана на расчет скалярного произведения
2х рандомных векторов
"""


question = int(input('Измеримость вектора_1: '))
question_2 = int(input('Измеримость вектора_2: '))

def rand_vector(x):
    i = 0
    a = []
    while i < x:
        #r = randint(-100, 100)
        r = randint(0, 10)
        a.append(r)
        i += 1
    # j = 0
    # while j < x:
    #     r = randint(0, 10)
    #     b.append(r)
    #     j += 1

    return a


'''
print('type:', type(rand_vector(question)))
print('a = ', rand_vector(question)[0])
print('b = ', rand_vector(question)[1])
'''

a_n = copy.deepcopy(rand_vector(question))
b_n = copy.deepcopy(rand_vector(question_2))

def show(vect):
    # show_a = print('%d-Dim vector a = ' % len(a_n), a_n)
    # show_b = print('%d-Dim vector b = ' % len(b_n), b_n)
    n = len(vect)
    print(n, "Dim-Vector: <", sep="", end="")
    for i in range(n - 1):
        print(vect[i], end="|")
    print(vect[n - 1], ">.", sep="")

    #return show_a, show_b
#show()

def scal_prod():
    global mult
    sum = 0
    step = 0
    # print('a = ', a_n)
    # print('b = ', b_n)
    #print()
    while step < min(len(a_n), len(b_n)):
        mult = a_n[step] * b_n[step]
        next = mult
        sum += next
        stp = step
        print('step%d = ' % (stp+1), next)
        step += 1
    k = print('sum =' ,sum)
    return k

show(a_n)
show(b_n)
print()
print('summa: ')
scal_prod()

