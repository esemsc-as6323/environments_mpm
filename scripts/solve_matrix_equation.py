from envtest import my_mat_solver as ms
from sympy.matrices import Matrix, MatrixSymbol

# Call function to solve lin equation of type Ax=b

A = Matrix([[2,1,3],[4,7,1],[2,6,8]])
b = Matrix(MatrixSymbol('b',3,1))
x = ms(A,b)

print(x)
