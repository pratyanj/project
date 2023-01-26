from tkinter import *
from tkinter import ttk
import requests

# city_name= "gujarat"
# API_key="41889632c46a39f18be10a12d4873741"
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
# info=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}",headers=headers).json()
# print(info)

weather=Tk()
weather.title("pratyanj weather apk")
weather.geometry("400x400")
weather.config(bg="lightblue")

name = Label(weather,text="Todays Weather",background="#58c0ed",font=("Time New Roman",15,"bold"),borderwidth=2,relief=SOLID)
name.place(x=50,y=30,width=300,height=35)

name_of_city=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
city_name=ttk.Combobox(weather,values=name_of_city,background="#58c0ed",font=("Time New Roman",10,),justify=CENTER,)
city_name.place(x=90,y=70,width=200,height=25)

# Button_main
Button_main = Button(weather,text="Enter",borderwidth=2,relief=SOLID,)
Button_main.place(x=170,y=100,height=30,width=50)

# weather_climate
weather_climate = Label(weather,text="weather climate :-",background="lightblue",font=("Time New Roman",10,"bold"),justify=LEFT)
weather_climate.place(x=40,y=170,width=140,height=30)
weather_climate1 = Label(weather,text="",background="black",font=("Time New Roman",10,"bold"),justify=LEFT)
weather_climate1.place(x=200,y=170,width=140,height=30)

# Temperature
Temperature = Label(weather,text="Temperature :-",background="lightblue",font=("Time New Roman",10,"bold"),justify=LEFT)
Temperature.place(x=40,y=200,width=120,height=30)
Temperature1 = Label(weather,text="",background="lightblue",font=("Time New Roman",10,"bold"),justify=LEFT)
Temperature1.place(x=200,y=200,width=120,height=30)

# Humidity
Humidity= Label(weather,text="Humidity :-",background="lightblue",font=("Time New Roman",10,"bold"),justify=LEFT)
Humidity.place(x=40,y=230,width=90,height=30)
Humidity1= Label(weather,text="Humidity :-",background="lightblue",font=("Time New Roman",10,"bold"),justify=LEFT)
Humidity1.place(x=200,y=230,width=90,height=30)

# Wind_pressure
Wind_pressure =Label(weather,text="Wind pressure :-",background="lightblue",font=("Time New Roman",10,"bold"),justify=LEFT)
Wind_pressure.place(x=40,y=260,width=130,height=30)
Wind_pressure1 =Label(weather,text="Wind pressure :-",background="lightblue",font=("Time New Roman",10,"bold"),justify=LEFT)
Wind_pressure1.place(x=200,y=260,width=130,height=30)

mainloop()