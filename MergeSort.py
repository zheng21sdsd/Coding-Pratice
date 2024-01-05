# def MergeSort(arr,left,right):
#     nums = []
#     mid = int((left+right)/2)
#     if left<right:
#         #左边分治
#         Larr = MergeSort(arr,left,mid)
#         #右边分治
#         Rarr = MergeSort(arr,mid+1,right)
#         print('Larr',Larr)
#         print('Rarr',Rarr)
#         ## 接下来把左边和右边完成排序的数组进行归并
#         i = 0
#         j = 0
#         ##这里得同时进行 必须and 为什么 因为两个数组不知道哪一个先到最后面，但是先到了最后面的，我们在里面进行把后面没到的直接加上去，就可以完成，所以这里只能用and
#         while i<=len(Larr)-1 and j<=len(Rarr)-1:
#             if Larr[i]>Rarr[j]:
#                 nums.append(Rarr[j])
#                 if j == len(Rarr)-1:
#                     while i < len(Larr):
#                         nums.append(Larr[i])
#                         i = i+1
#                         print('****',nums)
#                 else:
#                     j = j+1
#
#             else:
#                 # print(f'i1111 = {i},j11111 = {j}')
#                 nums.append((Larr[i]))
#                 # 诺i先到低 那么j数组就可以直接加上去
#                 if  i == len(Larr)-1:
#                     while j<len(Rarr):
#                         nums.append(Rarr[j])
#                         j = j+1
#                 else:
#                     i = i+1
#
#         print('merge_nums',nums)
#         return nums
#     else:
#         #返回单独的数组回去
#         nums = []
#         nums.append(arr[left])
#         print(nums)
#         return nums
#
# arr1 = [6, 1, 2, 5, 4, 3, 9, 7, 10, 8,13,18,75,65,65,95,49,46,65,99,21]
# # arr1 = [14,12,15,13,11,16]
# import time
# begin = time.time()
# print(len(arr1))
# print(MergeSort(arr1,0,len(arr1)-1))
# end = time.time()
# print(end-begin)

###根据中间作为基点把数组分成两份
## 然后递归分治 Larr = MergeSort(arr,left,mid)   --------------   Rarr = MergeSort(arr,mid+1,right)
### 分治之后 我们得把数字进行归并 就是把两个数组合并成一个数组，
#### 几个注意点 1.首先我们要知道，i 和 j都必须要到最后 ，反过来想就是while i <= end and j<=end
### 2.用双指针进行做题，然会就是把小的加入，然会小的指针后移
### 3.先后移到终点的，我们就不能继续后移，而且把没有后移到终点的直接加上去即可



def MergeSort(arr,left,right):
    nums = []
    mid = (left+right)//2
    if left<right:
        #左边分治
        Larr = MergeSort(arr,left,mid)
        #右边分治
        Rarr = MergeSort(arr,mid+1,right)
        print('Larr',Larr)
        print('Rarr',Rarr)
        ## 接下来把左边和右边完成排序的数组进行归并
        ##这里得同时进行 必须and 为什么 因为两个数组不知道哪一个先到最后面，但是先到了最后面的，我们在里面进行把后面没到的直接加上去，就可以完成，所以这里只能用and
        while len(Larr)>0 and len(Rarr)>0:
            if Larr[0]>Rarr[0]:
                nums.append(Rarr.pop(0))
            else:
                nums.append(Larr.pop(0))
        nums+=Larr
        nums+=Rarr
        print('merge_nums',nums)
        return nums
    else:
        #返回单独的数组回去
        nums = []
        nums.append(arr[left])
        return nums

# arr1 = [6, 1, 2, 5, 4, 3, 9, 7, 10, 8,13,18,75,65,65,95,49,46,65,99,21]
# arr1 = [14,12,15,13,11,16]
import random

random.seed(54)
arr1 = [random.randint(0, 100) for _ in range(20)]
import time
begin = time.time()
print(len(arr1))
print(MergeSort(arr1,0,len(arr1)-1))
end = time.time()
print(end-begin)


# =====================================================/
# def merge_sort(arr):
#     """归并排序"""
#     if len(arr) == 1:
#         return arr
#     # 使用二分法将数列分两个
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#     # 使用递归运算
#     return marge(merge_sort(left), merge_sort(right))
#
#
# def marge(left, right):
#     """排序合并两个数列"""
#     result = []
#     # 两个数列都有值
#     while len(left) > 0 and len(right) > 0:
#         # 左右两个数列第一个最小放前面
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     # 只有一个数列中还有值，直接添加  数组可以直接添加
#     result += left
#     result += right
#     return result
#
# print(merge_sort([11, 99, 33 , 69, 77, 88, 55, 11, 33, 36,39, 66, 44, 22]))
# #



# def Merge_sort(arr):
#     if len(arr) == 1:
#         return arr
#     else:
#         mid = len(arr)//2
#         left = arr[:mid]
#         right = arr[mid:]
#         nums = Join(Merge_sort(left),Merge_sort(right))
#         return nums
# def Join(left,right):
#     nums = []
#     while len(left)>0 and len(right)>0:
#         if left[0]<=right[0]:
#             nums.append(left.pop(0))
#         elif left[0]>right[0]:
#             nums.append(right.pop(0))
#     nums+=left
#     nums+=right
#     return nums

# print(Merge_sort([11, 99, 33 , 69, 77, 88, 55, 11, 33, 36,39, 66, 44, 22]))

# 返回结果[11, 11, 22, 33, 33, 36, 39, 44, 55, 66, 69, 77, 88, 99]