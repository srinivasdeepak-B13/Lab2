#copying one array to another in reverse order

#input of an array
l=list(map(int,input("Enter array ").split()))

#intialising empty array with None
s=[None]*len(l)

#copying ane array to another logic using for loop in reverse order
for i in range(0,len(l)):
    s[i]=l[len(l)-i-1]

#output
print("New array is ")
print(*s,sep=" ")
