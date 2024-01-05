
# 一般用数组来表示堆，下标为 i 的结点的父结点下标为(i-1)/2；其左右子结点分别为 (2i + 1)、(2i + 2)
def build(arr, root, end):
    while True:
        child = 2 * root + 1  # 左子节点的位置
        if child > end:  # 若左子节点超过了最后一个节点，则终止循环
            break
        if (child + 1 <= end) and (arr[child + 1] > arr[child]):  # 若右子节点在最后一个节点之前，并且右子节点比左子节点大，则我们的孩子指针移到右子节点上
            child += 1
        if arr[child] > arr[root]:  # 若最大的孩子节点大于根节点，则交换两者顺序，并且将根节点指针，移到这个孩子节点上
            arr[child], arr[root] = arr[root], arr[child]
            root = child
        else:
            break

def heap_sort(arr):
    n = len(arr)
    first_root = n // 2 - 1  # 确认最深最后的那个根节点的位置
    for root in range(first_root, -1, -1):  # 由后向前遍历所有的根节点，建堆并进行调整
        # print(root)
        build(arr, root, n - 1)

    for end in range(n - 1, 0, -1):  # 调整完成后，将堆顶的根节点与堆内最后一个元素调换位置，此时为数组中最大的元素，然后重新调整堆，将最大的元素冒到堆顶。依次重复上述操作
        arr[0], arr[end] = arr[end], arr[0]
        build(arr, 0, end - 1)


# 测试数据
if __name__ == '__main__':
    import random

    random.seed(54)
    arr = [random.randint(0, 100) for _ in range(10)]
    print("原始数据：", arr)
    heap_sort(arr)
    print("堆排序结果：", arr)

# 输出结果

# 原始数据： [17, 56, 71, 38, 61, 62, 48, 28, 57, 42]
# 堆排序结果： [17, 28, 38, 42, 48, 56, 57, 61, 62, 71]


















# ****===================================================================***
def build(arr,root,end):
    while True:
        child = 2*root+1
        ##当到底了前面的节点后 子节点可以作为根节点了 就得while 来确保作为根节点的子节点也满足最大堆序
        if child >end:
            break # 孩子超过了最后一个节点
        if child+1<end and arr[child+1]>arr[child]:
            child+=1
            # 选出孩纸中的最大的一个
        if arr[root]<arr[child]:
            arr[root],arr[child] = arr[child],arr[root]
            root = child
            # 判断孩子和根节点的关系要保证根节点最大且子节点作为的根节点也是最大
        else:
            break




 # 左子节点的位置
       # ，则终止循环

        # 若右子节点在最后一个节点之前，并且右子节点比左子节点大，则我们的孩子指针移到右子节点上

        # 若最大的孩子节点大于根节点，则交换两者顺序，并且将根节点指针，移到这个孩子节点上



def heap_sort(arr):
    ## 最后一个**根节点**的位置是n//2-1 或者说 每个根节点都有类似于这个
    n = len(arr)
    last_root =  n // 2+1# 确认最深最后的那个根节点的位置
    for root in range(last_root,-1,-1):    # 由后向前遍历所有的根节点，建堆并进行调整
        build(arr,root,n-1)
    ### 最大堆已经够好了，就得每次把最大堆的堆顶元素和最后一个元素进行对调
    # for root in range(len(arr)):
    #     arr[root],arr[n] = arr[n],arr[root]
    for end in range(n-1,0,-1):
        arr[0],arr[end] = arr[end],arr[0]#最大的到最后了
        build(arr,root,end-1)#最前面的堆进行排序 然会排除掉end




  # 调整完成后，将堆顶的根节点与堆内最后一个元素调换位置，此时为数组中最大的元素，然后重新调整堆，将最大的元素冒到堆顶。依次重复上述操作




# 测试数据
if __name__ == '__main__':
    import random
    import time
    random.seed(54)
    arr = [random.randint(0, 100) for _ in range(20)]
    print("原始数据：", arr)
    begin = time.time()
    heap_sort(arr)
    end = time.time()
    print("堆排序结果：", arr)
    print(end-begin)

# 输出结果


# 原始数据： [17, 56, 71, 38, 61, 62, 48, 28, 57, 42]
# 堆排序结果： [17, 28, 38, 42, 48, 56, 57, 61, 62, 71]