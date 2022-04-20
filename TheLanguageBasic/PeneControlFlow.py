#!/usr/local/bin/python
# coding=UTF-8
######################################################################################
# Created by Sahoo, Prasanta K
# Copyright © 2021 Prasanta K. Sahoo. All rights reserved.
#
# Source : https://docs.python.org/3.10/tutorial/controlflow.html
######################## What You Would Find Here
# 1 if Statement, 2 for  Statement, 3. for  Statement With Range,
# 4. While  Statement, 5. Use of break and Continue , 6. Use of Pass ,
# 7. Match Statement (TODO- version 3.10)
######################################################################################

'''
1 if Statement
'''
def iFStatementTest():
    print('Use of If statement')
    data = 0
    if data < 0:
        print('Data less than 0')
    elif data > 0:
        print('Data greater than 0')
    else:
        print('Data is  0')

'''
2 for  Statement
'''
def forStatementTest():
    print('Use of  for statement')
    data_list = ['data1', 'data2', 'data3']
    for data in data_list:
        print(data)

'''
3. for  Statement With Range
range(1, 5) : out put 1, 2, 3, 4 
range(1, 7, 2) : out put 1 , 3, 5 
'''
def forStatementWithRangeTest():
    print('Use of  for statement with range')
    for data in range(4):
        print(data)

'''
4. While  Statement
'''
def whileStatementTest():
    print('Use of  for while')
    count = 0
    while count < 5:
        print("I am in while count is ", count)
        count += 1
'''
5. Use of break and Continue 
'''
def breakAndContinue():
    count = 0
    while count < 5:
        print("### This print statement will be 5 time ", count)
        count += 1
        if count == 2:
            continue
        print("*** This print statement will be 4 time ", count)

    for data in range(4):
        print("This print will be only 3 times", data)
        if data == 2:
            break
'''
6. Use of Pass 
'''
def passStatement():
    count = 0
    print("Process started ... make sure you kill it Ctrl+C")
    #IndentationError: expected an indented block
    while count < 5:
        pass
    print("Never here")
    '''
        - The pass statement does nothing. It can be used when a statement is
           required syntactically but the program requires no action
        - This is commonly used for creating minimal classes:
            class MyEmptyClass:
                pass
        - As shown above if you remove pass the while loop will give syntax error
    '''

''' TODO
7. Match Statement (TODO- version 3.10)
def matchStatement():
    inputData = 2
    
    match inputData:
        case 1:
            return "One"
        case 2:
            return "Two"
        case _:
            return "Did not match"
'''
###############2 match Statements


if __name__ == "__main__":
    iFStatementTest()
    #forStatementTest()
    #forStatementWithRangeTest()
    #whileStatementTest()
    #breakAndContinue()
    #passStatement()
    #matchStatement()