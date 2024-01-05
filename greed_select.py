def Compare(a, b):
    if str(a)+str(b)>str(b)+str(a):
        return False
    return True
def G_S(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1,i,-1):
            if Compare(arr[j-1],arr[j]):
                arr[j-1],arr[j] = arr[j],arr[j-1]


    for k in range(len(arr)):
        print(arr[k],end = '')
arr = [13,312,343]
G_S(arr)