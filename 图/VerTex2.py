class VerTex:
    ### 定义边包含前向边 后向边 交叉边 还有顶点的指pre 和post
    def __init__(self,value):
        self.value = value
        # self.Fwd_edge = 0
        # self.T_edge = 0
        # self.B_edge = 0
        self.pre = 0
        self.post = 0
class Graph:
    # 定义值为列表的字典作为图
    def __init__(self):
        self.graph = {}
        # self.VerTexs = []
        # self.

    def add_edge(self,u,v):
        ### u,v为顶点
        if not self.graph.get(u):
            self.graph[u] = [v]
        else:
            self.graph[u.value].append(v.value)
    def __str__(self):
        result = ""
        for node, neighbors in self.graph.items():
            neighbors = [x.value for x in neighbors]
            result += f"{node.value}: {neighbors}\n"
        return result

def dfs(g,start):
    



g = Graph()
start = 0
g.add_edge(VerTex(1), VerTex(2))
g.add_edge(VerTex(2), VerTex(3))
g.add_edge(VerTex(3), VerTex(1))
dfs(g,start)


