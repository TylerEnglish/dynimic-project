"""
And this first tutorial I'll show you 3
ways to solve the factorial problem
"""


def fac(value):
    '''
    This uses simple recursion to 
    solve it but theres a limit
    to how many times it can recur
    '''
    if value <= 1:
        return 1

    else:
        return value * fac(value - 1)


print('limits of facorial recursion Problem 1:')
print(fac(1))
print(fac(10))
print(fac(100))


def fac2(value, saved = None):
    '''
    Usually saving the data back into 
    itself would be the solution, but 
    since we only going back and looking 
    at a value once this solution is only
    as fast as the first 1
    '''
    if saved is None:
        saved = dict()

    if value <= 1:
        return 1

    else:
        fact = value * (fac2(value-1, saved))
        saved[value] = fact
        return fact

print('\n\nlimits of more advance facorial recursion Problem 2:')
print(fac2(1))
print(fac2(10))
print(fac2(100))

def fac3(value):
    '''
    This doesn't use recursion
    while recursion is easy to 
    use, it's not handy when
    going through a recursion call
    thousands of times. Your memormy
    in your pc or laptop wouldn't 
    be able to handle it 
    '''
    if value <= 0:
        return 1
    fact = 1
    for i in range(1, value +1):
        fact = fact * i

    return fact
print('\n\nlimits of dynimic solution to factorial Problem 3:')
print(fac3(1))
print(fac3(10))
print(fac3(100))
print(fac3(1000))
print(fac3(10000))