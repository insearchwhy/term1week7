# Psuedo Codes

Plain language description of the steps in a algorithm or program
Bridge between the programs logic and the actual code.

## Importance
helps to understand and plan the program logic, so its easier to code
Improves collaboration in team projects
helps with troubleshooting
Identify the core areas of the programming thats needed

## Characteristics
plain language: simple to understand
Structured: follows a proper logic sequence
Abstraction: focuses oin logic more than syntax
Detailed: thorough walkthrough that helps explain the logic

## Basic constructs

Sequential

Step 1: do this
Step2: do that

Conditional

if condition matches then 
do something
ELSE
do something else
END IF

loops
WHILE condition meets
do something
END WHILE


For each in a collection
do something
END FOR

## Practical examples

Example 1: calculating the sum off a list of numbers

{1,2,3,4,5}
initialise sum to 0
then for each number in the list 
add the number to sum
END FOR
print sum


Example 2: Finding the maximum number in the list

Initialise max to the first number of the list
FOR each number in the list
If number is greter than max Then 
Set max to number
End If 
End for
print max

# Functions

one of the best tools for following dry coding principle
blocks of code that performs a specific task like prompt features
can be reused and helps the program modular and managaeble

## syntax
defining a function

def function_name(parameters):
    # code blocks
    return value

    Calling a function

    function_name()

## Scope
children can access parents scope
parents cannot access childrens scope

## return keyword
returns a value from function
also immediately ends the function
multiple possible return values in a function

## Arguments and fparameters
Arguments are values you can pass to the functionm
Parameters 
