#Age Group Classification
def age_group_classification(age):
   if age<13:
       return "Child"

   elif age>=13 and age<=19:
        return "Teenager"
   elif age>20 and age<=59:
        return "Adult"
   elif age>=60:
        return "Senior"
   
print(age_group_classification(13))