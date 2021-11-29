print("enter the string")
s=input()
a=s[0]
b=s[1:]
snew=b.replace(a,"$")
snew=a+snew
print(snew)
