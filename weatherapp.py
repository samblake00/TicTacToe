from tkinter import *
import requests
import json
from datetime import datetime

root =Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Weather App - Made by Sam")

city_value = StringVar()

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def showWeather():
    #API key
    api_key = "4ad65c84c7d49136f777bfe69fc97c8d"
    city_name = city_value.get()
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
    response = requests.get(weather_url)
    weather_info = response.json()
    tfield.delete("1.0", "end")

    if weather_info['cod'] == 200:
        kelvin = 273
        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        #wind_speed = weather_info['sys']['wind']*3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\n Sunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"

    tfield.insert(INSERT, weather)

city_head = Label(root, text="Enter City Name", font ='Aerial 12 bold').pack(pady=10)

inp_city = Entry(root, textvariable=city_value, width=24, font='Aerial 14 bold').pack()

Button(root, command =showWeather, text="Check Weather", font='Aerial 10', bg='lightblue', fg='black', activebackground='teal', padx=5, pady=5).pack(pady=20)

weather_now = Label(root, text="The Weather is: ", font='arial 12 bold').pack(pady=10)

tfield = Text(root, width=46, height=10)
tfield.pack()

root.mainloop()