# -*- coding: utf-8 -*-
"""
#%% the humble print statement
'''

1.a
Using the print() function only, get the wrong_add_function to print out where
it is making a mistake, given the expected output for ex, "we are making an error 
in the loop", which you would put near the loop. 
Structure the print() statement to show what the expected output ought to be
via f-strings: ie "The correct answer is supposed to be: [...]".
1.b
Then, changing as little as possible, modify the function, using the same 
general structure to output the correct answer. Call this new function 
correct_add_function() 
'''
"""

#1.a
def wrong_add_function(arg1,arg2):
    '''
    The function takes in two lists of integers, then it adds
    all of arg2 to each item of arg1.

    Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [6,9,12]

    whereas the expected correct answer is, [2,3,4]

    Parameters
    ----------
    arg1 : list
      list of integers.
    arg2 : list
      list of integers.

    Returns
    -------
    arg1 : list
      Elements of arg1, with each element having had the contents of
      arg2 added to it.

    '''
    arg1_index=0
    while arg1_index < len(arg1):
        arg_2_sum = 0
        for arg2_elements in arg2:

            print("1.a: Here is the error. The sum(arg1[arg1_index]+i for i in arg2]) is adding each value of arg2 to the value at arg1[arg1_index] then summing the resultant sums together.")
            print(f"1.a: The correct answer should be: {arg1[arg1_index] + arg2_elements}")
            arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])

        arg1[arg1_index]=arg_2_sum
        arg1_index+=1
    return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

print(f"1.a wrong_add_function_result: {wrong_add_function(arg1, arg2)}")

#1.b
def correct_add_function(arg1,arg2):
    '''
    The function takes in two lists of integers, then it adds
    all of arg2 to each item of arg1.

    Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [6,9,12]

    whereas the expected correct answer is, [2,3,4]

    Parameters
    ----------
    arg1 : list
      list of integers.
    arg2 : list
      list of integers.

    Returns
    -------
    arg1 : list
      Elements of arg1, with each element having had the contents of
      arg2 added to it.

    '''
    arg1_index=0
    while arg1_index < len(arg1):
        for arg2_elements in arg2:
            arg_2_sum = arg1[arg1_index] + arg2_elements
            # adjusted indentation so that arg1_index increments correctly. could change to two for-loops (which could be better)
            # but I'm trying to "change as little as possible"
            arg1[arg1_index]=arg_2_sum
            arg1_index+=1
    return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

print(f"1.b correct_add_function: {correct_add_function(arg1, arg2)}")

#%% try, except
'''
2.a
Update the numeric section of the function with your changes from 1 for both 
2.b and 2.c

2.b
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
returns an error message to the user, in case users give invalid inputs,
(for example an input of ["5","2", 5])
: "Your input argument [1 or 2] at element [n]
is not of the expected type. Please change this and rerun. Name this function 
exception_add_function()

2.c
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
gets it to process via the string section. IE, do not, outside the function,
change the values of arg_str_1 or arg_str_2. Name this function 
correction_add_function(), i.e you will not be updating the wrong_add_function,
you will simply handle the error of wrong inputs in a seperate function, you want
the wrong_add_function to output its current result you are only bolstering the 
function for edge cases .
'''
"""def wrong_add_function(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [4,5,6]
   
   If the lists are lists of strings, concatenate them
   Example:
      > wrong_add_function(['1','2','3'],['1','1','1'])
      > ['1111','2111','3111']
   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.

   '''
   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
               arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1
arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]
wrong_add_function(arg_str_1, arg_str_2)"""

#problem 2

# 2.b

