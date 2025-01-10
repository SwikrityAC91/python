import requests
import pyttsx3

city= input("enter the name of the city")
API_key='b84cd39991710b84517c5afc41c0830d'
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"
response=requests.get(url)
#if(response.status_code==200):
data=response.json()
#print(data['weather'])
w=(data['main']['temp'])
x=(data['main']['feels_like'])

#print(w)
    #print(" current temperature is ",data['main']['temp'])

engine=pyttsx3.init()
engine.say(f"current temperature in{city} is{w}")
engine.say(f"feels like temperature in{city} is{x}")
engine.runAndWait()


