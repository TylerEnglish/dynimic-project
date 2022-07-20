#recursion

'''
We are solving for fibonaci sequence.
The fibonaci sequence goes like this:
0+1+2+3+n 

In this program I showcase 2 ways
with recursion to solve these problems.

One way doesn't save previous values
which is the slow way

The other does save previous values.
'''
def fib(n):
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1:  
        return 1
    else:
        fibo = fib(n-1) + fib(n-2)
        return fibo



#better recursion
def fib2(n, saved = None):
    if saved is None:
        saved = dict()

    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1:  
        return 1

    elif n in saved:
        return saved[n]

    else:
        fibo = fib2(n-1, saved) + fib2(n-2, saved)
        saved[n] = fibo
        return fibo


'''
Soultion 1 - fib = 19

output:
4181
'''
print('Problem 1: ')
print('Fib 2 Sequence:', fib2(19))
print('Fib 1 Sequence:',fib(19))



'''
Soultion 2 - fib = 30

output:
832040
'''
print()
print('Problem 2:')
print('Fib 2 Sequence:', fib2(30))
print('Fib 1 limit Sequence:', fib(30))


'''
Soultion 3 - fib = 100

output:
354224848179261915075
'''
print()
print('Problem 3 Sequence:')
print('Fib 2 limit Sequence:', fib2(100))

