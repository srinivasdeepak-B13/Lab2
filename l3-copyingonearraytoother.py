#copying one array to another

#input of an array
l=list(map(int,input("Enter array ").split()))

#intialising empty array
s=[]

#copying ane array to another logic using for loop
for i in range(0,len(l)):
    s.append(l[i])

#output
print("New array is ")
print(*s,sep=" ")
