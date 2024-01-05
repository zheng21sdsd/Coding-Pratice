#递归
def count_ways(n):
    if n<3:
        return n
    if n == 3:
        return 4
    return count_ways(n-1)+count_ways(n-2)+count_ways(n-3)
# ## 迭代：;
# def count_ways(n):
#     if n<3:
#         return n
#     if n == 3:
#         return 4
#     else:
#         ### 离得最远的 离得第二远的 离得最近的  most_far second_far  near_far
#         most_far = 1
#         second_far = 2
#         near_far = 4
#         for i in range(4,n+1):
#             most_far,second_far,near_far = second_far,near_far,most_far+second_far+near_far
#         return near_far
# ways = count_ways(10)
# print(f"10级楼梯有 {ways} 种走法。")

#
# def count_ways(n):
#     if n <= 3:
#         return n
#     else:
#         a, b, c, d = 1, 2, 4, 0
#         for i in range(4, n + 1):
#             d = a + b + c
#             a, b, c = b, c, d
#         return d
#
# ways = count_ways(10)
# print(f"10级楼梯有 {ways} 种走法。")

# def count_ways(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4
#     else:
#          return count_ways(n-1)+count_ways(n-2)+count_ways(n-3)

ways = count_ways(10)
print(f"10级楼梯有 {ways} 种走法。")

# print(max([i for i in range(1,10//2)]))
# def dp(n):
#     if n>1:
#         b = [dp(i)*dp(n-i) for i in range(1,n//2)]
#         print(b)
#         a = max()
#         return a
#     else:
#         return n
# print(dp(8))


# OK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         need_pop = []
#         n = len(nums)
#         for i in range(n):
#             print(i)
#             if nums[i] == val:
#                 need_pop.append(i)
#         for j in need_pop[::-1]:
#             nums.pop(j)
#
#         return n-len(need_pop)
# Solution().removeElement([3,2,2,3],3)


# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         need_pop = []
#         n = len(nums)
#         for i in range(n):
#             print(i)
#             if nums[i] == val:
#                 need_pop.append(i)
#         for j in range(len(need_pop)-1,-1,-1):
#             nums.pop(need_pop[j])
#
#         return n-len(need_pop)
# Solution().removeElement([3,2,2,3],3)





#
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         nums3 = []
#         i = 0 ##nums1
#         j = 0##nums2
#         orilength = len(nums1)
#         for t in range(orilength,m,-1):
#             # print(t-1)
#             nums1.pop(t-1)
#         # print(nums1,len(nums1))
#         while len(nums1)>0 and len(nums2)>0:
#             # print(i,j)
#             if nums1[i]<nums2[j]:
#                 pop_num = nums1.pop(i)
#             else:
#                 pop_num = nums2.pop(j)
#             nums3.append(pop_num)
#         # print(nums3)
#         nums3+=nums1
#         nums3+=nums2
#         nums1 = nums3
#         return nums1
# print(Solution().merge([1,2,3,0,0,0],3,[2,5,6],3))