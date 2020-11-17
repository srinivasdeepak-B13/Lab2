def mergesort(ar):
    k=len(ar)
    if k<2:
        return ar
    mid=k//2
    l=mergesort(ar[:mid])
    r=mergesort(ar[mid:])
    i=0
    j=0
    k=0
    while i<len(l) and j<len(r):
        if l[i]<=r[i]:
            ar[k]=l[i]
            i+=1
            k+=1
        else:
            ar[k]=r[j]
            j+=1
            k+=1
    while i<len(l):
        ar[k]=l[i]
        i+=1
        k+=1
    while j<len(r):
        ar[k]=r[j]
        j+=1
        k+=1
    return ar
f=list(map(int,input().split()))
print(mergesort(f))
