# Program to Transpose a Sparse Matrix

# Function to represent the Sparse Matrix
def sparse_matrix(a):
    spa = []
    row = len(a) # Number of Rows
    col = len(a[0]) # Number of columns
    # Finding the non zero elements
    for i in range(row):
        for j in range(col):
            if a[i][j]!=0:
                spa.append([i,j,a[i][j]])
    return spa

# Function to transpose sparse matrix
def trans(a):
    res = []
    for i in a:
        res.append([i[1],i[0],i[2]])
    res.sort()
    return res


# Function to print martix
def print_matrix(a):
    if a==[]: print("Empty Matrix")
    for i in a:
        print(*i)

a = [] # Declaring the matrix

# Taking the matrix input
r = int(input("Enter the number of rows : "))
c = int(input("Enter the number of columns : "))
for i in range(r):
    d = list(map(int,input().split()))
    a.append(d)

print("The Original Matrix")
print_matrix(a)

print()

# Printing the sparse matrix
sp= sparse_matrix(a)
print("The Sparse Matrix")
print_matrix(sp)

# Printing the transpose of a sparse matrix
transpose = trans(sp)
print("The Transpose of the Sparse Matrix")
print_matrix(transpose)
