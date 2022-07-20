

def reverse(s):
    '''
    this will reverse a string 
    using recursion
    '''
    if s == '':
        return s
    else:
        return reverse(s[1:]) + s[0]
'''
Solution 1: reversing a string
input: ''
output: ''
'''
print('\n\nProblem 1:\n',reverse(''))


'''
Solution 2: reversing a string
input: 'hi my name tyler'
output: 'relyt eman ym ih'
'''

print('\n\nProblem 2:\n',reverse('hi my name tyler'))

'''
Solution 3: reversing a string
input: 'asdfasdfa'
output: 'afdsafdsa'
'''

print('\n\nProblem 3:\n', reverse('asdfasdfa'))




def permutations_choose(letters, size, word=""):
    if len(word) == size:
            print(word)

    else:
        for i in range(len(letters)):
            letters_left = letters[:]
            del letters_left[i]

            
            
            permutations_choose(letters_left, size, word + letters[i])

'''
Solution 4: premutate a string
input: "ABCD"
number input: 3
output: 
ABC
ABD
ACB
ACD
ADB
ADC
BAC
BAD
BCA
BCD
BDA
BDC
CAB
CAD
CBA
CBD
CDA
CDB
DAB
DAC
DBA
DBC
DCA
DCB
'''
print('\n\nProblem 4:')
permutations_choose(list("ABCD"),3)

'''
Solution 5: premutate a string
input: "ABCD"
number input: 2
output: 
AB
AC
AD
BA
BC
BD
CA
CB
CD
DA
DB
DC
'''
print('\n\nProblem 5:')
permutations_choose(list("ABCD"),2)  

'''
Solution 6: premutate a string
input: "ABCD"
number input: 1
output: 
A
B
C
D
'''
print('\n\nProblem 6:')
permutations_choose(list("ABCD"),1)