import numpy as np

m = np.array([[1, 5, 2],
              [4, 7, 4],
              [2, 0, 9]])
print(m, m.shape)
print('Matrix Transpose:\n', m.transpose(), '\n')
# matrix determinant
print('Matrix Determinant:', np.linalg.det(m), '\n')

# matrix inverse
m_inv = np.linalg.inv(m)
print('Matrix inverse:\n', m_inv, '\n')

# identity matrix (result of matrix x matrix_inverse)
iden_m = np.dot(m, m_inv)
iden_m = np.round(np.abs(iden_m), 0)
print('Product of matrix and its inverse:\n', iden_m)

# eigendecomposition

m = np.array([[1, 5, 2],
              [4, 7, 4],
              [2, 0, 9]])
eigen_vals, eigen_vecs = np.linalg.eig(m)
print('Eigen Values:', eigen_vals, '\n')
print('Eigen Vectors:\n', eigen_vecs)
