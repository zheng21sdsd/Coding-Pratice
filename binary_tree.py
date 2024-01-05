###理解何为二叉树 树本省有左右两个子节点 其子节点也可以作为树的根节点，所以如何定义数据结构尤为重要1！！

# 首先先定义树
# from collections import Iterable
# class Node:
#     def __init__(self,value,left=None,right = None):
#         self.value = value  #节点值
#
#         self.left = left  #左子节点
#         self.right = right  #右子节点
#
# class BinaryTree:
#     def __init__(self,seq = ()):
#         assert isinstance(seq,Iterable)    #确保输入的参数为可迭代对象
#         self.root = None
#         self.insert(*seq)
#     def insert(self,*args):
#         if not args:
#             return
#         if not self.root:
#             self.root = Node(args[0])
#             args = args[1:]
#         for i in args:
#             seed = self.root
#             while True:
#                 if i>seed.value:
#                     if not seed.right:
#                         node = Node(i)###一个值为i的节点
#                         seed.right = node
#                         break
#                     else:
#                         seed = seed.right
#
#                 else:
#                     if not seed.left:
#                         node = Node(i)###一个值为i的节点
#                         # seed.left = node
#                         break
#                     else:
#                         seed = seed.left
#
#
# l = [40,20,30,70,60,75,71,74]
# tree = BinaryTree(l)
# print(tree)
# print(tree.root)
# tree.root.value


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
a = [i for i in range(10)]
print(a)
print(a[:4])