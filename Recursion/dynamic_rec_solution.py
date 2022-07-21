
# 
'''
Tower of Hanoi is a mathematical puzzle where we have n rods and n disks. 
The objective of the puzzle is to move the entire stack to another rod, 
obeying the following simple rules: Only one disk can be moved at a time
'''
def towerOfHanoi(n, from_rod, to_rod, aux_rod1, aux_rod2):
    '''
    Recursive program for Tower of Hanoi

    base cases are if 0 do nothing 
    if 1 move disk from rod to rod
    '''
    if (n == 0):
        return
    if (n == 1):
        print("Move disk", n, "from rod",from_rod, "to rod", to_rod)
        return

    towerOfHanoi(n - 2, from_rod, aux_rod1,aux_rod2, to_rod)
    print("Move disk", n-1, "from rod", from_rod,"to rod", aux_rod2)

    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)

    print("Move disk", n-1, "from rod", aux_rod2, "to rod", to_rod)

    towerOfHanoi(n - 2, aux_rod1, to_rod,from_rod, aux_rod2)

# driver program

'''
Solution 1 with 4 rods

output:
Move disk 1 from rod A to rod D
Move disk 2 from rod A to rod B
Move disk 1 from rod D to rod B
Move disk 3 from rod A to rod C
Move disk 4 from rod A to rod D
Move disk 3 from rod C to rod D
Move disk 1 from rod B to rod C
Move disk 2 from rod B to rod D
Move disk 1 from rod C to rod D
'''
n = 4 # Number of disks

# A, B, C and D are names of rods
print('Problem 1:')

towerOfHanoi(n, 'A', 'D', 'B', 'C')

'''
Solution 2 with 10 rods

output:
Move disk 1 from rod A to rod D
Move disk 2 from rod A to rod B
Move disk 1 from rod D to rod B
Move disk 3 from rod A to rod C
Move disk 4 from rod A to rod D
Move disk 3 from rod C to rod D
Move disk 1 from rod B to rod C
Move disk 2 from rod B to rod D
Move disk 1 from rod C to rod D
Move disk 5 from rod A to rod B
Move disk 6 from rod A to rod C
Move disk 5 from rod B to rod C
Move disk 1 from rod D to rod C
Move disk 2 from rod D to rod A
Move disk 1 from rod C to rod A
Move disk 3 from rod D to rod B
Move disk 4 from rod D to rod C
Move disk 3 from rod B to rod C
Move disk 1 from rod A to rod B
Move disk 2 from rod A to rod C
Move disk 1 from rod B to rod C
Move disk 7 from rod A to rod D
Move disk 8 from rod A to rod B
Move disk 7 from rod D to rod B
Move disk 1 from rod C to rod A
Move disk 2 from rod C to rod D
Move disk 1 from rod A to rod D
Move disk 3 from rod C to rod B
Move disk 4 from rod C to rod A
Move disk 3 from rod B to rod A
Move disk 1 from rod D to rod B
Move disk 2 from rod D to rod A
Move disk 1 from rod B to rod A
Move disk 5 from rod C to rod D
Move disk 6 from rod C to rod B
Move disk 5 from rod D to rod B
Move disk 1 from rod A to rod B
Move disk 2 from rod A to rod C
Move disk 1 from rod B to rod C
Move disk 3 from rod A to rod D
Move disk 4 from rod A to rod B
Move disk 3 from rod D to rod B
Move disk 1 from rod C to rod D
Move disk 2 from rod C to rod B
Move disk 1 from rod D to rod B
Move disk 9 from rod A to rod C
Move disk 10 from rod A to rod D
Move disk 9 from rod C to rod D
Move disk 1 from rod B to rod C
Move disk 2 from rod B to rod D
Move disk 1 from rod C to rod D
Move disk 3 from rod B to rod A
Move disk 4 from rod B to rod C
Move disk 3 from rod A to rod C
Move disk 1 from rod D to rod A
Move disk 2 from rod D to rod C
Move disk 1 from rod A to rod C
Move disk 5 from rod B to rod D
Move disk 6 from rod B to rod A
Move disk 5 from rod D to rod A
Move disk 1 from rod C to rod A
Move disk 2 from rod C to rod B
Move disk 1 from rod A to rod B
Move disk 3 from rod C to rod D
Move disk 4 from rod C to rod A
Move disk 3 from rod D to rod A
Move disk 1 from rod B to rod D
Move disk 2 from rod B to rod A
Move disk 1 from rod D to rod A
Move disk 7 from rod B to rod C
Move disk 8 from rod B to rod D
Move disk 7 from rod C to rod D
Move disk 1 from rod A to rod B
Move disk 2 from rod A to rod C
Move disk 1 from rod B to rod C
Move disk 3 from rod A to rod D
Move disk 4 from rod A to rod B
Move disk 3 from rod D to rod B
Move disk 1 from rod C to rod D
Move disk 2 from rod C to rod B
Move disk 1 from rod D to rod B
Move disk 5 from rod A to rod C
Move disk 6 from rod A to rod D
Move disk 5 from rod C to rod D
Move disk 1 from rod B to rod D
Move disk 2 from rod B to rod A
Move disk 1 from rod D to rod A
Move disk 3 from rod B to rod C
Move disk 4 from rod B to rod D
Move disk 3 from rod C to rod D
Move disk 1 from rod A to rod C
Move disk 2 from rod A to rod D
Move disk 1 from rod C to rod D
'''
print('\n\nProblem 2:')
n = 10
towerOfHanoi(n, 'A', 'D', 'B', 'C')