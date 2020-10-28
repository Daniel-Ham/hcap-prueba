import numpy as np
#Funcion que calcula la matriz resultante C despues de aplicar la operacion convolucion de A*B
def convolucion(A,B):
    C=np.zeros((A.shape[0]-2,A.shape[1]-2))
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            temp=0
            for ii in range(B.shape[0]):
                for jj in range(B.shape[1]):
                    temp+=A[ii+i][jj+j]*B[ii][jj]
            C[i][j]=temp
    return C
A=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[0,0,1,16,17,18],[0,1,0,7,23,24],[1,7,6,5,4,3]])
B= np.array([[1,1,1],[0,0,0],[2,10,3]])
print(convolucion(A,B))
