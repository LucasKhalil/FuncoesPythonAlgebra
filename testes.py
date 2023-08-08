import determinante as det
import reducaoMatriz as rm

# teste 1: REDUÇÃO DE MATRIZ

# teste 1.1: Matriz nula OK
M = None
assert rm.reducaoMatriz(M,0,0) == None

# teste 1.2: Matriz 1x1 OK 
M = [[10]]
assert rm.reducaoMatriz(M,0,0) == None

# teste 1.3: Matriz 2x2 OK
M = [[1,2],[3,4]]
assert rm.reducaoMatriz(M,0,0) == [[4]]

# teste 1.4: Matriz 3x3 OK
M = [[1,2,3],[4,5,6],[7,8,9]]
assert rm.reducaoMatriz(M,2,1) == [[1,3],[4,6]]

# teste 1.5: Matriz 4x4 com valores nulos OK
M = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
assert rm.reducaoMatriz(M,0,0) == [[0,0,0],[0,0,0],[0,0,0]]


# teste 2: DETERMINANTE 

# teste 2.1: Matriz nula OK
M = None
assert det.determinante(M) == None

# teste 2.2: Matriz 1x1 OK
M = [[10]]
assert det.determinante(M) == 10

# teste 2.3: Matriz 2x2 OK
M = [[1,2],[1,2]]
assert det.determinante(M) == 0

# teste 2.4: Matriz 3x3
M = [[1,2,3],[4,4,4],[1,4,6]]
assert det.determinante(M) == 4

# teste 2.5: Matriz 4x4
M = [[-1,2,3,4],[0,4,2,0],[-1,2,-3,0],[2,5,3,1]]
assert det.determinante(M) == 144

