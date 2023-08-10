from Auxiliares.matrizIdentidade import matrizIdentidade
from cofatorEDeterminante import determinante

def escalonamento(Matriz):
    if determinante(Matriz) != 0:
        return matrizIdentidade(len(Matriz))
    
    #TODO implementar o caso de a determinante da Matriz ser igual a 0
    
    return None
