#concatenate multiple arrays

#Taking input of three arrays
l=list(map(int,input("Enter array 1 ").split()))
m=list(map(int,input("Enter array 2 ").split()))
n=list(map(int,input("Enter array 3 ").split()))

#concatenating two arrays l amd m using for loop

for i in m:
    l.append(i)

print("concatenation of l and m is ",l)

#concatenating two arrays using + and storing it in j it displays all the elements

j=l+n
print("concatenation of l and n is :",j)

