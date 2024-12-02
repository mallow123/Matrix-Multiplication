import numpy as np
r1 = int(input("Number of rows in Matrix1: "))
c1 = int(input("Number of columns in Matrix1: "))
r2 = int(input("Number of rows in Matrix2: "))
c2 = int(input("Number of columns in Matrix2: "))

if c1 != r2:
    print("Matrix multiplication is not possible.")
else:
    M1 = np.zeros((r1,c1))
    M2 = np.zeros((r2,c2))

    print("Elements in Matrix1: ")
    for i in range(0,r1):
        for j in range(0,c1):
            M1[i][j] = float(input(f"M1[{i}][{j}]"))
    print("Elements in Matrix2: ")
    for i in range(0,r2):
        for j in range(0,c2):
            M2[i][j] = float(input(f"M2[{i}][{j}]"))

    M = np.dot(M1,M2)

    print("Matrix1: ")
    print(M1)
    print("Matrix2: ")
    print(M2)
    print("Resultant Matrix: ")
    print(M)