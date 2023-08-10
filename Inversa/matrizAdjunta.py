from Inversa.transposta import transposta
from Inversa.matrizDosCofatores import matrizDosCofatores

def matrizAdjunta(Matriz):
    return transposta(matrizDosCofatores(Matriz))