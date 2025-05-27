# Fruit Ripeness Classification
colour=input("Input your fruit colour: " )

def check_fruit(colur):
   if colour.lower()=="green":
       return "Unrip"
   elif colour.lower()=="yellow":
        return "Ripe"
   elif colour.lower()=="brown":
        return "Overripe"
   
print(f"Fruit rip condition {check_fruit(colour)}")