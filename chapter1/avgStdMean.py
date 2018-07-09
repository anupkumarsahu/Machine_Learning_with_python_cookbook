# load library
import numpy as np

# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Return mean
print("Mean \n",np.mean(matrix))

# Return mean for column
print("Mean by column \n",np.mean(matrix, axis=0))

# Return mean for column
print("Mean by row \n",np.mean(matrix, axis=1))

# Return variance
print("variance \n", np.var(matrix))

# Return variance for column
print("variance by column \n",np.var(matrix, axis=0))

# Return variance for row
print("variance by row \n",np.var(matrix, axis=1))

# Return standard deviation
print("deviation \n",np.std(matrix))
