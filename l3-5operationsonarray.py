#4 operations on array

def copyfun(l):
    k=[]
    for i in l:
        k.append(i)
    return k

def removeduplicates(l):
    j=[]
    for i in l:
        if i not in j:
            j.append(i)
    return j

def deleteindex(l,n):
    g=[]
    for i in range(len(l)):
        if i is not n:
            g.append(l[i])
    return g
def searchelement(l,h):
    for i in range(0,len(l)):
        if l[i]==h:
            return i
def display(l):
    print(l)
    return

#Enter array
l=list(map(int,input().split()))

#Enter the operation you want to perform
k=int(input("Enter 1 copying ,2 for removing duplicates, 3 for deleting specific index,4 for searching an item, 5 for displaying array "))

if k==1:
    print("copied array is ",copyfun(l))
elif k==2:
    print("array after removing duplicates ",removeduplicates(l))
elif k==3:
    h=int(input("Enter index to delete"))
    print("Array after deleting index ",h,"is",deleteindex(l,h))
elif k==4:
    h=int(input("Enter element to search"))
    print("Elememt ",h,"found at index no.",searchelement(l,h))
else:
    display(l)
    
    
