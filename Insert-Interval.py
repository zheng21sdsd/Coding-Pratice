#
# def init():
#     Intervals = []
#     for i i range(4):
#         Intervals.append(list(map(int,input().split())))
#     return Intervals
#
# def newInterval():
#     newInterval = []
#     return newInterval
#
# def Insert_Int(Intervals, newInter):
#     pass
# def showarr(arr):
#     for i in range(len(arr)):
#         print(arr[i],end=' ')
#     print()
#
# Intervals = init()
# newInter = newInterval()
# arr = Insert_Int(Intervals, newInter)
# showarr(arr)
#
#
# ###


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ## 暂存前面数组
        temp = []
        ##暂存后面数组
        temp_after = []
        ## 插入
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                temp = intervals[0:i]
                temp.append(newInterval)
                temp_after = intervals[i + 1:]
                arr = temp + temp_after
                break
        ### 判断
        for i in range(len(arr)):
            pass



