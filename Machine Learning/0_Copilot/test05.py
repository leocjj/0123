matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = [[row[i] for row in matrix] for i in range(3)]

inverse = [[row[i] for row in matrix] for i in range(3)][::-1]

# Calculate the inverse of a matrix using numpy
import numpy as np
matrix = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
inverse = np.linalg.inv(matrix) # inverse of a matrix
print(inverse)
# [[-3.00000000e+00  1.00000000e+00  2.00000000e+00]
#  [ 2.00000000e+00 -8.88178420e-16 -2.00000000e+00]
#  [-1.00000000e+00  1.00000000e+00  1.00000000e+00]]

