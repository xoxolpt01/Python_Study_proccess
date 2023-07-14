def solve_eqn(f, x0, n):
    x = x0

    for k in range(1, n+1):
        x = f(x)
    return x

# eqn 1st
def eqn_1(x):
    return ((x**2)+5)/6

#eqn 2nd
def eqn_2(x):
    return (6*x-5)**0.5

print(solve_eqn(eqn_1,0,34))
print()
#print(solve_eqn(eqn_2,0,10))

