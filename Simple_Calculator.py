num1=float(input("Enter the number:"))
num2=float(input("Enter the number:"))

print("Select Operations:")
print(" + : Addition")
print(" - : Subtraction")
print(" * : Multiplication")
print(" / : Division")

op=input("Enter the operation:")

if(op=="+"):
    print("Result:",num1+num2)

elif(op=="-"):
    print("Result:",num1-num2)

elif(op=="*"):
    print("Result:",num1*num2)

elif(op=="/"):
    print("Result:",num1/num2)

else:
    print("Enter a valid input")