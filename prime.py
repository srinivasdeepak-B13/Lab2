# Prime numbers upto a specified limit

# input
n= int(input("Enter n "))

# logic
for num in range(2, n+1):#numbers from 2 to n
    flag=0
    if num>1:
        for i in range(2, int((num/2)+1)):#checking num is prime or not
            if (num%i) == 0:
                flag=1
                break
    if flag==0:
        print(num,end=" ")#print if it is prime
            


    
