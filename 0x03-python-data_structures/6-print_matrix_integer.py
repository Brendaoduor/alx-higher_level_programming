#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
       """matrix = [[column * row for column in range(3)] for row in range(3)]
          matrix[column][row] = column
          print(matrix[column][row], end=" ")"""    
n = 3
m = 3
matrix = [0] * n
for x in range(n):
    matrix[x] = [0] * m
print(matrix)


print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
