def matrizIdentidade(n):
    toReturn = []

    for i in range(n):
        toReturn.append([])
        for j in range(n):
            if i == j:
                toReturn[i].append(1)
            else:
                toReturn[i].append(0)

    return toReturn

