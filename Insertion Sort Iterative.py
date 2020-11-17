l=list(map(int,input().split()))
for i in range(1,len(l)):
    k=l[i]
    j=i-1
    while j>=0 and l[j]>k:
        l[j+1]=l[j]
        j-=1
    l[j+1]=k
print(l)
