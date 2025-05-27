distance=int(input("Enter yout transportaion distance :"))

def transport(distance):
   if distance<3:
       return "Walk"
   elif distance<=15:
      return "Bike"
   elif distance>15:
      return "Car"
   
print(transport(distance))