import copy

def reducaoMatriz(Matriz,i,j):

    M = copy.deepcopy(Matriz)

    if M == None or len(M) == 1:
        return None
    
    M.pop(i)

    for k in range(len(M)):
        M[k].pop(j)

    return M