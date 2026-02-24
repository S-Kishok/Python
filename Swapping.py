#with third variable
'''
a=int(input("enter the number"))
b=int(input("enter the number"))
print(a,b)
temp=a
a=b
b=temp
print(a,b)
'''
#without third variable
a=int(input("enter the number"))
b=int(input("enter the number"))
print("before swap:",a,b)
a,b=b,a
print("after swap",a,b)



