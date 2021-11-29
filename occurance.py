n=int(input("enter the number of names:"))
list=[]
count=0
for i in range(n):
    name=input("enter name:")
    list.append(name)
for i in list:
    for j in i:
        if(j=="a"):
            count=count+1;
print(count)            
