"""
===============================================
Python for AI/ML Engineering
Phase 0 - Professional Python

Day 07 - NumPy
Practice File

Author: Fajar Naeem Rana
===============================================
"""
# Array Inspection
import numpy as np

X = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Array:")
print(X)

print("Type:", type(X))
print("Dimensions:", X.ndim)
print("Shape:", X.shape)
print("Size:", X.size)
print("Data type:", X.dtype)
print("Item size:", X.itemsize)
print("Total bytes:", X.nbytes)
#============================================

# Creating Arrays:
print(f"Creating Array:\n {np.array([10,20,30,40,50], dtype=float)}")
print(f"Array with zeros:\n {np.zeros((2,3))}")
print(f"Array with ones:\n {np.ones((2,3))}")
print(f"Array with custom values:\n {np.full((2,3), 5, dtype=float)}")
print(f"Empty array:\n {np.empty((2,3),dtype=float)}")
print(f"Array with step size of 2:\n {np.arange(0,20,2)}")
print(f"Array of 10 values between a range of 0-5:\n {np.linspace(0,5,10)}")
print(f"Identity matrix:\n{np.eye(3)}")
#==============================================

# Indexing and Slicing
X = np.array([
    [21, 5.5, 90, 80],
    [24, 7.0, 85, 75],
    [22, 6.0, 95, 88],
    [30, 4.5, 70, 65],
    [27, 8.0, 92, 91]
])

print("Shape:", X.shape)
print("First student:")
print(X[0])

print("Age column:")
print(X[:, 0])

print("Study Hours column:")
print(X[:, 1])

print("First three students:")
print(X[:3])

print("Study Hours + Attendance:")
print(X[:, 1:3])
#=========================================

# Reshaping
X = np.arange(24)

print("Original:")
print(X)
print("Shape:", X.shape)

X = X.reshape(6, 4)

print("\nReshaped:")
print(X)
print("Shape:", X.shape)

print("\nTranspose:")
print(X.T)
print("Shape:", X.T.shape)

print("\nFlatten:")
print(X.reshape(-1))
print("Shape:", X.reshape(-1).shape)
#==========================================

# Vectorization
x = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))

x = np.array([1, 2, 3, 4])
print(x * 3 + 1)
#==========================================

# Broadcasting
A = np.zeros((5, 3))
B = np.zeros(3)
C = A + B

A = np.zeros((5, 3))
B = np.zeros((5, 1))
C = A + B

A = np.zeros((2, 3, 4))
B = np.zeros((4,))
C = A + B
#==========================================

# View vs Copy
x = np.array([10, 20, 30, 40])

y = x[2:3].copy()
y[0] = 999
print(x)

y = x[[1, 3]]
y[0] = 999
print(x)

y = x
y[0] = 999
print(x)

y = x[1:3]
y[0] = 999
print(x)


