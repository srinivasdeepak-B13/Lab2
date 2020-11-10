ar=list(map(int,input().split()))
def QuickSort(l):
    k=len(l)
    if k<2:
        return l
    cur=0
    for i in range(1,k):
        if l[i]<=l[0]:
            cur+=1
            l[cur],l[i]=l[i],l[cur]
    l[0],l[cur]=l[cur],l[0]
    left=QuickSort(l[0:cur])
    right=QuickSort(l[cur+1:])
    return left+[l[cur]]+right
print("Sorted array is ",QuickSort(ar))
            
