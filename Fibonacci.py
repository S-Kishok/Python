num=int(input("Enter the num:"))
a=0
b=1
print(a,b,end=" ")
for i in range(2,num):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
print()

##while loop
num=int(input("Enter the num:"))
a=0
b=1
count=0
while(count<num):
    print(a,end=" ")
    a,b=b,a+b
    count+=1

