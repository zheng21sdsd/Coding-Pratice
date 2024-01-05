def bubble_sort(array):
    for i in range(len(array)):
        ### 一个元素bubble
        for j in range(len(array)-i):
            if j==len(array)-i-1:
                break
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                # temp = array[j + 1]
                # array[j+1] = array[j]
                # array[j] =temp
unsorted_array = [64, 34, 25, 12, 22, 11, 90]
print('unsorted_array',unsorted_array)
bubble_sort(unsorted_array)
print('sorted_array',unsorted_array)


