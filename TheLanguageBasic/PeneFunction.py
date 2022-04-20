#!/usr/local/bin/python
# coding=UTF-8
######################################################################################
# Created by Sahoo, Prasanta K
# Copyright © 2021 Prasanta K. Sahoo. All rights reserved.
#
# Source : https://docs.python.org/3.10/tutorial/controlflow.html
######################## What You Would Find Here
# 1. Standard Function Syntax , 2. Function With Argument and Return( No info in signature about Return),
# 3. Function Argument with default values (and rules) , 4. default value is evaluated(Imp) ,
# 5. Parameters *name receives a tuple | **name receives a dictionary
# 6. Parameters *name and  **name(Readability-TODO Whether 3.10 only)
######################################################################################

'''
  1. Standard Function Syntax
  def : function definition.
  functionExample : Function Name
  Function statements :  Body of the function start at the next line, and must be indented.

  The Execution :
     A- All variable assignments in a function stored in a local symbol table
     B- Variables first looked into local symbol table, symbol table of enclosing function and
        then global symbol table and then at the end table of build-in names
    C- This is the reason global variables  and variable of enclosing function can not directly assigned a value
        To do that  it should be named in a global statement
    D- parameters (arguments)  are introduced in the local symbol table
    E- arguments are passed using call by value (where the value is always an object reference, not the value of the object)
'''
def functionExample():
    """
      This way  you can document the function detail
      The first statement is optional but suggested to be used for the function’s documentation string,
    """
    print("Starting to understand function")

'''
2. Function With Argument and Return( No info in signature about Return) 
A- The return statement returns with a value from a function, without that it returns None
'''
def functionWithArgumentAndReturn(count):
    data = []
    countTemp = 0
    while  countTemp < count:
        data.append(countTemp)
        countTemp += 1
    return data

'''
3. Function Argument with default values (and rules) 
A- The return statement returns with a value from a function, without that it returns None
B- non-keyword argument after a keyword argument is not allowed 
C- In a function call, keyword arguments must follow positional arguments
D- keyword arguments order is not important
'''
def functionWithArgumentDefaultValue(count, defaultString = "This is default", defaultInt = 5 ):
     print (count, defaultString ,defaultInt )

'''
4. default value is evaluated(Imp) 
The default value is evaluated only once. This makes a difference when 
the default is a mutable object such as a list, dictionary, or instances of most classes.
Make sure that reset that 
'''
def impWarningTestWithDefaultValueIssue(a, data = []):
    data.append(a)
    return data

def impWarningTestWithDefaultValueGood(a, data = None):
    if data is None:
        data = []
    data.append(a)
    return data

'''
5. Parameters *name receives a tuple | **name receives a dictionary
- Final formal parameter of the form **name is present, it receives a dictionary (Keyword Argument)
- Formal parameter of the form *name receives a tuple 
'''
def specificParameterswithStarNames(data,   *starData, **doubleStarData):
    print(data)
    for data1 in starData:
        print("Star data : ", data1 )

    for data2 in doubleStarData:
        print("Double Star data : ", data1 )

'''
6. Special Parameters *name and  **name(Readability-TODO Whether 3.10 only)
- Arguments may be passed to a Python function either by position or explicitly by keyword
- For readability and performance we could use the following way ( / and * are optional) 

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
         
- To mark parameters as keyword-only, indicating the parameters must be passed by keyword argument, 
place an * in the arguments list just before the first keyword-only parameter.
'''
#def specialParameters(pos_only, /, standard, *, kwd_only):
#    print(pos_only, standard, kwd_only)

'''
7. Arbitrary Argument Lists
'''
def arbitraryArgumentListsTest(*args):
     print(args)
'''
8. Unpacking Argument Lists
- Dictionaries can deliver keyword arguments with the **-operator
'''
def usearbitraryArgumentListsTest():
    def anotherFunction(data1, data2, data3):
        print(data1, data2,  data3)
    d = {"data1": "One", "data2": "3", "data3": "5"}
    anotherFunction(**d)

