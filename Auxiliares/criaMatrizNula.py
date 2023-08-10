def criaMatrizNula(linhas,colunas):
    novaMatriz = []
    for i in range(linhas):
        novaMatriz.append([])
        for j in range(colunas):# e o número de colunas da segunda
            novaMatriz[i].append(0)

    return novaMatriz