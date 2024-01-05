class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers)-1
        while right>left:
            if numbers[left]+ numbers[right]>target:
                right-=1
            elif numbers[left]+ numbers[right]<target:
                left+=1
            else:
                return [left+1,right+1]
        return 0
numbers = [2,7,11,15]
target = 9
print(Solution().twoSum(numbers,target))










