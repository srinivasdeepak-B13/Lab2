#Sum of digits of a number

#input
n=int(input("Enter number: "))
temp=n   #storing n in a temporary variable as value of n changes
sum=0

#logic
while n>0:
    x=n%10    #finding last digit of the number
    sum=sum+x  #adding the number to the sum
    n=n//10     #updating the number by dividing it with 10 to find next digit


#output
print("sum of the digits in ",temp," is ",sum)

