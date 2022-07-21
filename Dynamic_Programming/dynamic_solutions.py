'''
Longest Common Subsequence 

Given two sequences, find the length of longest subsequence 
present in both of them. A subsequence is a sequence that 
appears in the same relative order, but not necessarily contiguous. 
For example, “abc”, “abg”, “bdf”, “aeg”, ”acefg”, .. etc 
are subsequences of “abcdefg”.
'''
def recLCS(m, n, X, Y):
    #base case
    if m == 0 or n == 0:
        return 0
    
    elif Y[n-1] == X[m-1]:
        return 1 + recLCS(m-1, n-1, X, Y)
    
    else:
        return max(recLCS(m,n-1, X, Y), recLCS(m-1, n, X, Y))

def longComSub(X,Y):
    m = len(X)
    n = len(Y)
    L = [[None]*(n+1) for i in range(m+1)]
 
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    return L[m][n]


'''
Collect Maximum Points in Matrix with given constraints

Give a matrix of M x X filled with either a 1,0,-1
where -1 denotes unsafe. Collect numbers of ones starting 
from cell [0][0]

Solution I provide uses recursion
'''
def notSafe(mat, i, j):
    #unsafe boxes
    return i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]) or mat[i][j] == -1
 
 
# Function to collect the maximum number of ones starting from cell `mat[i][j]`
def findMax(mat, i=0, j=0):
 
    # base case
    if not mat or not len(mat):
        return
 
    # return if unsafe
    if notSafe(mat, i, j):
        return 0
 
    # odd left or down
    if i & 1:
        return mat[i][j] + max(findMax(mat, i, j - 1), findMax(mat, i + 1, j))
 
    # even right or down
    else:
        return mat[i][j] + max(findMax(mat, i, j + 1), findMax(mat, i + 1, j))

'''
Word Break Problem: 
Given a string and a dictionary of words, 
determine if the string can be segmented 
into a space-separated sequence of one or 
more dictionary words.
'''
def wordBreak(words, word, out=''):
    #base case
    if not word:
        print(out)
        return
    
    for x in range(1, len(word) + 1):
        prefix =word[:x]

        if prefix in words:
            wordBreak(words, word[x:], out + ' '+ prefix )

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