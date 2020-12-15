#Minimum of three numbers

#input of three numbers

num1=int(input("Enter no. 1 "))
num2=int(input("Enter no. 2 "))
num3=int(input("Enter no. 3 "))

#logic begins

if num1<=num2 and num1<=num3:
    smallest=num1
elif num2<=num3:
    smallest=num2
else:
    smallest=num3

#output
print("smallest number is ",smallest)
