n = 50000
ds = 1/n

#количевство точек, которые попоадают внутрь
pts = 0
i = 0

while i <= n:
    # x koordinte
    x = ds*i

    j =0
    while j<= n:
        # y koordinate
        y = ds*j
        if y <=x and y >= x**2:
            pts += 1
        j += 1
    i += 1
summation = pts/(n)**2
print('Площадь фигуры: ', summation )