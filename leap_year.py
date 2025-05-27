# Calculate leap year 
x=input("Enter yaer ")
year=int(x)

if year%4==0 and year%100!=0:
   result="It is leap year"

elif year%400==0:
    result="It is leap year"

else:
     result="It is not leap year"

print(result)