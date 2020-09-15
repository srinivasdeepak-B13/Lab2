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
a = [[0,1,0,0],[0,0,1,0],[1,0,0,0],[0,0,0,1]]
print("original matrix")
pmatrix(a)
sparse(a)

