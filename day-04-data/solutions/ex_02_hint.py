"""Hints for ex_02

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # One-liner
    transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print(transpose)

    # Or use zip (but implement manually for practice)
