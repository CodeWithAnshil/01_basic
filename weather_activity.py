# Weather Activity Suggestion

weather=input("Enter Today's weather : ")
def weather_activity(weather):
    if weather.lower()=="sunny":
         return "Go for Walk"
    elif weather.lower()=="rainy":
         return "Read a book"
    elif weather.lower()=="Snowy":
         return "Build a snowman"
    

print(weather_activity(weather))