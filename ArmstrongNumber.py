#Armstrong number

#input
n=int(input("Enter number: "))
temp=n
temp2=n #storing n in a temporary variable as value of n changes
sum1=0
sum2=0

#logic
while n>0:
    sum1=sum1+1  
    n=n//10     
while temp>0:
    x=temp%10
    sum2=sum2+(x**sum1)
    temp=temp//10
if temp2==sum2:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
#output


