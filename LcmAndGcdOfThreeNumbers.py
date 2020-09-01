from math import gcd
#Lcm and Gcd of Three Numbers

#input
x=int(input("Enter number 1 :"))
y=int(input("Enter number 2 :"))
z=int(input("Enter number 3 :"))

#logic starts
gcd1=gcd(x,y)
gcd2=gcd(gcd1,z)
lcm=y*z//gcd1
lcm2=x*lcm//gcd(x,lcm)

print("LCM is ",lcm2," and GCD is ",gcd2)