# # 01背包问题
#
# W = [16,15,25] #价值
# V = [45,25,25]# 体积
# B = 30 #最大体积
# Solutions = []
# ### 定义二叉树
# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data
#
# def insert_l(root, data):
#     if root is None:
#         return Node(data)
#     root.left =  data
#     return root
# def insert_r(root, data):
#     if root is None:
#         return Node(data)
#     root.right = data
#     return root
# # 定义一个函数inorder，用于中序遍历二叉树
# # def inorder(root):
# #     # 如果根节点存在
# #     if root:
# #         # 递归遍历左子树
# #         inorder(root.left)
# #         # 打印根节点
# #         print(root.data),
# #         # 递归遍历右子树
# #         inorder(root.right)
#
# print("Inorder traversal of the constructed tree is")
# inorder(r)
# # restraint =
#
#include<iostream>
import math



# 用于记录是否存放当前地物体
inOut = [0, 0, 0, 0]
# 保存最多的价值
value = 0
# 定义背包的总共的重量的
bagVolume = 9

# 描述：背包问题的约束条件，当传入对应的序号，就去判定是否要放对应的物品
# 参数：放入包中物体的序号
# 返回：当前物体总重量和背包容量的关系
#     true：表示没有超重
#     false：表示超重
# 原理：判定当前的物品的总重量，是不是小于物体的实际重量
def bagConstraint(m, weight):
    # 一直遍历m层之前的所有物体，求出其对应的重量
    allweight = sum(inOut[i] * weight[i] for i in range(m + 1))

    # 比较当前的物体总重量和背包的总重量关系
    return allweight <= bagVolume

# 描述：深度优先搜索的函数，递归函数
# 参数：m:是要装入背包的物品的数量
#     weight：是背包中各个物品的重量
#     value：是背包中各个物品的价值
# 返回：最终返回的是最大的价值
def bagProblem(m, weight, valueAll):
    global value

    # 首先确定终止条件，那就比较最大值
    if m == 4:
        sum1 = 0
        sum1 = sum(inOut[i] * valueAll[i] for i in range(m))
        # 比较最大值
        if sum1 > value:
            value = sum1
    else:
        # 没有到达终止条件，继续向下进行递归
        for i in range(2):
            inOut[m] = i
            # 判定是否满足对应约束条件
            if bagConstraint(m, weight):
                # 满足约束条件，继续向下进行递归的
                bagProblem(m + 1, weight, valueAll)

# 输入样例
num = 4
weight = [2, 3, 4, 5]
valueAll = [3, 4, 5, 6]

# 调用函数
bagProblem(0, weight, valueAll)

# 输出结果
print("最终的结果是：", value)#include<iostream>
