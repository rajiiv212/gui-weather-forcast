# python3 -- Weather Application using API

# importing the libraries
from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk, Image


# necessary details
root = Tk()
root.title("Weather Forcasting")
root.geometry("350x500")
root['background'] = "#ddd"

# Image
new = ImageTk.PhotoImage(Image.open('logo.jpg'))
panel = Label(root, image=new)
panel.place(x=0, y=420)


# Dates
dt = datetime.datetime.now()
date = Label(root, text=dt.strftime('%A--'), bg='white', font=("bold", 12))
date.place(x=5, y=130)
month = Label(root, text=dt.strftime('%m %B'), bg='white', font=("bold", 12))
month.place(x=100, y=130)

# Time
hour = Label(root, text=dt.strftime('%I : %M %p'),
			bg='white', font=("bold", 12))
hour.place(x=10, y=160)

# Theme for the respective time the application is used
if int((dt.strftime('%I'))) >= 8 & int((dt.strftime('%I'))) <= 5:
	img = ImageTk.PhotoImage(Image.open('sun.jpg'))
	panel = Label(root, image=img)
	panel.place(x=140, y=170)
else:
	img = ImageTk.PhotoImage(Image.open('moon.jpg'))
	panel = Label(root, image=img)
	panel.place(x=120, y=170)


# City Search
city_name = StringVar()
city_entry = Entry(root, textvariable=city_name,font=("bold", 12), width=27)
city_entry.grid(row=1, column=0, ipady=10, stick=W+E+N+S)
api_key="42cd6963072b6d7f9b2a3197b320a7a6"


def city_name():

	# API Call
	api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
							+ city_entry.get() + "&units=metric&appid="+api_key)

	api = json.loads(api_request.content)

	# Temperatures
	apil=api_request.json()

	if apil["cod"] != "404":
 
	    # store the value of "main"
	    # key in variable y
	    y = apil["main"]
	    current_temprature = y['temp']
	    humidity = y['humidity']
	    tempmin = y['temp_min']
	    tempmax = y['temp_max']
	    # store the value corresponding
	    # to the "pressure" key of y
	    current_pressure = y["pressure"]
	    # Coordinate
	    x = apil['coord']
	    longtitude = x['lon']
	    latitude = x['lat']
	    # Country
	    so = apil['sys']
	    country = so['country']
	    citi = apil['name']

	    current_humidity = y["humidity"]

	    z = apil["weather"]

	    weather_description = z[0]["description"]


    #**************************************************
	# Adding the received info into the screen
	lable_temp.configure(text=current_temprature)
	lable_humidity.configure(text=current_humidity)
	max_temp.configure(text=tempmax)
	min_temp.configure(text=tempmin)
	lable_lon.configure(text=longtitude)
	lable_lat.configure(text=latitude)
	lable_country.configure(text=country)
	lable_citi.configure(text=citi)


# Search Bar and Button
city_nameButton = Button(root, text="Search", command=city_name, font=("bold", 15))
city_nameButton.grid(row=1, column=1, padx=5, stick=W+E+N+S)


# Country Names and Coordinates
lable_citi = Label(root, text="...", width=0,
				bg='white', font=("bold", 12))
lable_citi.place(x=10, y=63)

lable_country = Label(root, text="...", width=0,
					bg='white', font=("bold", 12))
lable_country.place(x=135, y=63)

lable_lon = Label(root, text="...", width=0,
				bg='white', font=("Helvetica", 12))
lable_lon.place(x=25, y=95)
lable_lat = Label(root, text="...", width=0,
				bg='white', font=("Helvetica", 12))
lable_lat.place(x=105, y=95)

# Current Temperature

lable_temp = Label(root, text="...",fg="#f055fa", width=0, bg='white',
				font=("Helvetica", 45))
lable_temp.place(x=18, y=220)

# Other temperature details

humi = Label(root, text="Humidity: ", width=0,
			bg='white', font=("bold", 12))
humi.place(x=3, y=350)

lable_humidity = Label(root, text="...", width=0,
					bg='white', font=("bold", 12))
lable_humidity.place(x=107, y=350)


maxi = Label(root, text="Max. Temp.: ", width=0,
			bg='white', font=("bold", 12))
maxi.place(x=3, y=370)

max_temp = Label(root, text="...", width=0,
				bg='white', font=("bold", 12))
max_temp.place(x=128, y=370)


mini = Label(root, text="Min. Temp.: ", width=0,
			bg='white', font=("bold", 12))
mini.place(x=3, y=390)

min_temp = Label(root, text="...", width=0,
				bg='white', font=("bold", 12))
min_temp.place(x=128, y=390)


# Note
note = Label(root, text="All temperatures in degree celsius",
			bg='white', font=("italic", 8))
note.place(x=95, y=410)


root.mainloop()
