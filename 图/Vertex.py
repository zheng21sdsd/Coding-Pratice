class Vertex:   ### 顶点类 包含了顶点的邻居和变得权重
    ##Vertex 使用字典connnectedTo来记录预期相连的顶点，以及每一条边的权重
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    ##addNerghbor 方法 添加一个顶点到另一个顶点的链接
    def addNerghbor(self,nbr,weight = 0):
        self.connectedTo[nbr] = weight

###打印这个顶点和哪些点是邻居
    def __str__(self):
        return str(self.id)+'connectedTo: '+str([x.id for x in self.connectedTo])

    def getConnection(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]