
def stacked_while(input_list:list)->[int]:
    """
    using a while statement and a rolling list of item to check, figure out the deepest list.
    :param input_list: the testing list
    :return: returns the deepest list
    """
    level = 0 #initial depth
    stack = [(level, input_list)] # rolling stack
    max_level = 0 # starting max level
    deepest_list = [] # return value deepest list

    while stack: #as long as there are entries in the stack
        level, entry = stack.pop(0) #pop the first entry
        if level > max_level: #check level of the list
            max_level = level # reset max level
            deepest_list = entry #
        elif level == max_level: # if there is a list at the same depth.
            deepest_list = [deepest_list,entry] # make a double entry list.
        for item in entry: # iterate each value in the current list.
            if isinstance(item,list): # if an entry is a list
                stack.append((level+1,item)) #create new stack entry from the list item and increment the depth
        pass
    try:
        out_list = [x + 1 for x in deepest_list] # try to catch exceptions ( if a two-list list.)
    except Exception as e:
        print(e, "Unable to increment all values of list")
    return out_list


if __name__ == "__main__":
    input_list = [1, 2, 3, 4, [5, 6, 7, [8, 9, 1, 3, 4, 65, 6, 43, 3, 4, 5, 56, 3, 4, 5, 56, 45, 4, 3], 45, 4, 3],
                  [8, 9, 1, 3, 4, 65, 6, 43, 3, 4, 5, 56,
                   [8, 9, 1, 3, 4, 65, 6, 43, [3, 4, 5, 56, 45, 4, 3], 3, 4, 5, 56, 45, 4, 3], 45, 4,
                   [8, 9, 1, 3, 4, 65, 6, 43, [3, 4, 5, 56, [1, 2, 3, 4], 45, 4, 3], 3]]]
    second_list = [1,2,3,4,[5,6,7,[8,9]]]
    output = stacked_while(input_list)
    print(output)
    output = stacked_while(second_list)
    print(output)
