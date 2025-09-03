import numpy as np

np.random.seed(13)

def build_random_2d_array() -> np.ndarray: #define expected data type that is returned
    rows,cols = 3,4 # defining the size of the array generated
    array_2d = np.random.randint(1,100, size=(rows,cols)) #generating random number in an array of size (rows,cols)
    mix_array = np.array(array_2d,dtype=object) # creating an NP array which can hold multiple data types
    break_array(mix_array,rows,cols) #adding string to random location
    return mix_array

def break_array( mix_array:np.ndarray, rows:int, cols:int) -> np.ndarray:
    inserted_value = "Hello World"
    random_cell = (np.random.randint(0,np.size(mix_array,0)), np.random.randint(0,np.size(mix_array,1)))
    mix_array[random_cell] = inserted_value
    return mix_array

if __name__ == "__main__":
      # generate my random array with errant string
    my_array = build_random_2d_array()
      # iterate through each entry in the numpy array, (iterating an "object" np array is a little funny)
    with np.nditer(my_array, flags=['refs_ok'], op_flags=['readwrite']) as it:
        for item in it:

            val = item % 2
            print(val, item)
            #
            # try:
            #     #attempt a modulus on the value. should error for any string.
            #     val = item%2
            #     print(val,item)
            # except Exception as e:
            #     print(e, item)

