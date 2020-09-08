#searching for an element in an array by calling function

#search function
def search(n,l):
    for i in range(0,len(l)):
        if l[i]==n:
            return i
        


#input an array
l=list(map(int,input("Enter array ").split()))

#input of an element to find
n=int(input("Enter element to find "))

#logic
x=search(n,l)
#output
print("Element ",n,"found at index no.",x)
