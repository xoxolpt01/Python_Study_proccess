x = input('x? :')
y = input('y? :')

def f(x, y):
    try:
        y = int(y)
        x = int(x)
        sum = x + y
        return sum

    except ValueError:
        print('you wrote a text')
        print('please, rewrite')



print(f(x, y))