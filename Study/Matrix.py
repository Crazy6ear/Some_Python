""""программа, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой,
 содержащей только строку "end" (без кавычек).Программа выводит матрицу того же размера, у которой каждый
  элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
  У крайних символов соседний элемент находится с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению."""
A, enter = [], input()
while str(enter) != 'end':
    A.append([int(i) for i in enter.split()])
    enter = input()
il, jl = len(A), len(A[0])
form = [[sum([A[i - 1][j], A[i - il + 1][j], A[i][j - 1], A[i][j - jl + 1]]) for j in range(jl)] for i in range(il)]

for i in range(il):
    if i != 0:
        print('\n', end='')
    for j in range(jl):
        print(form[i][j], end=' ')

#Пример ввода:     Пример Вывода:
#9 5 3             3 21 22 
#0 7 -1            10 6 19 
#-5 2 9            20 16 -1
#end