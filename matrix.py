class Matrix:
    def __init__(self,linhas,colunas):
        self.matrix = []
        self.linhas = linhas
        self.colunas = colunas
        self.addLinhas(linhas)

    def addLinhas(self,r):
        for i in range(r):
            self.matrix.append([])

m = Matrix(10,10)

print(m.matrix)
