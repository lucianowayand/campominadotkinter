
class Matrix:
    def __init__(self,linhas,colunas):
        self.matrix = []
        self.linhas = linhas
        self.colunas = colunas
        self.addLinhas(linhas)

    def addLinhas(self,r):
        for i in range(r):
            self.matrix.append([])

    def initiateMatrix(self);
        for i in range (self.linhas):
            for j in range(self.colunas):
                self.matrix[i].append(j)

m = Matrix(10,10)
