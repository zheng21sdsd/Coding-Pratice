# class Solution(object):
#     def canJump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         n = len(nums)-1
#         if n == 0:
#             print('dsd')
#             return False
#         if n == 1:
#             return True
#         if nums[n-1]>=1:
#             return self.canJump(nums[:n])
#         else:
#             print('111111')
#             return False
#
# Solution().canJump(nums =
# [2,3,1,1,4]


class Solution(object):
    def canJump(self, nums):
        max_i = nums[0]
        for index,jump in enumerate(nums):
            if max_i>=index and jump+index>=max_i:
                max_i = jump+index
        if max_i>=len(nums)-1:
            return True
        else:
            return False
Solution().canJump(nums =
[1,0,1,0])