def except_add_function(arg1, arg2):
    '''
    The function takes in two lists of integers, then it adds
    all of arg2 to each item of arg1.

    Example:
       > wrong_add_function([1,2,3],[1,1,1])
       > [4,5,6]

    If the lists are lists of strings, concatenate them
    Example:
       > wrong_add_function(['1','2','3'],['1','1','1'])
       > ['1111','2111','3111']
    Parameters
    ----------
    arg1 : list
       list of integers.
    arg2 : list
       list of integers.

    Returns
    -------
    arg1 : list
       Elements of arg1, with each element having had the contents of
       arg2 added to it.

    '''
    # numeric section
    errors = []
    try:# try statment testing each entry type against the type of the first entry. collect any that differ, and if the
        # len of the collected errors is > 0 raise type error and report this to the user.
        ref_type = type(arg1[0])
        for index,val in enumerate(arg1):
            if type(val) != ref_type:
                errors.append((index,val,"arg1"))
        for index,val in enumerate(arg2):
            if type(val) != ref_type:
                errors.append((index,val,"arg2"))
        if len(errors) > 0:
            raise TypeError
    except TypeError:
        for index,val,arg in errors:
            print(f"2.b: The value({val}) at index({index}) in argument({arg}) is of a different type({type(val)}). All entries must be either a string or integer. Please adjust your input and try again.")
            return #exit the program smoothly
    if sum([type(i) == int for i in arg1]) == len(arg1) and \
            sum([type(i) == int for i in arg2]) == len(arg2):
        arg1_index = 0 #here is the start of my code from problem 1, only slightly adjusted to return the expected result as indicated in problem 2.
        while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
                arg_2_sum = arg1[arg1_index] + arg2_elements
                # the "correct result" in problem 2 is different from problem 1. problem 1 says the correct answer would be [2,3,4] and here is [4,5,6]
                # I adjusted this function in problem 2 so that it returns the expected result mentioned in the comments for problem 2.
                arg1[arg1_index] = arg_2_sum
            arg1_index += 1
        print("except_add_function: ", arg1)
        return arg1
    # string section
    elif sum([type(i) == str for i in arg1]) == len(arg1) and \
            sum([type(i) == str for i in arg2]) == len(arg2):
        arg1_index = 0
        while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
                arg_2_sum += arg2_elements
            arg1[arg1_index] = arg1[arg1_index] + str(arg_2_sum)
            arg1_index += 1
        return arg1

arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]
except_add_function(arg_str_1, arg_str_2)


#2.c
def correction_add_function(arg1, arg2):
    '''
    The function takes in two lists of integers, then it adds
    all of arg2 to each item of arg1.

    Example:
       > wrong_add_function([1,2,3],[1,1,1])
       > [4,5,6]

    If the lists are lists of strings, concatenate them
    Example:
       > wrong_add_function(['1','2','3'],['1','1','1'])
       > ['1111','2111','3111']
    Parameters
    ----------
    arg1 : list
       list of integers.
    arg2 : list
       list of integers.

    Returns
    -------
    arg1 : list
       Elements of arg1, with each element having had the contents of
       arg2 added to it.

    '''
    # numeric section
    errors = []
    try: # try statment testing each entry type against the type of the first entry. collect any that differ, and if the
        # len of the collected errors is > 0 raise type error and report this to the user.
        ref_type = type(arg1[0])
        for index,val in enumerate(arg1):
            if type(val) != ref_type:
                errors.append((index,val,"arg1"))
        for index,val in enumerate(arg2):
            if type(val) != ref_type:
                errors.append((index,val,"arg2"))
        if len(errors) > 0:
            raise TypeError
    except TypeError:
        for index,val,arg in errors:
            print(f"2.c: The value({val}) at index({index}) in argument({arg}) is of a different type({type(val)}). All entries must be either a string or integer.")
            print("2.c: Arguments with be converted to lists of strings.")
        #This section would be very slow for large arrays.
        arg1 = [str(x) for x in arg1] #make sure each entry is a string
        arg2 = [str(x) for x in arg2] #make sure each entry is a string.
    if sum([type(i) == int for i in arg1]) == len(arg1) and \
            sum([type(i) == int for i in arg2]) == len(arg2):
        arg1_index = 0 #here is the start of my code from problem 1, only slightly adjusted to return the expected result as indicated in problem 2.
        while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
                arg_2_sum = arg1[arg1_index] + arg2_elements
                # the "correct result" in problem 2 is different from problem 1. problem 1 says the correct answer would be [2,3,4] and here is [4,5,6]
                # I adjusted this function in problem 2 so that it returns the expected result mentioned in the comments for problem 2.
                arg1[arg1_index] = arg_2_sum
            arg1_index += 1
        print("except_add_function: ", arg1)
        return arg1
    # string section
    elif sum([type(i) == str for i in arg1]) == len(arg1) and \
            sum([type(i) == str for i in arg2]) == len(arg2):
        arg1_index = 0
        while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
                arg_2_sum += arg2_elements
            arg1[arg1_index] = arg1[arg1_index] + str(arg_2_sum)
            arg1_index += 1
        return arg1

arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]

print("2.c: correction_add_function: ", correction_add_function(arg_str_1,arg_str_2))