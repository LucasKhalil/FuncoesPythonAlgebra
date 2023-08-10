import copy

def transposta(Matriz):
    M = copy.deepcopy(Matriz)
    for i in range(len(Matriz)):
        for j in range(i,len(Matriz)):
            M[i][j] = Matriz[j][i]
            M[j][i] = Matriz[i][j]

    return M
