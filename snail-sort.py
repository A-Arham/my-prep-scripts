# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]


import numpy as np
def snail(snail_map):
    l=np.flatten(snail_map)


array1 = [[1,2,3],
         [4,5,6],
         [7,8,9]]


print(snail(array1))