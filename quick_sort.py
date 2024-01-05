
def quick_sort(low,high,arr):
    '''
    5 2 1 9 7 3
    j的索引值指代3
    i 指代9
    比较一次可以对一个数进行调整成正确位置
    右边找到第一个比基准左边大的
    左边找到第一个比基准小的
    进行交换
    然后继续如此
    知道指针碰撞
    完成一个位置的正确
    :param low:
    :param high:x`
    :param arr:
    :return:
    '''
    if low<high:
        i = low
        j = high
        print('************************'*19)
        while i != j:
            while j>i and arr[j] >= arr[low]:###j>i 或者J!=i
                j = j - 1
                print('i = ', i, 'j = ', j)
            while i != j and arr[i] <= arr[low]:
                i = i + 1
            print('i11',i,'j111',j)
            print('stop')
            arr[i], arr[j] = arr[j], arr[i]
        arr[i], arr[low] = arr[low], arr[i]
        print(arr)
        quick_sort(low, i-1,arr)
        quick_sort(i+1,high,arr)








# arr1 = [6, 1, 2, 5, 4, 3, 9, 7, 10, 8,13,18,75,65,65,95,49,46,65,99,21]
import time
import random

random.seed(54)
arr1 = [random.randint(0, 1000) for _ in range(5000)]
begin = time.time()
quick_sort(0,len(arr1)-1,arr1)
end = time.time()
print(f'start:{begin}  end_time:{end}')
print(end-begin)
print(input())
#


