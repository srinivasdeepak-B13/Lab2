#Linear Search Implementation
a=[1,2,3,4,5,6,7,8,9,10]
find=7
pos=-1
def linearsearch(a,search):
    for i in range(len(a)):
        if a[i]==find:
            return i
pos=linearsearch(a,find)
if pos==-1:
    print("Element Not Found")
else:
    print(find,"found at",pos,"index")
    
