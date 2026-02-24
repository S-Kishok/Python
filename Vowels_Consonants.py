while True:
    ch=(input("Enter the character:")).lower()
    if(ch.isalpha() and len(ch)==1):
        break
    else:
        print("Enter a valid input")
        
if(ch in "aeiou"):
    print("Vowels")
else:
    print("Consonants")

