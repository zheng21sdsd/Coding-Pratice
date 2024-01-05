# # class Solution(object):
# #     def minSubArrayLen(self, target, nums):
# #         """
# #         :type target: int
# #         :type nums: List[int]
# #         :rtype: int
# #         """
# #         begin = 0
# #         end = len(nums)
# #         add_begin = nums[begin+1::]
# #         end_sub = nums[:len(nums)-1:]
# #         while sum(nums)>=target:
# #             min_len = len(nums)
# #             print('nums:', nums)
# #             print('add_begin:',add_begin)
# #             print('end_sub:', end_sub)
# #             print('min_len:',min_len)
# #             print('*************************************' * 2)
# #             if sum(add_begin)>=target:
# #                 if min_len>Solution.minSubArrayLen(self,target,add_begin):
# #                     min_len = Solution.minSubArrayLen(self,target,add_begin)
# #                     print('min_len_add_begin:',min_len)
# #
# #             if sum(end_sub)>=target:
# #                 if min_len>Solution.minSubArrayLen(self,target,end_sub):
# #                     min_len = Solution.minSubArrayLen(self,target,end_sub)
# #             return min_len
# #         else:
# #             return 0
# class Solution(object):
#     def minSubArrayLen(self, target, nums):
#         length = len(nums)
#         i = 0
#         min_len = length
#         while i < length:
#             left = i
#             right = i
#             while left - 1 >= 0 and sum(nums[left-1:i:]) <= target:
#                 left -= 1w
#             while right + 1 <= length and sum(nums[i:right+1:]) <= target:
#                 right += 1
#             while left - 1 >= 0 and right + 1 <= length and sum(nums[left - 1:right + 1]) <= target:
#                 left -= 1
#                 right += 1
#             print('left:', left)
#             print('right:', right)
#             print('i:', i)
#
#
#             Len = right - left + 1
#             print('length:', length)
#             print('min_len:', min_len)
#             print('Len:', Len)
#             print('***' * 33)
#             if min_len > Len:
#                 min_len = Len
#             i += 1
#         return min_len
#
#
# object_test = Solution()
#
# print(object_test.minSubArrayLen(target = 7, nums =[2,3,1,2,4,3]))
#
#
#
#
#
#
#
#
#
#
# def BTree_H(Tree):
#     if Tree == None:
#         return BTree_H(Tree) = 0
#     else:
#         if Tree.lchild == None:
#             return BTree_H(Tree.lchild) = 0
#         if Tree.rchild == None:
#             return BTree_H(Tree.rchild)  = 0
#         if Tree.lchild != None and Tree.lchild != None:
#             return BTree_H(Tree.lchild)+1 if BTree_H(Tree.lchild)>BTree_H(Tree.rchild) else BTree_H(Tree.rchild)+1
#
#
#
# #
# #
# #
# #
# #
# #
#
#
# def f(m, n):
#     if n == 0:
#         return 1
#     elif m < n or m == 0:
#         return 0
#     else:
#         return f(m - 1, n) + f(m, n-1)
# print('共有',f(20,10),'种排队购票方式')
#
#
#
#
#
#
#
#
#


# f(m,n)的次数是由其子问题之和得出来的
# 卖给第一个人为身怀50元人民币的玩家 那其次数为f(m-1,n)
# 卖给第一个人为身怀100元人民币的玩家 那其次数为f(m,n-1)
# 当然限定条件很简单，就是第几个百元人名币玩家前面必须有几个五十元人名币玩家即m>=n 且n != 0
# 函数出口我们知道就是n = 0






# def build(arr,root,end):
#     while True:
#         child = 2*root+1
#         ##当到底了前面的节点后 子节点可以作为根节点了 就得while 来确保作为根节点的子节点也满足最大堆序
#         if child >end:
#             break # 孩子超过了最后一个节点
#         if child+1<end and arr[child+1]>arr[child]:
#             child+=1
#             # 选出孩纸中的最大的一个
#         if arr[root]<arr[child]:
#             arr[root],arr[child] = arr[child],arr[root]
#             root = child
#             # 判断孩子和根节点的关系要保证根节点最大且子节点作为的根节点也是最大
#         else:
#             break
#
#
#
#
#  # 左子节点的位置
#        # ，则终止循环
#
#         # 若右子节点在最后一个节点之前，并且右子节点比左子节点大，则我们的孩子指针移到右子节点上
#
#         # 若最大的孩子节点大于根节点，则交换两者顺序，并且将根节点指针，移到这个孩子节点上
#
#
#
# def heap_sort(arr):
#     ## 最后一个**根节点**的位置是n//2-1 或者说 每个根节点都有类似于这个
#     n = len(arr)
#     last_root =  n // 2+1# 确认最深最后的那个根节点的位置
#     for root in range(last_root,-1,-1):    # 由后向前遍历所有的根节点，建堆并进行调整
#         build(arr,root,n-1)
#     ### 最大堆已经够好了，就得每次把最大堆的堆顶元素和最后一个元素进行对调
#     # for root in range(len(arr)):
#     #     arr[root],arr[n] = arr[n],arr[root]
#     for end in range(n-1,0,-1):
#         arr[0],arr[end] = arr[end],arr[0]#最大的到最后了
#         build(arr,root,end-1)#最前面的堆进行排序 然会排除掉end
#
#
#
#
#   # 调整完成后，将堆顶的根节点与堆内最后一个元素调换位置，此时为数组中最大的元素，然后重新调整堆，将最大的元素冒到堆顶。依次重复上述操作
#
#
#
#
# # 测试数据
# if __name__ == '__main__':
#     import random
#
#     random.seed(54)
#     arr = [random.randint(0, 100) for _ in range(10)]
#     print("原始数据：", arr)
#     heap_sort(arr)
#     print("堆排序结果：", arr)
#
# # 输出结果
#
#
# # 原始数据： [17, 56, 71, 38, 61, 62, 48, 28, 57, 42]
# # 堆排序结果： [17, 28, 38, 42, 48, 56, 57, 61, 62, 71]



import matplotlib.pyplot as plt
x = [i for i in range(10)]
y = [i**2 for i in range(10)]
plt.plot(x, y, "-bo", label="try_just")    #线型，颜色，标记，名称
plt.legend(loc="right")     #放置位置
plt.show()
