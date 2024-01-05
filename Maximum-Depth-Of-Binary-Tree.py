class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Tree:
    def build_tree(arr,self):
        if not arr:
            return None
        ###建树过程就是整体化和分支话思想，把左边整个子树，看成一个子节点即可
        root = 0
        node = TreeNode(arr[root])
        node.left = self.build_tree(arr[2*root+1:])
        node.right = self.build_tree(arr[2*root+2:])
        return node
    ###求二叉树的最大深度 思想:根节点到左子树的深度 和 根节点到右子树的深度的较大者
    def Max_Depth(self,node):
        if not node:
            return 0
        depth_l = 1+self.Max_Depth(node.left)
        depth_r = 1+self.Max_Depth(node.right)

        return max(depth_l,depth_r)

node= Tree().build_tree([3,9,20,'null','null',15,7])
print(Tree().Max_Depth(node))

