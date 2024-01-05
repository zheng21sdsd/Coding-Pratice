## 所谓快排就是一次把一个数的位置确定好
# def quick_sort(arr):
#     low = 0
#     high = len(arr)-1
#     i = low
#     j = high
#     print('high',high)
#     mid = (low+high)//2
#     while i!=j:
#         print('j == ',j)
#         if not arr[j]<arr[mid]:
#             j-=1
#         if not arr[i]>arr[mid]:
#             i+=1
#         if arr[j]< arr[mid] and arr[i]>arr[mid]:
#             arr[j],arr[i] = arr[i],arr[j]
#     quick_sort(arr[low:mid-1])
#     quick_sort(arr[mid+1:high])
#
# unsorted_array = [64, 34, 25, 12, 22, 11, 90]
# print('unsorted_array', unsorted_array)
# quick_sort(unsorted_array)
# print('sorted_array', unsorted_array)
#
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    low = 0
    high = len(arr)-1
    mid = (low+high)//2
    pivot = arr[mid]
    left = [x for x in arr if x<pivot]
    mid = [x for x in arr if x==pivot]
    right = [x for x in arr if x>pivot]
    return quick_sort(left)+mid+quick_sort(right)

unsorted_array = [64, 34, 25, 12, 22, 11, 90]
print('unsorted_array', unsorted_array)
unsorted_array = quick_sort(unsorted_array)
print('sorted_array', unsorted_array)
