'''
Longest Common Subsequence 

Given two sequences, find the length of longest subsequence 
present in both of them. A subsequence is a sequence that 
appears in the same relative order, but not necessarily contiguous. 
For example, “abc”, “abg”, “bdf”, “aeg”, ”acefg”, .. etc 
are subsequences of “abcdefg”.
'''
#start of problem
def recLCS(m, n, X, Y):
    pass
#end of problem
#start of problem
def longComSub(X,Y):
    pass
#end of problem



'''
Collect Maximum Points in Matrix with given constraints

Give a matrix of M x X filled with either a 1,0,-1
where -1 denotes unsafe. Collect numbers of ones starting 
from cell [0][0]

Solution I provide uses recursion
'''
#start of problem
def notSafe(mat, i, j):
    pass
 
# Function to collect the maximum number of ones starting from cell `mat[i][j]`
def findMax(mat, i=0, j=0):
    pass
#end of problem
'''
Word Break Problem: 
Given a string and a dictionary of words, 
determine if the string can be segmented 
into a space-separated sequence of one or 
more dictionary words.
'''
#start of problem 
def wordBreak(words, word, out=''):
    pass
#end of problem

'''
Solution 1: recursion lcs/ naivie solution

x input: 'AGGIJKB'
y input: 'BGIJGKB'
output: 5
'''
print('Problem 1:')
x = 'AGGIJKB'
y = 'BGIJGKB'

print('Lenght of LCS is:', recLCS(len(x), len(y), x, y),'\n\n')

'''
Solution 2: non-naivie solution

x input: 'AGGIJKB'
y input: 'BGIJGKB'
output: 5
'''
print('Problem 2:')
print('Lenght of LCS is:', longComSub(x, y),'\n\n')


'''
Solution 3: Find max points in a map

input: mat = [ [1, 1, -1, 1, 1],
               [1, 0, 0, -1, 1],
               [1, 1, 1, 1, -1],
               [-1, -1, 1, 1, 1],
               [1, 1, -1, -1, 1]]
output: 9
'''
mat = [ [1, 1, -1, 1, 1],
        [1, 0, 0, -1, 1],
        [1, 1, 1, 1, -1],
        [-1, -1, 1, 1, 1],
        [1, 1, -1, -1, 1]]
print('Problem 3:')
print('Points found', findMax(mat))

'''
Solution 4: wordbreak
word dic: ['th', 'is', 'this', 'a', 
         'word', 'wo', 'rd', 'break',
         'br', 'ak', 'eak', 'bre', 
         'brea', 'reak']
word: 'thisisawordbreak'
output: 
th is is a wo rd br eak
th is is a wo rd bre ak
th is is a wo rd break
th is is a word br eak
th is is a word bre ak
th is is a word break
this is a wo rd br eak
this is a wo rd bre ak
this is a wo rd break
this is a word br eak
this is a word bre ak
this is a word break
'''

words = ['th', 'is', 'this', 'a', 
         'word', 'wo', 'rd', 'break',
         'br', 'ak', 'eak', 'bre', 
         'brea', 'reak']

word = 'thisisawordbreak'

print('Problem 5:')
wordBreak(words, word)