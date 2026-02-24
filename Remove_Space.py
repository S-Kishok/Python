str=input("Enter input:")
result=(str.replace(" ",""))
print(result)

##without Built In function
str=input("Enter the number:")
result=" "

for ch in str:
    if ch!=" ":
        result+=ch
print(result)