#Binary Search in a Array
def BinarySearch(a,low,high,search):
    if high>=low:
        mid=(low+high)//2
        if a[mid]==search:
            return mid
        elif a[mid]>search:
            return BinarySearch(a,low,mid-1,search)
        else:
            return BinarySearch(a,mid+1,high,search)    
    else:
        return -1
arr=[1,2,3,4,5,6,7,8,9,10]
find=9
pos=BinarySearch(arr,0,len(arr)-1,find)
if pos==-1:
    print("element not found")
else:
    print("Element",find,"found at",pos,"index")
    
