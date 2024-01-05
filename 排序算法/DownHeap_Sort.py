
def build(arr,root,end):
    while True:
        child = 2*root+1 ## 表示根节点的左子节点
        if child>end:
            break
        if (child+1<=end) and (arr[child+1]>arr[child]):  ## 右节点最大
            child+=1  #指针 指向右节点
        if arr[child]>arr[root]:### 右节点比父亲节点都要大  最大堆  就是父亲比儿子要大
            arr[child],arr[root] =arr[root],arr[child]
            root = child
        else:
            break

def heap_sort(arr):
    n = len(arr)
    first_root = n//2 -1 # 确认最深最后的根节点位置
    for root in range(first_root,-1,-1):
        build(arr,root,n-1)
    for end in range(n-1,0,-1):
        arr[0],arr[end] = arr[end],arr[0]
        build(arr,0,end-1)


if __name__ == '__main__':
    import random

    random.seed(54)
    arr = [random.randint(0, 100) for _ in range(10)]
    print("原始数据：", arr)
    heap_sort(arr)
    print("堆排序结果：", arr)
