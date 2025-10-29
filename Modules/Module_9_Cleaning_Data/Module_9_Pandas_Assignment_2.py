import pandas as pd
import numpy as np

# Question 1 (15 Points)
# Compute the euclidean distance between series (points) p and q, without using a packaged formula.
# Input

p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

#d(p,q) = sqr((a1-a2)^2 + (b1-b2)^2 ... (f1-f2)^2)
def euclidean_distance(p, q):
    sqrddiff = (p-q)**2
    sqrsum = sqrddiff.sum()
    return np.sqrt(sqrsum)
q_1 = euclidean_distance(p, q)
print("\nQuestion 1: ", q_1)


# Question 2 (15 Points)
# Change the order of columns of a dataframe. Interchange columns 'a' and 'c'.
# Input
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
q_2 = df [['c','b','a','d','e']] #manually switched lcoations of columns by changing the order in the index array provided.
print("\nQuestion 2: \n", q_2)


# Question 3 (15 Points)
# Change the order of columns of a dataframe.  Create a generic function to interchange two columns, without hardcoding column names.
# Input
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

def swap_func(df, col1, col2):
    cols = df.columns
    new_index = []
    for i, col in enumerate(cols): #iterate through the columns, generate index array with col1 and col2 switching.
        if col == col1:
            new_index.append(col2)
        elif col == col2:
            new_index.append(col1)
        else:
            new_index.append(col)
    df = df[new_index]
    return df

q3 = swap_func(df, 'b','e')

print("\nQuestion 3: \n", q3)

#
# Question 4 (15 Points)
# Format or suppress scientific notations in a pandas dataframe. Suppress scientific notations like ‘e-03’ in df and print upto 4 numbers after decimal.
# Input
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])
q_4 = df['random'].map('{:,.4f}'.format) #format the floats for printing, but doesn't change the data in df (can do more math after print)
print("\nQuestion 4: \n", q_4)

# #>    random
# #> 0  0.0035
# #> 1  0.0000
# #> 2  0.0747
# #> 3  0.0000

#
# Question 5 (15 Points)
# Create a new column that contains the row number of nearest column by euclidean distance. Create a new column such that, each row contains the row number of nearest row-record by euclidean distance.
# Input
q_5 = df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1), columns=list('pqrs'), index=list('abcdefghij'))
scidf = df.copy()
def calc_df_distances(df):
    indices = []
    distances = []
    #double loop check each row. ignoring when the dist == 0. rounding to 1 decimal point after the zero.
    for row in df.iterrows():
        nearest = ""
        distance = np.inf

        for comp in df.iterrows():
            dist = euclidean_distance(row[1], comp[1])
            if dist < distance and dist != 0:
                distance = dist
                nearest = comp[0]
        indices.append(nearest)
        distances.append(distance)
    return indices, distances

df["nearest_row"],df["dist"]=calc_df_distances(df)

print("\nQuestion 5: \n", q_5)


#alternative scipi way

from scipy.spatial.distance import cdist

data = scidf.to_numpy()
distance_matrix = cdist(data, data, 'euclidean')
np.fill_diagonal(distance_matrix, np.inf)
# print(distance_matrix)
nearest_idx = np.argmin(distance_matrix, axis=1)
lowest_value = np.min(distance_matrix, axis=1)

scidf["nearest_row"] = scidf.index[nearest_idx]
scidf["dist"] = lowest_value




# df
#     p   q   r   s
# a  57  77  13  62
# b  68   5  92  24
# c  74  40  18  37
# d  80  17  39  60
# e  93  48  85  33
# f  69  55   8  11
# g  39  23  88  53
# h  63  28  25  61
# i  18   4  73   7
# j  79  12  45  34

# Desired Output
# df
#    p   q   r   s nearest_row   dist
# a  57  77  13  62           i  116.0
# b  68   5  92  24           a  114.0
# c  74  40  18  37           i   91.0
# d  80  17  39  60           i   89.0
# e  93  48  85  33           i   92.0
# f  69  55   8  11           g  100.0
# g  39  23  88  53           f  100.0
# h  63  28  25  61           i   88.0
# i  18   4  73   7           a  116.0
# j  79  12  45  34           a   81.0

#
# Question 6 (15 Points)
#
# Correlation is a statistical technique that shows how two variables are related. Pandas dataframe.corr() method is used for creating the correlation matrix. It is used to find the pairwise correlation of all columns in the dataframe. Any na values are automatically excluded. For any non-numeric data type columns in the dataframe it is ignored.
#
# Input
data = {'A': [45, 37, 0, 42, 50],
        'B': [38, 31, 1, 26, 90],
        'C': [10, 15, -10, 17, 100],
        'D': [60, 99, 15, 23, 56],
        'E': [76, 98, -0.03, 78, 90]
        }

q_6 = df = pd.DataFrame.from_dict(data, orient='index')
df.corr()
print("\nQuestion 6: \n", df.corr())