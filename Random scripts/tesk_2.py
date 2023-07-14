
list_1 = [2, False, 9.1, 2 ,'hello', 5, 'Python']

list_2 =  [5, 3, 'HELLO', 7, 12.5, 'Python', True, False]


i = 0

for running_1 in list_1:
    for running_2 in list_2:
        if running_2 == running_1:

            print('list_1 совпадение такое слово: ' + str(running_1))
            print('list_1 совпадение такое слово: ' + str(running_1))

            print()

            i += 1

if 0 <= i <= 4:
    print("совпадает с двух списков, %d словa" % i)
elif i >= 5:
    print("совпадает с двух списков, %d слов" % i)


