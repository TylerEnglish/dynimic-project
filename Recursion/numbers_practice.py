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

#start of problem 1
def fib(n):
    pass
#end of problem 1

#start of problem 2
#better recursion
def fib2(n, saved = None):
    pass
#end of problem 2


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

