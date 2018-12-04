s = [int(i) for i in (input()).split()]
x = [0 for i in range(len(s))]
y = [0 for i in range(len(s))]
mat = [s]
mat.append(x)
mat.append(y)
mat[1][0] = 1
mat[2][0] = 1
for i in range(len(s)):
    a = 0
    b = 0
    for j in range(i):
        if mat[0][j] < mat[0][i]:
            if mat[2][j] > a:
                a = mat[2][j]
        if mat[0][j] > mat[0][i]:
            if mat[1][j] > b:
                b = mat[1][j]
    mat[1][i] = a + 1
    mat[2][i] = b + 1
print(max(max(mat[1]), max(mat[2])))
