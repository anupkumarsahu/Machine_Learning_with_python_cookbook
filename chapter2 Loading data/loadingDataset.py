# Load library
import numpy as np
from sklearn import datasets

# load digit dataset
digits = datasets.load_digits()

# Create features matrix
feature = digits.data

# Create target vector
target = digits.target

# View first observation
print(feature[0])