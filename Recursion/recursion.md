# Recursion

## History of Recursion
***This dates back to late 19th century with mathematicians Dedekind and Peano who used the principle of defining a function with induction. This played an important role in the foundation of mathematics.***

## What is Recursion
***Its a widely used phenomenon in Computer Science in which is used to solve complex problems by using the concept of Overlapping Subproblems. It's solved by which a function calls itself directly or indirectly.***

## Examples
***Below this is a basic case of recursion***

``` python
    def recursion():
        if True:
            return
        else:
            recursion()
``` 

***Below this is a more complex case of recursion***

``` python
    def fac(value):
        if value <= 1:
            return 1

        else:
            return value * fac(value - 1)
``` 
***You might have saw this when you looked at the welcome page. This recusion example solves a factorial problem. As you can see there are 2 core requirements of a recursion model. One is having a base case and the other the recursive call.***
# Problem Solving
* [numbers practice](Recursion\numbers_practice.py)
* [dynamic recursion practice](Recursion\dynamic_rec_practice.py)
* [string practice](Recursion\string_practice.py)
* [numbers solution](Recursion\numbers_solutions.py)
* [string solution](Recursion\strings_solutions.py)
* [dynamic recursion solution](Recursion\dynamic_rec_solution.py)

# Use Cases of Recursion
## Benefits
* Adds clarity and sometimes reduces time in writing
* Reduces time Complexity
* Performs better in solving problems based on tree structures
* Reduces unnecessary calling of function
* Better at tree traversal

## Problems
* Requires a lot of memory
* Slower than nonrecursive functions
* Not more effective in terms of space and time
* Difficult to analyze code

# Other Pages
* [Welcome](Welcome\welcome.md)
* [Linked List](Linked_List\linked_list.md)
* [Dynamic Programming](Dynamic_Programming\dynamic.md)

# Links
* [pdf](https://eprints.illc.uva.nl/id/eprint/383/1/PP-2010-04.text.pdf#:~:text=The%20notion%20of%20recursion%20dates,the%20foundations%20of%20mathematics%20(cf.)
* [Recursion](https://www.educative.io/answers/what-is-recursion)
* [use cases](https://stackoverflow.com/questions/5250733/what-are-the-advantages-and-disadvantages-of-recursion)
* [more use cases](https://cbselibrary.com/advantages-and-disadvantages-of-recursion/)