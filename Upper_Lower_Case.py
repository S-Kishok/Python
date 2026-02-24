str=input("Enter the input:")
result=("UPPERCASE",str.upper())
result2=("LOWERCASE",str.lower())
print(result,result2)

#without built in function
str = input("Enter a string: ")
result = ""

for ch in str:
    if 'a'<=ch<='z':
        result+=ch(ord(ch)-32)
    else:
        result+=ch

print("Uppercase:", result)

##Swapcase
str=input("Enter the input:")
print(str.swapcase())