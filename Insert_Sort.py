### 假设前面都是排好的，你要把后面没排好的牌一个一个放到前面排好的牌上去
def insert_sort(arr):
    '''
    i 代表排好序列的指针
    j 代表还没拍好序列的指针
    给定一个数组，那么排好序列的指针促使之肯定为0好位置 未排好序列的指针肯定在1好位置
5 2 1 9 7 3
2 5 1 9 7 3 temp_i = -1  temp_j = 0
2 5 1 9 7 3 temp_i = 1   temp_j = 2
2 1 5 9 7 3 temp_i = 0   temp_j = 1
1 2 5 9 7 3 temp_i = -1  temp_j = 0
1 2 5 9 7 3 temp_i = 2   temp_j = 3

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
if __name__ == '__main__':
    import random
    import time
    random.seed(54)
    begin = time.time()
    arr1 = [random.randint(0, 100) for _ in range(20)]
    insert_sort(arr1)
    end = time.time()

    print(arr1)
    print(end-begin)
