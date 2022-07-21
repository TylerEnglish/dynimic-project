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
    pass

print('limits of facorial recursion Problem 1:')
print(fac(1))
print(fac(10))
print(fac(100))



def fac2(value):
    '''
    This doesn't use recursion
    while recursion is easy to 
    use, it's not handy when
    going through a recursion call
    thousands of times. Your memormy
    in your pc or laptop wouldn't 
    be able to handle it 
    '''
    pass

print('\n\nlimits of dynimic solution to factorial Problem 3:')
print(fac2(1))
print(fac2(10))
print(fac2(100))
print(fac2(1000))
print(fac2(10000))