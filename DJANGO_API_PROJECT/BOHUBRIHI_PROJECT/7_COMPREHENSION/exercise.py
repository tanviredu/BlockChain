my_matrix = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]

## make it with a for loop

matrix = []
for item in range(3):
    matrix.append([])
    for i in range(1,5):
        matrix[item].append(i)
print(matrix)


## make it with list comprehension
matrix = [[i for i in range(1,5)] for j in range(3)]
print(matrix)
