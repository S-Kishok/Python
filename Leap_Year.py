Year=int(input("Enter the year:"))
if(Year%400==0 or Year%4==0 and Year%100!=0):
    print(Year,"Is a leap year")
else:
    print(Year,"It's not a leap year")