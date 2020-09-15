#original array
a = [[0,1,0,0],[0,0,1,0],[1,0,0,0],[0,0,0,1]]
print("original matrix")
for i in range(4):
    for j in range(4):
	print(a[i][j])
#print sparse
s = []
for i in range(4):
    for j in range(c):
        temp = []
        if a[i][j]!=0:
	    temp.append(i)
	    temp.append(j)
	    temp.append(a[i][j])
	    s.append(temp)		
print("sparse matrix")
for i in range(len(s)):
    for j in range(len(s[i])):
	print(s[i][j],end='')
