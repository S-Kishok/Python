# num=int(input("Enter the number:"))
# temp=num
# rev=0
# while(num>0):
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# if(rev==temp):
#     print("Panlindrome")
# else:
#     print("Not Panlindrome")
##String Method
num=input("Enter the number:")
if(num==num[::-1]):
    print("Panlindrome")
else:
    print("Not Panlindrome")
