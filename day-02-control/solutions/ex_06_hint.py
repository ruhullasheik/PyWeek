"""Hints for ex_06

This is an advanced exercise — don't worry if it takes time.

Step-by-step breakdown for 2×2 matrices:

     A = [[1, 2],      B = [[5, 6],
          [3, 4]]           [7, 8]]

 C[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0]   # = 1*5 + 2*7 = 19
 C[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1]   # = 1*6 + 2*8 = 22
 C[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0]   # = 3*5 + 4*7 = 43
 C[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1]   # = 3*6 + 4*8 = 50

Notice the pattern: each C[i][j] is sum of A[i][k] * B[k][j] over k.
This becomes a triple loop:

    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]

    print(C)

General case: use len() for dimensions instead of hardcoded 2.
"""
