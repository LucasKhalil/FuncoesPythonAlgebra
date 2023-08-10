from Inversa.multiplicacaoPorEscalar import multiplicacaoPorEscalar
from Inversa.matrizAdjunta import matrizAdjunta
from cofatorEDeterminante import determinante

def inversa(Matriz): # 1/detMatriz * adjMatriz
    return multiplicacaoPorEscalar(1/determinante(Matriz),matrizAdjunta(Matriz))
