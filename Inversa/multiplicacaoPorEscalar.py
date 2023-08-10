def multiplicacaoPorEscalar(escalar , Matriz):
    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            Matriz[i][j] *= escalar