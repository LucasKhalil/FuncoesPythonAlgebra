from Auxiliares.reducaoMatriz import reducaoMatriz

def cofator(Matriz,i,j): # cofator de aij = (-1)**(i+j) * determinante(reducaoMatriz(Matriz,i,j))
    valorDeUm = (-1)**(i+j+2)
    detMatriz = determinante(reducaoMatriz(Matriz,i,j))

    return valorDeUm * detMatriz


def determinante(Matriz):
    if Matriz == None:
        return None
    
    if len(Matriz) == 1:
        return Matriz[0][0]
    
    if len(Matriz) == 2:
        return Matriz[0][0] * Matriz[1][1] - Matriz[0][1] * Matriz[1][0]
    
    # somatória de i=1 até n de ai1 * -1^i+1 * detAi1

    toReturn = 0
    for i in range(len(Matriz)):
        valorA = Matriz[i][0]
        cof = cofator(Matriz,i,0)
        toReturn += valorA * cof

    return toReturn
