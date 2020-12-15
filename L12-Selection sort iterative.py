l=list(map(int,input().split()))
for i in range(len(l)):
    min_i=i
    for j in range(i+1,len(l)):
        if l[j]<l[min_i]:
            min_i=j
    l[i],l[min_i]=l[min_i],l[i]
print(l)
