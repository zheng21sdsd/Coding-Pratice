# class Solution:
#     def findTheArrayConcVal(self, nums):
#         if len(nums) > 1:
#             print(nums)
#             temp_sum = int(str(nums[0]) + str(nums[len(nums)-1]))
#             print(temp_sum)
#             return temp_sum + Solution.findTheArrayConcVal(self, nums[1:len(nums) - 1])
#         elif len(nums) == 1:
#             return nums[0]
#         else:
#             return 0
# A = Solution()
# print(A.findTheArrayConcVal([5,14,13,8,12]))
# # b = [7,52,2,4]
# # print(b[0:len(b)])
# class Solution:
#     ##最大子数组和
#     def findTheArrayConcVal(self, nums,left,right):
#         if left-right>0:
#             return 0
#         if left-right == 0:###数组为单个元素
#             return nums[left]
#         if right-left>=1:###数组为多个元素时 进行分治
#             sum1 =int(str(nums[left])+str(nums[right]))
#             return sum1+Solution.findTheArrayConcVal(self,nums,left+1,right-1)
# A = Solution()
# print(A.findTheArrayConcVal([5,14,13,8,12],0,4))



class Solution:
    def findTheArrayConcVal(self, nums):
        left = 0
        right = len(nums)-1
        if left-right>0:
            return 0
        if left-right == 0:###数组为单个元素
            return nums[left]
        if right-left>=1:###数组为多个元素时 进行分治
            sum1 =int(str(nums[left])+str(nums[right]))
            return sum1+Solution.findTheArrayConcVal(self,nums[left+1:right])
A = Solution()
print(A.findTheArrayConcVal([5,14,13,8,12]))
a = [5,14,13,8,12]
