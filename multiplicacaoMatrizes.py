from Auxiliares.criaMatrizNula import criaMatrizNula

def multiplicacaoMatrizes(M1,M2):
    if len(M1[0]) != len(M2): # caso o número de colunas da primeira não seja igual ao de linhas da segunda, não se pode realizar a multiplicação
        return None
    
    novaMatriz = criaMatrizNula(len(M1),len(M2[0])) # cria uma matriz nula com o número de linhas e de colunas da nova matriz

    for i in range(len(novaMatriz)): 
        linha = M1[i] #separo a linha relativa àquele elemento da nova Matriz
        for j in range(len(novaMatriz[0])):
            coluna = [] #separo a coluna relativa àquele elemento da nova Matriz
            for k in range(len(M2)):
                coluna.append(M2[k][j])

            resultado = 0
            for idx in range(len(linha)): #somatória de m1[i][idx] * m2[idx][j] com idx variando entre 0 e o número de elementos na linha
                resultado += linha[idx]*coluna[idx] 

            novaMatriz[i][j] = resultado

    return novaMatriz

     