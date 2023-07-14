x = 100

def test_vars():

    global x, y, indifferent_var
    indifferent_var = 'hello, friend'
    x = 'some word'
    print('function`s body x =', x)

    y = 2000
    print('Inside function y =', y)

    x = 300

test_vars()

print()
print(indifferent_var)
print('outside function x = ', x)
print('outside function y =', y)
