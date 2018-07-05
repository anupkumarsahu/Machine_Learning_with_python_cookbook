# Load library
import numpy as np
from scipy import sparse

# Create a matrix
matrix = np.array([[0, 0],
                  [0, 1],
                  [0, 2]])

# Create ompressed sparse row (CSR) matrix
matrix_sparse = sparse.csr_matrix(matrix)

print(matrix_sparse)