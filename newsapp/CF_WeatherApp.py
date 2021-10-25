from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import requests

bluee = '#0066CC'

class WeatherApp:
    global url,apiKey
    apiKey = 'c3a9e9bc64cb8adb63e677acfe719a2d'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    
    
    def __init__(self,root):
        self.root = root
        self.root.title("CheckWeather") 
        self.root.geometry('380x460+550+150')
        self.root['bg']='red'
        # self.txt = Label(text='CheckWeather - by CF',font=('rockwell bold',16),bg='red',fg='white')
        # self.txt.pack(pady=20)
        
        
        cityText = StringVar()
        cityEntry = ttk.Entry(root,text=cityText,width=20,font=('arial bold',30),style='EntryStyle.TEntry',justify='center')
        cityEntry.pack(pady=0)
        cityEntry.focus()
     
        
        def check_weather(city):
            result = requests.get(url.format(city,apiKey))
            if result:
                json = result.json()
                # (City, Country, temp_Celsius, temp_fahrenheit, icon, weather)
                city = json['name'] #0
                country = json['sys']['country'] #1
                temp_kelvin = json['main']['temp'] 
                temp_Celsius = temp_kelvin - 273.15 #2
                temp_fahrenheit = temp_Celsius*(9/5)+32 #3
                icon = json['weather'][0]['icon'] #4
                weather = json['weather'][0]['main'] #5
                final = (city,country,temp_Celsius,temp_fahrenheit,icon,weather)       
                return final
            else:
                return None
        
        
        def searched_for(root):
            city = cityText.get()
            weather = check_weather(city)
            if weather:
                locationLabel['text'] = f"{weather[0]}, {weather[1]}"
                img["file"] = f'img\\{weather[4]}.png'
                temperatureLabel['text'] = f"{weather[2]:.2f} °C, {weather[3]:.2f} °F"
                weatherLabel['text'] = f"{weather[5]}"
                introLabel.destroy()
            else:
                messagebox.showerror('ERROR',f"'Couldn't find the city name '{city}' :(")
            print(f'Searched for: {city}')
        
        
        
        def press():
            introLabel.destroy()
            searched_for(root)
        
        
        
        searchButton = Button(root,text='Press Enter ↵\n/\nSearchWeather',font=('rockwell bold',16),width=20,height=4,bg=bluee,fg='white',command=press)
        searchButton.pack(pady=20)
        
        cityEntry.bind('<Return>',searched_for)
        
        locationLabel = Label(root,text='',bg='red',fg='white',font=('rockwell bold',30))
        locationLabel.pack()
        
        introLabel = Label(root,text='Search by - City/State/Country',font=('rockwell bold',16),bg='red',fg='white')
        introLabel.pack()
        
        img = PhotoImage(file='')
        image = Label(root,image=img,bg='red',fg='white')
        image.pack()
        
        temperatureLabel = Label(root,text='',font=('rockwell bold',21),bg='red',fg='white')
        temperatureLabel.pack()
        
        
        weatherLabel = Label(root,text='',font=('rockwell bold',21),bg='red',fg='white')
        weatherLabel.pack()
        
        

    def startWeather():
        root = Toplevel()
        WeatherApp(root)
        # root.state('zoomed')
        root.mainloop()