str1=input("Enter the input:").upper()
str2=input("Enter the input:").upper()

if sorted(str1)==sorted(str2):
    print("It is Anagram")
else:
    print("Its Not Anogram")