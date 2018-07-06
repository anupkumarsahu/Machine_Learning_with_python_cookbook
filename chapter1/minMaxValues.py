# Load library
import numpy as np

# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Return maximum value
print(np.max(matrix))

# Return minimum value
print(np.min(matrix))

# Find maximum element in each column
print(np.max(matrix, axis=0))

# Find maximum element in each row
print(np.max(matrix, axis=1))