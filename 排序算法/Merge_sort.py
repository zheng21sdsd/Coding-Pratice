def Merge_sort(listA,listB):
    # 归并两个有序数组  把小的数组的第一个pop出去  判断哪一个最先pop完
    # # 1 3 5
    # # 2 4 6 8
    newlist = []
    while listA or listB:## A B 都不为空
        if listA and listB:  ## A B 都不为空
            if listA[0] < listB[0]:
                newlist.append(listA.pop(0))
            else:
                newlist.append(listB.pop(0))
        elif not listA:### A为空
            while listB:
                newlist.append(listB.pop(0))
        else:### B为空
            while listA:
                newlist.append(listB.pop(0))
    return newlist
## A B已排序好的
unsorted_array = [25,34,64]
unsorted_array1 = [11,12,22,90]
newlist = Merge_sort(unsorted_array,unsorted_array1)
print('sorted_array',newlist)






