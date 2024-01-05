## 插入排序  就是对于未排序的数据，从已排序的数据中从后往前找到合适的位置插入
def insert_sort(arr):
    for pos in range(1,len(arr)):### pos 代表未排序的首个数字
        for j in range(pos-1,-1,-1):
            ## 后面的比前面的要大
            if arr[pos] < arr[j]:## 如果未排序的数不比当前数大
                arr[pos],arr[j] = arr[j],arr[pos]
                ##交换后pos 减一
                pos = pos-1
            else:
                print(f'第{i}次排序{arr}')
                break

unsorted_array = [64, 34, 25, 12, 22, 11, 90]
print('unsorted_array',unsorted_array)
insert_sort(unsorted_array)
print('sorted_array',unsorted_array)