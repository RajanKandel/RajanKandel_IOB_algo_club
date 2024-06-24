 #python script to find the least square fit of a linear equations represented as a matrix 

import numpy as np 

def reduce_to_RREF(A):
    """
    Reduces a matrix to Reduced Row Echelon Form (RREF) using Gaussian elimination.

    Args:
        A: list of list representing the matrix to be reduced. (This is the square matrix 
            obtained by Transpose(A)*A and with a last column representing the augmented form)

    Returns:
        A upper traingular matrix. 
    """
    m = len(A)
    n = len(A[0])
    for i in range(n):
        
        if A[i][i] == 0 : #interchange the row
            B = A[i]
            A[i] = A[i+1]
            A[i+1] = B  

        if A[i][i] != 1:
            for k in range(n): 
                A[i][k] = A[i][k]/ A[i][i]            
              

        #make everything below the pivot row zero 
        for row in range(i, m):
            if A[row][i] != 0:
                for k in range(n):
                    A[k][row] = A[k][row] - A[k] [row] * A[i][i]    
    return A

A = [[1, 2, 3], [2, 4, 5], [3, 6, 7]]
print("Original matrix:", A)

reduced_matrix = reduce_to_RREF(A)
print("\nReduced Row Echelon Form:", reduced_matrix)