## 二分查找
### sorted_seq是排序好了的  没有排序好的  我们可以用sorted函数来实现
import random
def binary_sort(sorted_arr,val):
    low = 0
    high = len(sorted_arr)-1
    while low<high:
        ## 和区间中间比较
        mid = (low+high)//2
        if sorted_arr[mid] == val:
            return mid
        elif sorted_arr[mid]>val:
            high = mid-1
        else:
            low = mid+1



### 下面为调用
###https://docs.python.org/zh-cn/3.8//howto/sorting.html  sort和sorted函数
# list.sort 返回的是一个none  但是list改变了  sorted（list）  返回的是一个新的数组、、
sorted_array = [random.randint(1,100) for i in range(100)]
sorted_array.sort()
print(sorted_array)
target_value = 8
result = binary_sort(sorted_array,target_value)
if result != -1:
    print(f"目标值 {target_value} 在数组中的索引为 {result}")
else:
    print(f"目标值 {target_value} 不在数组中")
### list sort sorted都有一个形参  key 来指定在进行比较之前 在每列元素上进行调用的函数
# print("This is a test string from Andrew".split())
# print(sorted("This is a test string from Andrew".split(), key=str.lower))### 在split之后  在比较之前  每列元素都得调用str.lower函数  然后在进行排序
