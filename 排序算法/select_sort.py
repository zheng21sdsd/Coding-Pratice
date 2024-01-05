# 可以看作是冒泡的改进，每次找一个最小的元素交换，每一轮只需要交换一次
# 时间复杂度：O(n^2)
def select_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]

unsorted_array = [64, 34, 25, 12, 22, 11, 90]
print('unsorted_array',unsorted_array)
select_sort(unsorted_array)
print('sorted_array',unsorted_array)
