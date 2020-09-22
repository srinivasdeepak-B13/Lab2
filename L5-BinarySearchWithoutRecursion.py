#Binary Search without recursion
def BinarySearch(a,search):
    low=0
    high=len(a)-1
    if high>=low:
        mid=(low+high)//2
        if search==a[mid]:
            return mid
        elif a[mid]>search:
            for i in range(0,mid):
                if a[i]==search:
                    return i
        else:
            for i in range(mid+1,high+1):
                if a[i]==search:
                    return i
    else:
        return None
l=list(map(int,input("Enter array ").split()))
find=int(input("Enter element to find "))
pos=BinarySearch(l,find)
if pos==None:
    print("element not found")
else:
    print("Element",find,"found at",pos,"index")
