import copy
from reducaoMatriz import reducaoMatriz

def determinante(Matriz):
    M = copy.deepcopy(Matriz)
    if M == None:
        return None
    
    if len(M) == 1:
        return M[0][0]
    
    if len(M) == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    
    # somatória de i=1 até n de ai1 * -1^i+1 * detAi1

    toReturn = 0
    for i in range(len(M)):
        valorA = M[i][0]
        cofator = ((-1)**(i+2))*determinante(reducaoMatriz(M,i,0))
        toReturn += valorA * cofator

    return toReturn


