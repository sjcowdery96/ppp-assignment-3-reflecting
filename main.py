'''
Implement a function that will flatten and sort
an array of integers in ascending order, 
and which adheres to a functional programming paradigm.

Key characteristics of functional programming:
Pure functions: Functions that always produce the same output for the same input and have no side effects.
Immutability: Data is treated as immutable, meaning it cannot be modified after creation.
Recursion: Functions are often defined recursively, using themselves to solve smaller subproblems.
Higher-order functions: Functions that can take other functions as arguments or return functions as results.
Lazy evaluation: Expressions are evaluated only when their results are needed.



This function leverages Python's built-in sorted function to sort the flattened array. 
The flatten_helper function is a recursive helper function that flattens the nested array by iterating through each element. 
If an element is a list, it recursively flattens it. Otherwise, it appends the element to the result list.
'''

def flatten_and_sort(array):
    def flatten_helper(array, result):
        for element in array:
            if isinstance(element, list):
                result = flatten_helper(element, result)
            else:
                result.append(element)
        return result

    return sorted(flatten_helper(array, []))

#test array to prove functionality
testArray = [3,5,13,6,7,8,2,5,7]
print(flatten_and_sort(testArray)) #prints [2, 3, 5, 5, 6, 7, 7, 8, 13]


'''
REFLECTION QUESTIONS
-- How does this solution ensure data immutability?
-- Is this solution a pure function? Why or why not?
-- Is this solution a higher order function? Why or why not?
-- Would it have been easier to solve this problem using a different programming style?
-- Why in particular is functional programming a helpful paradigm when solving this problem?

1. Data Immutability
The script ensures data immutability by avoiding in-place modifications and leveraging recursion.

2. Pure Function
Yes, this is a pure function -- it always produces the same output from a given input.

3. Higher-Order Function
No, this is not a higher-order function because it does not retun a function.

4. Alternative Programming Style
Maybe, but for a problem this straight forward and constrained, functional programming is the way to go.

5. Why Functional Programming is Helpful
Functional programming is well-suited for this problem because of the need for data manipulation and repeatability. 
'''

##PART 2

##first define the base class with traits and function(s)
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired" 


#Use inheritance to define AnikinsPod with an added function for boost
class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

#Use inheritance to define SebulbasPod with an added function for flame_jet
class SebulbasPod(Podracer):
    def flame_jet(self, other_podracer):
        other_podracer.condition = "trashed"

'''
REFLECTION:
-- Is one of these coding paradigms "better" than the other? Why or why not?
-- Given the opportunity to work predominantly using either of these coding paradigms, which seems more appealing? Why?
-- Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best handled using functional programming? Object Oriented Programming?
-- Personally, which of these styles takes more work to understand? What should be done in order to deepen understanding related to this paradigm?

1. Better or worse
Functional programming is much better for block-scoped problems like optimization. 
Wheras object-oriented-programing is better for operations without fixed outcomes like games or simulations.

2. Which do you prefer
I definitely find Object-Oriented Programming more appealing because I love games!

3. What handles what
Optimization problems definitely are better suited to functional programming, but a combination of both styles
can be super effective. For instance, a functional program could be used to calculate the health of players in an in-game battle
and OOP can be used to hold the traits and functions of those characters in the game

4. To understand deeper
I think object-oreiented programming is more natural to first understand since it is less abstract by definition. 
In order to better understand functional programming, I love visualizations to see and comprehend BigO sorting speeds etc.

'''