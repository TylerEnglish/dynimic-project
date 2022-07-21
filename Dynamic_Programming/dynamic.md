# Dynamic Programming

## History of Dynamic Programming
***Richard Bellman the creator of Dynamic Programming as we know it became intrested in multistage decision problems in 1949 till 1955. In 1946 at the age of 25 he recieved a PHD from Princeton in Mathmatics. Bellman had the outstanding ability to apply math solution to real world problems. Later his Applied Mathmatics came to be known as Operation Research. In 1949 Richard Bellman was eager to go to RAND and to start working on Multistage Decision Processes. Of the Fall semester at RAND in 1950 he spent his time trying to come up with a name for this (during this time mathematical research wasn't doing well). He later met a guy in Washington named Wilson who hated the word research. Wilson worked with the Airforce and the RAND Corporation was employed to them. Henceforth, Bellman came up with the idea of naming it Programming and wanted to get the idea across that it was Dynamic. And this is how this Multistage Decision Processes became Dynamic Programming.***

## What is Dynamic Programming?
***Dynamic Programming is Multistage Decision Processes to effectively solve a class of problems that correlate with overlapping subproblems and optimal substructures.***

### Overlapping Subproblems

***This means that a problem can be broken into different subproblems which will be use several times. Usually can be solve using recursion.***

### Optimal Substructures

***A problem can be concidered this if an optimal solution can be constructed from optimal solutions of its subproblems. This helps clarify the usefullness of dynamic programming and greedy algorithms.***

## Examples
``` python
    def fac(value):
        if value <= 1:
            return 1

        else:
            return value * fac(value - 1)
``` 
***Recursion even if determine on memory capacity is a great example of basic dynanimic programming. With recursion we can look at both the Optimal and Overlapping subsequences.***

``` python
    
# Python program solution of
# friends pairing problem
 
# Returns count of ways
# n people can remain
# single or paired up.
def countFriendsPairings(n):
 
    dp = [0 for i in range(n + 1)]
 
    # Filling dp[] in bottom-up manner using
    # recursive formula explained above.
    for i in range(n + 1):
 
        if(i <= 2):
            dp[i] = i
        else:
            dp[i] = dp[i - 1] + (i - 1) * dp[i - 2]
 
    return dp[n]
 
# Driver code
n = 4
print(countFriendsPairings(n))
 
# This code is contributed
# by Soumen Ghosh.
``` 
***This is an example of solving a problem without the use of recursion.***
# Problem Solving
* [solution](Dynamic_Programming\dynamic_solutions.py)
* [practice](Dynamic_Programming\dynamic_practice.py)

# Use Cases of Recursion
## Benefits
* Great when problem can be subcatogorized into smaller problems
* Can obtain both local and total optimal solution
* Practical knowledge can be used to effectively gain higher efficiency on problems


# Other Pages
* [Welcome](Welcome\welcome.md)
* [Linked List](Linked_List\linked_list.md)
* [Recursion](Recursion\recursion.md)

# Links
* [pdf on the birth of Dynamic Programming](https://pubsonline.informs.org/doi/pdf/10.1287/opre.50.1.48.17791)
* [programiz](https://www.programiz.com/dsa/dynamic-programming)
* [overlapping subproblems](https://en.wikipedia.org/wiki/Overlapping_subproblems)
* [optimal substructures](https://en.wikipedia.org/wiki/Dynamic_programming)
* [benefits](https://www.ipl.org/essay/Advantages-Of-Dynamic-Programming-FCC7JQXZN6#:~:text=The%20advantage%20of%20dynamic%20programming,appear%20during%20the%20solving%20process.)
* [geeksforgeeks](https://www.geeksforgeeks.org/friends-pairing-problem/)