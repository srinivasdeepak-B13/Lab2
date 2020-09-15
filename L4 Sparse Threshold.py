def sparse(a):
	s = []
	for i in range(len(a)):
	    for j in range(len(a[i])):
	        temp = []
	        if a[i][j]!=0:
		    temp.append(i)
		    temp.append(j)
		    temp.append(a[i][j])
		    s.append(temp)		
	#print sparse
	print("sparse matrix")
	pmatrix(s)

def pmatrix(s):
	for i in range(len(s)):
	    for j in range(len(s[i])):
		print(s[i][j],end='')
#original array
a = []
row = int(input("enter number of rows"))
col = int(input("enter number of columns"))
thres = int(input("enter threshold value"))
for i in range(row):
    for j in range(col):
    	k = int(input())
        if k<=thres:
            a[i][j]=0
        else:
        	a[i][j]=k
print("original matrix")
pmatrix(a)
sparse(a)
