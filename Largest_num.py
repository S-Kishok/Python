''''
num1=int(input("Enetr a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))

if(num1>num2 and num1>num3):
    print("Num 1 is the largest number")
elif(num2>num1 and num2>num3):
    print("Num 2 is the largest number")
else:
    print("Num 3 is the largest numebr")
    '''

#using max 
''''

num1=int(input("Enetr a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))
Largest=max(num1,num2,num3)
print("the largest number is:",Largest)
'''

#using dictionary
num1=int(input("Enetr a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))

numbers={
    "num1":num1,
    "num2":num2,
    "num3":num3
}
largest_var=max(numbers,key=numbers.get)
print(largest_var,"is the largest value")