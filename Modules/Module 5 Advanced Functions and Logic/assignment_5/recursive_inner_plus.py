

def recusion_mother(inlist):
    """

    :param inlist: list to process
    :return: deepest list + 1 for each entry
    """

    def recursive_inner(inlist:[int], recursionlevel=0, maxlevel=0, currentlist=[any])->[int]:
        """
        :param inlist: the list being processed
        :param recursionlevel: current recusion level, starting at 0. self increments
        :param maxlevel: deepest level seen so far
        :param currentlist: the current list being processed or sent down/up
        :return: returns the deepest list after recusions is done and the current max level
        """
        for value in inlist:
            if isinstance(value,list): #testing if list
                if recursionlevel > maxlevel: #comparing recursion level to our max level
                    currentlist = value # if we're deeper, update our list.
                    maxlevel = recursionlevel #if we're deeper, update level
                currentlist, maxlevel = recursive_inner(value,recursionlevel+1,maxlevel,currentlist), #go another step
        return currentlist, maxlevel

    deepest_list,_ = recursive_inner(inlist) # don't need the depth, so throw away that value when unpacking
    return [x+1 for x in deepest_list] # add 1 to each value and create a new list


if __name__ == "__main__":
    input_list = [1, 2, 3, 4,
                    [5, 6, 7,
                        [8, 9, 1, 3, 4, 65, 6, 43, 3, 4, 5, 56,
                            [8, 9, 1, 3, 4, 65, 6, 43,
                                [3, 4, 5, 56
                                , 45, 4, 3]
                            , 3, 4, 5, 56, 45, 4, 3]
                        , 45, 4, 3]
                     ]
                  ]
    second_list = [1, 2, 3, 4, [5, 6, 7, [8, 9]]]

    output = recusion_mother(input_list)
    print(output)
    output = recusion_mother(second_list)
    print(output)
