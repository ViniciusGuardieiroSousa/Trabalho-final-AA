import numpy as np
import time
import matplotlib.pyplot as plt

def createMatrix(n):
    return np.random.randint(100,size=(n,n),dtype=np.longlong)
        
def simpleMultiplication(m1, m2):
    n = len(m1)
    result = createMatrix(n)
    for i in range(n):
        for j in range(n):
            result[i][j] = 0
            for k in range(n):
                result[i][j] = result[i][j] + (m1[i][k] * m2[k][j])
    return result

def addMatrix(m1,m2):
    return np.add(m1,m2)

def subMatrix(m1,m2):
    return np.subtract(m1,m2)

def split(matrix): 
    row, col = matrix.shape 
    row2, col2 = row//2, col//2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def strassenMultiplication(m1,m2):
    if len(m1) <= 2:
        return np.matmul(m1,m2)

    a11, a12, a21, a22 = split(m1)
    b11, b12, b21, b22 = split(m2)
    
    P1 = strassenMultiplication(a11, subMatrix(b12, b22))
    P2 = strassenMultiplication(addMatrix(a11, a12), b22)
    P3 = strassenMultiplication(addMatrix(a21, a22), b11)
    P4 = strassenMultiplication(a22, subMatrix(b21, b11))
    P5 = strassenMultiplication(addMatrix(a11, a22), addMatrix(b11, b22))
    P6 = strassenMultiplication(subMatrix(a12, a22), addMatrix(b21, b22))
    P7 = strassenMultiplication(subMatrix(a11, a21), addMatrix(b11, b12))

    c11 = addMatrix(subMatrix(addMatrix(P5, P4), P2), P6)
    c12 = addMatrix(P1, P2)
    c21 = addMatrix(P3, P4)
    c22 = subMatrix(subMatrix(addMatrix(P1, P5), P3), P7)
    return np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22)))) 


def main():
    numberOfFullTest = 11
    numberOfExecution = 40
    simpleData = []
    strassenData = []
    nData = []
    print("N\t\tTempo em segundos simple\tTempo em segundos strassen")
    print("----------------------------------------------------------------------------")
    for i in range(numberOfFullTest):
        n = pow(2,i)
        simple = 0
        strassen = 0
        for j in range(numberOfExecution):
            m1 = createMatrix(n)
            m2 = createMatrix(n)
            start_time = time.time()
            m4 = strassenMultiplication(m1,m2)
            strassen = strassen + (time.time() - start_time)
            start_time = time.time()
            m3 = simpleMultiplication(m1,m2)
            simple = simple + (time.time() - start_time)
            
        simpleData.append(simple/numberOfExecution)
        strassenData.append(strassen/numberOfExecution)
        nData.append(n)
        print("%d:\t\t\t%f\t\t\t%f" % (nData[i], simpleData[i], strassenData[i]))
    
    #plotar gráfico
    plt.plot( nData, simpleData, color = 'blue') # linha pontilha orange
    plt.plot( nData, strassenData, color = 'red')
    plt.xlabel("n")
    plt.ylabel("Tempo em segundos")
    plt.show()
    
main()
