#perfect number

#input
x=int(input(" Please Enter any Number: "))
sum= 0

#logic
for i in range(1, x):
    if(x % i == 0):
        sum = sum + i
if (sum == x):
    print("Perfect Number")
else:
    print("Not a Perfect Number")
