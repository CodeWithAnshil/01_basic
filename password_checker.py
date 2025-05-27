password=input("Enter yout password :")

if len(password)<6:
    criteria ="Weak password"
elif len(password)<10:
     criteria="Medium password"
else:
      criteria="Strong password"

print(criteria)       