###插入排序insert_sort
def insert_sort(arr):
    '''
    i 代表排好序列的指针
    j 代表还没拍好序列的指针
    给定一个数组，那么排好序列的指针初始值肯定为0好位置 未排好序列的指针肯定在1好位置
    :param arr:
    :return:
    '''
    i = 0
    j = 1
    tem_i = i
    tem_j = j
    while j<len(arr):
        if arr[tem_j]<arr[tem_i] and tem_i !=-1:
            arr[tem_i],arr[tem_j] =arr[tem_j],arr[tem_i]
            tem_i-=1
            tem_j-=1
        else:
            i = i+1
            j = j+1
            tem_i = i
            tem_j = j
########################################
###堆排序heap_sort
def build(arr,root,end):
    while True:
        child = 2*root+1
        if child >end:
            break
        if child+1<end and arr[child+1]>arr[child]:
            child+=1
            # 选出孩纸中的最大的一个
        if arr[root]<arr[child]:
            arr[root],arr[child] = arr[child],arr[root]
            root = child
            # 判断孩子和根节点的关系要保证根节点最大且子节点作为的根节点也是最大
        else:
            break
def heap_sort(arr):
    ## 最后一个**根节点**的位置是n//2-1 或者说 每个根节点都有类似于这个
    n = len(arr)
    last_root =  n // 2+1# 确认最深最后的那个根节点的位置
    for root in range(last_root,-1,-1):    # 由后向前遍历所有的根节点，建堆并进行调整
        build(arr,root,n-1)
    ### 最大堆已经够好了，就得每次把最大堆的堆顶元素和最后一个元素进行对调
    for end in range(n-1,0,-1):
        arr[0],arr[end] = arr[end],arr[0]#最大的到最后了
        build(arr,root,end-1)#最前面的堆进行排序 然会排除掉end
##############################################
###归并排序merge_sort
# def merge_sort(arr,left,right):
#     nums = []
#     mid = int((left+right)/2)
#     if left<right:
#         #左边分治
#         Larr = merge_sort(arr,left,mid)
#         #右边分治
#         Rarr = merge_sort(arr,mid+1,right)
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
#         print('merge_nums', nums)
#         return nums
#     else:
#         #返回单独的数组回去
#         nums = []
#         print(left)
#         nums.append(arr[left])
#         print(nums)
#         return nums
##############################################
###归并排序merge_sort
###归并排序
def merge_sort(arr):
    if len(arr) == 0:
        "万一数组为空"
        return
    """归并排序"""
    if len(arr) == 1:
        return arr
    # 使用二分法将数列分两个
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # 使用递归运算
    return marge(merge_sort(left), merge_sort(right))
def marge(left, right):
    """排序合并两个数列"""
    result = []
    # 两个数列都有值
    while len(left) > 0 and len(right) > 0:
        # 左右两个数列第一个最小放前面
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # 只有一个数列中还有值，直接添加  数组可以直接添加
    result += left
    result += right
    return result


##########################################
#####快速排序quick_sort


# def quick_sort(low,high,arr):
#     if low<high:
#         i = low
#         j = high
#         print('************************'*19)
#         while i != j:
#             while j>i and arr[j] >= arr[low]:###j>i 或者J!=i
#                 j = j - 1
#                 print('i = ', i, 'j = ', j)
#             while i != j and arr[i] <= arr[low]:
#                 i = i + 1
#             print('i11',i,'j111',j)
#             print('stop')
#             arr[i], arr[j] = arr[j], arr[i]
#         arr[i], arr[low] = arr[low], arr[i]
#         print(arr)
#         quick_sort(low, i-1,arr)
#         quick_sort(i+1,high,arr)
##########################################
####快速排序quick_sort
def quick_sort(data):
    """quick_sort"""
    if len(data) >= 2:
        mid = data[len(data)//2]
        left,right = [], []
        data.remove(mid)
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data

def Compare_Time(arr2,n):
    import time
    t_insert_sort = []
    t_heap_sort = []
    t_merge_sort = []
    t_quick_sort = []
    for needed_sort in arr2:
        ###插入排序时间
        begin = time.time()
        insert_sort(needed_sort)
        end = time.time()
        t_insert_sort.append(end-begin)
        ###堆排序时间
        begin = time.time()
        heap_sort(needed_sort)
        end = time.time()
        t_heap_sort.append(end - begin)
        # ###归并排序时间
        begin = time.time()
        merge_sort(needed_sort)
        end = time.time()
        t_merge_sort.append(end - begin)
        ###快速排序时间
        begin = time.time()
        # quick_sort(0,len(needed_sort)-1,needed_sort,)
        quick_sort(needed_sort)
        end = time.time()
        t_quick_sort.append(end - begin)
    x = n
    y1, y2, y3, y4 = t_insert_sort, t_heap_sort, t_merge_sort, t_quick_sort
    fig = plt.figure()
    plt.plot(x, y1, linestyle="-", label="insert_sort", color="blue")
    plt.legend(loc="upper left")  # 放置位置
    plt.plot(x, y2, linestyle="-", label="heap_sort", color="red")
    plt.legend(loc="upper left")  # 放置位置
    plt.plot(x, y3, linestyle='-', label='merge_sort',color = 'orange')
    plt.legend(loc="upper left")  # 放置位置
    plt.plot(x, y4, linestyle="-", label="quick_sort", color="green")
    plt.legend(loc="upper left")  # 放置位置
    plt.show()
if __name__ == '__main__':
    import random



    import numpy as np
    import matplotlib.pyplot as plt
    random.seed(54)
    ###问题规模为 n
    ###该规模时间为t
    ###各个排序的时间

    n = [i for i in range(0,200,10)]
    arr2 = []###arr2 :是不同的问题规模的数组
    ###scale 问题规模
    for scale in n:
        arr1 = [random.randint(0, 4000) for _ in range(scale)]
        # print(arr1)
        arr2.append(arr1)
    # print(arr2)
    Compare_Time(arr2,n)