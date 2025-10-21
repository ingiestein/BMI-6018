#1: import numpy
import numpy as np

#2: print numpy version
print("Problem 2")

print(f"The NumPy version is: {np.__version__}")

#3: make an array from 0 to 10.
my_darray = np.arange(0, 10, dtype=int)
print("Problem 3")
print(my_darray)
print(type(my_darray))

#4: import data file with Numpy as a comma delineated file with utf-8 character encoding, define datatypes and create column headers
data_array = np.genfromtxt(fname="iris.data", delimiter=',', dtype=[('1', 'f4'), ('2', 'f4'), ('3', 'f4'), ('4', 'f4'), ('5', 'U15')], encoding='utf-8')
mask = data_array['4'] > 1.0
row_index = np.where(mask) #first entry True from the mask.
print("Problem 4")
print("First row (index) where column 4 > 1.0: ", row_index[0][0])

#5

np.random.seed(100)
a = np.random.uniform(1,50, 20)
#replace all >30 values with 30
a[a>30] = 30
#replace and < 10 values with 10
a[a<10] = 10
print("Problem 5")

print(a)