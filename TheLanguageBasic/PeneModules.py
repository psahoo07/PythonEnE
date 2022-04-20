#!/usr/local/bin/python
# coding=UTF-8
######################################################################################
# Created by Sahoo, Prasanta K
# Copyright © 2021 Prasanta K. Sahoo. All rights reserved.
#
# Source : https://docs.python.org/3.10/tutorial/modules.html
# TO DO - Start from 6.1.1. Executing modules as scripts
######################## What You Would Find Here
# 1 if Statement, 2 for  Statement, 3. for  Statement With Range,
# 4. While  Statement, 5. Use of break and Continue , 6. Use of Pass ,
# 7. Match Statement (TODO- version 3.10)
######################################################################################
""" Important Notes
1 . A module is a file containing Python definitions and statements. The file name is the module
    name with the suffix .py appended. Within a module, the module’s name (as a string) is available
    as the value of the global variable __name__

2. A module can contain executable statements as well as function definitions. These
    statements are intended to initialize the module. They are executed only the first time the
    module name is encountered in an import statement. Those also run if the file is executed as a script

3. Not required to place all import statements at the beginning of a module

4. For efficiency reasons, each module is only imported once per interpreter session.
    Therefore, if you change your modules, you must restart the interpreter – or,
    if it’s just one module you want to test interactively, use importlib.reload(),
    e.g. import importlib; importlib.reload(modulename).

5. Each module has its own private symbol table, which is used as the global symbol table
    by all functions defined in the module. Thus, the author of a module can use global variables
    in the module without worrying about accidental clashes with a user’s global variables.
    On the other hand, if you know what you are doing you can touch a module’s global variables
    with the same notation used to refer to its functions, modname.itemname.

6. The imported module names are placed in the importing module’s global symbol table.
   There is a variant of the import statement that imports names from a module directly
   into the importing module’s symbol table. For example:
"""
import PeneFunction
'''
1- calling a function from other module & assigning method to local name
'''
def callFullModule():
        print("calling PeneFunction.functionExample")
        PeneFunction.functionExample()
        print("------ You can assign to a local name ")
        other_name = PeneFunction.functionExample # Important : () is not there
        other_name()

'''
2- Call some names from a module 
'''
def callSomeNamesFromModule():
        from PeneCollections import listExample, listAsStacks
        print("-------- Calling listExample from PeneCollections")
        listExample()

'''
3- Call all names from a module using * (Not full module: except beginning with an underscore (_))
'''
def callALLNamesFromModuleUsingStar():
    """
    - This imports all names except those beginning with an underscore (_)
    - Normally it is not suggested because it introduces an unknown set of names into the interpreter
    - May create a conflict which you already created
    """
    from PeneCollections import *
    # Waring : SyntaxWarning: import * only allowed at module level def callALLNamesFromModuleUsingStar():
    print("-------- Using import *  from PeneCollections")
    listExample()

'''
4- Call all names using as keyword 
'''
def callNamesFromModuleUsingAs():

    import PeneCollections as pc
    print("...................Using as  from PeneCollections")
    pc.listExample()
    print("...................Using as  from PeneFunction")
    from PeneFunction import functionExample as tfe
    tfe()


if __name__ == "__main__":
    #callFullModule()
    #callSomeNamesFromModule()
    #callALLNamesFromModuleUsingStar()
    callNamesFromModuleUsingAs()

