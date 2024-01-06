# 题目：迷宫问题
#       1
# 3     2     6
# 4     5    7(出口)


# 路口 动作 结果
# 1(入口) 正向走  进到2
# 2 右拐弯 进到3
# 3 右拐弯 进到4
#
# 4 堵死 回溯 退到3
# 3 堵死 回溯 退到2
# 2  正向走 进到5
# 5(堵死) 回溯 退到 2
# 2 右拐弯 进到6
# 6 拐弯  进到7
# (出口)
## 上面就是小型迷宫的交通路口数据
# 定义迷宫数据结构最重要
maze_graph = {
    1:[2],
    2:[3,5,6],
    3:[4],
    4:[3],
    5:[2],
    6:[7],
    7:[]### 出口
}
def dfs(maze_graph,start_node,target_node,visited_nodes,path):
    visited_nodes[start_node] = True
    path.append(start_node)
    ## 判断开始节点是否为目标节点
    if start_node == target_node:
        print('找到啦路径')
        return path
    ## 发现当前节点不是目标节点   遍历该节点可以一步到达的节点
    for node in maze_graph[start_node]:
        ## 邻居节点 未遍历过
        if not visited_nodes[node]:
            path_found = dfs(maze_graph,node,target_node,visited_nodes,path)
            if path_found:
                return path_found
    ### 遍历完了这个节点  发现从这个结点开始  无法到达出口（自己不是出口  而且通过自己的邻居也无法到达出口）
    # 4 发现不行  就把四pop出来  就像相当于回溯
    path.pop()

## 初始化访问路径
visited_nodes = {node:False for node in maze_graph}
## 初始化路径
start_node = 1
target_node = 7
path_found = dfs(maze_graph,start_node,target_node,visited_nodes,[])
if path_found:
    print('f找到了从{}到{}的路径'.format(start_node,target_node))
    print(path_found)
    print(visited_nodes)
else:
    print('未找到路径')

