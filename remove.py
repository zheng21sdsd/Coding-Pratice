class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        need_pop = []
        n = len(nums)
        for i in range(n):
            # print(i)
            if nums[i] == val:
                need_pop.append(i)
        for j in range(len(need_pop)-1,-1,-1):
            nums.pop(need_pop[j])

        return n-len(need_pop)
nums = [3,2,2,3]
Solution().removeElement(nums,3)

print(Solution().removeElement([3,2,2,3],3),end=' ')
print(nums)