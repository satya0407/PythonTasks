import random

#Create an n*n matrix from zeros and creates a simple diagonal with ones.

n = int(input('Adj meg egy számot!'))
matrix = []
for i in range(n):
    lista = []
    for j in range(n):
        if (i-j) == 0:
            lista.append(1)
        else:
            lista.append(0)
    matrix.append(lista)
for i in matrix:
    print(i)
print('\n')

#Creates an n*n matrix with random integers splits the matrix by the diagonal
#Search for highest value in both parts

n = int(input('Mekkora legyen a mátrix?'))
matrix = []
for i in range(n):
    lista = []
    for j in range(n):
        x = random.randint(1, 100)
        lista.append(x)
    matrix.append(lista)
for i in matrix:
    print(i)
upper_matrix = []
lower_matrix = []
for i in range(n):
    for j in range(n):
        if j <= i:
            lower_matrix.append(matrix[i][j])
        if j >= i:
            upper_matrix.append(matrix[i][j])
lower_max = 0
upper_max = 0
for i in lower_matrix:
    if i > lower_max:
        lower_max = i
for i in upper_matrix:
    if i > upper_max:
        upper_max = i
if lower_max > upper_max:
    print(f'Ez a legnagyobb szám, ami az alsó mátrixban található: {lower_max}')
elif upper_max > lower_max:
    print(f'Ez a legnagyobb szám, ami a felső mátrixban található: {upper_max}')
else:
    print(f'Ez a legnagyobb szám, ami mindkét mátrixban megtalálható: {lower_max}')
print('\n')

#Creates a 5*5 matrix then transpose the rows into coloums.

n = 5
was = []
matrix = []
for i in range(n):
    lista = []
    j = 0
    while j < n:
        x = random.randint(1, 50)
        if x not in was:
            lista.append(x)
            was.append(x)
            j += 1
    matrix.append(lista)
for i in matrix:
    print(i)
print('\n')
new_matrix = []
for i in range(n):
    lista = []
    for j in range(n):
        lista.append(matrix[j][i])
    new_matrix.append(lista)
for i in new_matrix:
    print(i)