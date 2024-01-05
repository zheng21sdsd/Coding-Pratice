def quick_sorting(lst,h,r):#快排,h=head,r=rear
    if(r==h):
        return
    pivot=lst[h]
    p_big=h#找比基准大的数,big++
    p_sma=r#找比基准小的数,sma--
    while(p_sma>p_big):
        while(p_sma>=0 and lst[p_sma]<=pivot):
            p_sma-=1
            #print('p_sma',lst[p_sma])
        while(lst[p_big]>=pivot and p_big<len(lst)):
            p_sma-=1
        if p_big < len(lst) and p_sma >= 0:
            lst[p_big], lst[p_sma] = lst[p_sma], lst[p_big]
            #print(p_big,p_sma)
            #print(lst)
        if(p_big==len(lst)):
            lst[p_big-1], lst[p_sma] = lst[p_sma], lst[p_big-1]
        #lst[p_big],lst[p_sma]=lst[p_sma],lst[p_big]
        print('交换后',lst)

    #tem=lst[p_big]
    if(p_big==len(lst)):
        lst[p_big-1], lst[h] = pivot, lst[p_big-1]
    else:
        if (p_big==h+1 and lst[p_big]<lst[h]):
            lst[p_big],lst[h]=lst[h],lst[p_big]
        elif(p_big!=h+1):
            lst[p_big-1],lst[h]=pivot,lst[p_big-1]
        #print(p_big,h)
    #lst[h]=tem
    print('一次排序后',lst)
    return quick_sorting(lst,h,p_big-1),quick_sorting(lst,p_big+1,r)
if __name__ =='__main__':
    #lst=[0, 1, 3, 2, 4, 8]#???
    #lst=[1,2,3,4,0,8]
    #lst=[0,1,2,3,4,5,6]
    lst=[1,2,3,4,5,6]
    n=20
    b=[]
    # for i in range(n):
    #     a=[random.randint(0,100) for j in range(i)]
    #     b.append(a)
    # for i in b:
    #     print('前',i)
    #     quick_sorting(i,0,len(i)-1)
    #     print('排序后',i)
    i=[49, 52, 49, 12, 83]
    quick_sorting(i,0,len(i)-1)
    print(i)
