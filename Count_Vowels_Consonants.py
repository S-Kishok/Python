str=input("Enter the string:")
v=0
c=0
for ch in str:
    if ch.isalpha:
        if ch in "aeiou":
            v+=1
        else:
            c+=1
print("Vowels=",v)
print("Consonants=",c)