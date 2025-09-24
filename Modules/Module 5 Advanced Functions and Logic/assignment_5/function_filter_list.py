

def filter_function(value:int,threshold:int):
    # takes a value, and a threshold, compares the two, returns false if bigger, true otherwise
    if value > threshold:
        return False
    return True


if __name__ == "__main__":

    test_list = [1,2,3,4,5,6,7,8,9]
    threshold = 6

    out = filter(lambda x: filter_function(x,threshold),test_list) # filter function with threshold using lambda
    print([x for x in out]) #take filter object, turn to list, print list.
