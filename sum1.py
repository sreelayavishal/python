print("enter the number:")
n=int(input())
t=0
while(n>0):
    dig=n%10
    t=t+dig
    n=n//10
print("the sum of digits is",t)