'''
9. Lambda Expressions
- Small anonymous functions can be created with the lambda keyword
- Lambda functions can be used wherever function objects are required
- Like nested function definitions, lambda functions can reference variables from the containing scope
- The below return tge function. This can be used to pass a small function as argument 
'''
def checkLambdaExpressions(data):
    return lambda data2: data2 + data


'''
10. Function Annotations ( TODO - May be 3.10)
- Function annotations are completely optional metadata information about the types used by user-defined functions
- https://peps.python.org/pep-3107/
'''
#def annotationsExample(data1: str, data2: int = 2) -> str:
def annotationsExample(data1, data2):
    #print("Annotations:", annotationsExample.__annotations__)
    print("Arguments:", data1, data2)
    return ""

'''
 1- even functions without a return statement do return a value (The value is None) 
'''
def functionExamplesRun():
    #returnData = functionExample()
    #print(returnData) # It will print None
    '''
      - There are three types of parameter

    '''
    #print(functionWithArgumentAndReturn(4))
    #functionWithArgumentDefaultValue(5,7) # (5, 7, 5)
    #functionWithArgumentDefaultValue(5, "new Data ", 7)  # (5, 'new Data ', 7)
    #functionWithArgumentDefaultValue(7)
    #functionWithArgumentDefaultValue(3, defaultString="This is good")
    #functionWithArgumentDefaultValue(3, defaultInt=7)  # This may be you expected to do

    #print(impWarningTestWithDefaultValueIssue(2))
    #print(impWarningTestWithDefaultValueIssue(11))
    #print(impWarningTestWithDefaultValueIssue(111))
    #print(impWarningTestWithDefaultValueGood(2))
    #print(impWarningTestWithDefaultValueGood(11))
    #print(impWarningTestWithDefaultValueGood(111))

    #specificParameterswithStarNames("Argument 1 ", 'Start 1', 'Star 2', 'Star 3',
    #                                "DoubleStar 1 = XYZ1", "DoubleStar 2 = XYZ2", "DoubleStar 3 = XYZ3" )
    #arbitraryArgumentListsTest('Data1', 'Data2', 1, 3, 4, 5)
    #usearbitraryArgumentListsTest()
    functionObj = checkLambdaExpressions(77)
    #print(functionObj(2))
    #print(functionObj(5))
    annotationsExample("Test1","Test2")

if __name__ == "__main__":
    functionExamplesRun()

'''
Style Guide for Python Code : https://peps.python.org/pep-0008/
Suggestion 1 . Use 4-space indentation, and no tabs.
    4 spaces are a good compromise between small indentation (allows greater nesting depth) and 
large indentation (easier to read). Tabs introduce confusion, and are best left out.

Suggestion 2 . Wrap lines so that they don’t exceed 79 characters.
    This helps users with small displays and makes it possible to have several code files side-by-side on larger displays.

Suggestion 3 .Use blank lines to separate functions and classes, and larger blocks of code inside functions.

Suggestion 4 .When possible, put comments on a line of their own.

Suggestion 5 .Use docstrings.

Suggestion 6 .Use spaces around operators and after commas, but not directly inside bracketing constructs: 
    a = f(1, 2) + g(3, 4).

Suggestion 7 .Name your classes and functions consistently; the convention is to use UpperCamelCase for 
classes and lowercase_with_underscores for functions and methods. Always use self as the name for the 
first method argument (see A First Look at Classes for more on classes and methods).

Suggestion 8 .Don’t use fancy encodings if your code is meant to be used in international environments. 
Python’s default, UTF-8, or even plain ASCII work best in any case.

Suggestion 9 .Likewise, don’t use non-ASCII characters in identifiers if there is only the slightest 
chance people speaking a different language will read or maintain the code.
'''