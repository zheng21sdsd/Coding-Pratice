# def sorted_node(nodes):
#     ## 先不合并  看给出数据是否合适
#     # 假设合适
#     return nodes
#
# # def get_tree(node1,node2):
# #
#
# ## 先构建输入
# nodes = [[1,0,'a'],[3,1,'c']]
# # for i in range(2):
# #     node = []
# #     for j in range(2):
# #         node.append(j)
# #     node.append(node)
# ## 先排序
# # nodes = sorted_node(nodes)
# ### 最后一个节点
# temp = nodes[len(nodes)-1]
# ## 节点合并
# for i in range(len(nodes)-1,-1,-1):
#     nodes[i].append(temp)
#     temp = nodes[i]
# # 输出node
# # print(temp)
# #
# #
# class tree():
#     def init(self,id,parid,name,node):
#         self.id = id
#         self.parid = parid
#         self.name = name
#         self.child = node
#     ##
nodes = [[1,0,'a'],[3,1,'c']]
temp = nodes[0]

def addnode(temp,nodes):## node[0]节点
    if len(nodes) == 1:
        nodes.append([])
        merge = temp.append(nodes)
        # print(merge)
        return merge
    for j in range(1,len(nodes)):
        for i in range(len(nodes)):
            if temp[0] == nodes[i][1]:
                addnode(temp,nodes[i:])
                # addnode(temp,nodes[i:])

        temp = nodes[j]
addnode(temp,nodes)
## 逻辑关系   逻辑有点

