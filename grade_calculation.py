per=int(input("Enter your number:" ))

if per>=101:
    print("please enter a vailid percentage")
    exit()


def grade_cal(per):
   if per<60 :
     return "F"
   elif per<70:
       return "D"
   elif per<80:
      return "C"
   elif per<90:
       return "B"
   else:
       return "A"
   
print(grade_cal(per))