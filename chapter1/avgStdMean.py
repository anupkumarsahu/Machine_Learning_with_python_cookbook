# load library
import numpy as np

# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Return mean
print(np.mean(matrix))

# Return mean for column
print(np.mean(matrix, axis=0))