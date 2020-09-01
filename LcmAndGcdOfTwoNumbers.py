#Lcm and Gcd of Two Numbers

#input
x=int(input("Enter number 1 :"))
y=int(input("Enter number 2 :"))

#logic starts
if x>y:
    greater=x
else:
    greater=y
while(True):
    if greater%x==0 and greater%y==0:
        lcm=greater
        break
    greater+=1
gcd=int(x*y/lcm)
print("LCM is ",lcm," and GCD is ",gcd)