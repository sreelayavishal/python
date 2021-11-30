print("enter the num: ")
n=int(input())
r=0
while(n>0):
    dig=n%10
    r=r+dig
    n=n//10
print("the sum of digits is",r)
    
