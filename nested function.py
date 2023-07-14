def sq_sum():
    #there function get`s int number
    def get_n():
        global n
        n = int(input('Слагаемый в сумме: '))

        return n

    # & here next step, function calculate
    n = get_n()
    def find_sq_sum():
        s = 0

        for i in range(1, n+1):
            s += i**2
        return s
    # return -> get result, calculated by find_sq_sum()
    return find_sq_sum()
z = sq_sum()

print("Сумма квадратов равна: ", z)