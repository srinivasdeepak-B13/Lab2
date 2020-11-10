l=list(map(int,input().split()))
d=set(l)
m=min(d)
d.remove(m)
if len(d)==0:
    k=m
else:
    k=min(d)
if k==m:
    print("list doesn't have second smallest element")
else:
    print("Second smallest :",k)
        
    
