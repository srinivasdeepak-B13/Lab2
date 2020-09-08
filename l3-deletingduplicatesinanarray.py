#Deleting duplicates in array

#input of an array
l=list(map(int,input("Enter array ").split()))
#initialising new array to store elements without duplicate
s=[]

#logic for deleting duplicates
for i in l:
    if i not in s:
        s.append(i)
        
#output
print("New array is ")
print(*s,sep=" ")
