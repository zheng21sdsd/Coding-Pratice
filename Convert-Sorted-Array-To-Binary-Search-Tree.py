# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Tree:
    def inorder_tree_walk(self, nums):
        if nums !=None:
            self.inorder_tree_walk(nums.left)
            print(nums.val,end=' ')###中序遍历
            self.inorder_tree_walk(nums.right)
    def preorder_tree_walk(self, nums):
        if nums !=None:
            print(nums.val, end=' ')  ###前序遍历
            self.inorder_tree_walk(nums.left)
            self.inorder_tree_walk(nums.right)
    def laterorder_tree_walk(self, nums):
        if nums !=None:
            self.inorder_tree_walk(nums.left)
            self.inorder_tree_walk(nums.right)
            print(nums.val, end=' ')  ###后序遍历
    def sortedArrayToBST(self, nums) :
        ##用递归方法建立二叉树
        #判断数组 是否存在
        if not nums:
            return None
        mid = len(nums)//2

        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node

node = Tree().sortedArrayToBST(nums = [-10,-3,0,5,9])

# 进行遍历 中序遍历 左中右
print('中序 左中后',end=' ')
Tree().inorder_tree_walk(node)
print()
print('前序： 中左右',end=' ')
Tree().preorder_tree_walk(node)

print('后序： 左右中',end = ' ')
Tree().laterorder_tree_walk(node)

