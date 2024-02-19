import tkinter as tk
from PIL import Image, ImageTk
import requests
import pyperclip
from io import BytesIO

# Function to fetch weather data from the API
def get_weather(city):
    api_key = "d00c29a2bfb24a9382793935241902"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()
    return data

# GUI pour infos méteo
def show_weather():
    city = entry.get()
    weather_data = get_weather(city)

    # API params
    location = weather_data['location']['name'] + ', ' + weather_data['location']['region'] + ', ' + weather_data['location']['country']
    local_time = weather_data['location']['localtime']
    temperature = weather_data['current']['temp_c']
    condition = weather_data['current']['condition']['text']
    wind_speed = weather_data['current']['wind_kph']
    wind_direction = weather_data['current']['wind_dir']
    humidity = weather_data['current']['humidity']
    cloud_cover = weather_data['current']['cloud']
    pressure = weather_data['current']['pressure_mb']
    visibility = weather_data['current']['vis_km']

    # Les labels
    location_label.config(text=f"Informations Météo pour : {location}", font=("Arial", 14, "bold"), fg="navy")
    local_time_label.config(text=f"Date : {local_time}", font=("Arial", 12), fg="navy")
    temperature_label.config(text=f"Température : {temperature}°C", font=("Arial", 12), fg="navy")
    condition_label.config(text=f"Condition : {condition}", font=("Arial", 12), fg="navy")
    wind_speed_label.config(text=f"Vitesse du vent : {wind_speed} km/h", font=("Arial", 12), fg="navy")
    wind_direction_label.config(text=f"Direction du vent : {wind_direction}", font=("Arial", 12), fg="navy")
    humidity_label.config(text=f"Humidité : {humidity}%", font=("Arial", 12), fg="navy")
    cloud_cover_label.config(text=f"Nuages : {cloud_cover}%", font=("Arial", 12), fg="navy")
    pressure_label.config(text=f"Pression : {pressure} mb", font=("Arial", 12), fg="navy")
    visibility_label.config(text=f"Visibilité : {visibility} km", font=("Arial", 12), fg="navy")

    # API image
    local_image_path = "Soulayman_Free_API.png"
    local_image = Image.open(local_image_path)
    local_image = local_image.resize((700, 300))
    local_photo = ImageTk.PhotoImage(local_image)
    local_image_label.config(image=local_photo)
    local_image_label.image = local_photo

window = tk.Tk()
window.title("Weather Information")
window.configure(bg="lightblue")

# GUI par TKinter
entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=10)

button = tk.Button(window, text="Get Weather", command=show_weather, font=("Arial", 12), bg="navy", fg="white")
button.pack(pady=5)

location_label = tk.Label(window, font=("Arial", 14, "bold"), fg="navy", bg="lightblue")
location_label.pack()

local_time_label = tk.Label(window, font=("Arial", 12), fg="navy", bg="lightblue")
local_time_label.pack()

temperature_label = tk.Label(window, font=("Arial", 12), fg="navy", bg="lightblue")
temperature_label.pack()

condition_label = tk.Label(window, font=("Arial", 12), fg="navy", bg="lightblue")
condition_label.pack()

wind_speed_label = tk.Label(window, font=("Arial", 12), fg="navy", bg="lightblue")
wind_speed_label.pack()

wind_direction_label = tk.Label(window, font=("Arial", 12), fg="navy", bg="lightblue")
wind_direction_label.pack()

humidity_label = tk.Label(window, font=("Arial", 12), fg="navy", bg="lightblue")
humidity_label.pack()

cloud_cover_label = tk.Label(window, font=("Arial", 12), fg="navy", bg="lightblue")
cloud_cover_label.pack()

pressure_label = tk.Label(window, font=("Arial", 12), fg="navy", bg="lightblue")
pressure_label.pack()

visibility_label = tk.Label(window, font=("Arial", 12), fg="navy", bg="lightblue")
visibility_label.pack()

# Label pour api expiration date
expiration_label = tk.Label(window, text="Free API Link && expiration date: 2024/mars/04\n", font=("Arial", 14, "bold"), fg="navy")
expiration_label.pack()
expiration_label = tk.Label(window, text="Web Site : https:///www.weatherapi.com/", font=("Arial", 14, "bold"), fg="navy")
expiration_label.pack()
# copier API vers Clipboard
def copy_api_key():
    api_key = "d00c29a2bfb24a9382793935241902"
    pyperclip.copy(api_key)

# copy button
copy_button = tk.Button(window, text="Copier le API Key", command=copy_api_key, font=("Arial", 12), bg="navy", fg="white")
copy_button.pack(pady=5)

# Label d'image
local_image_label = tk.Label(window, bg="lightblue")
local_image_label.pack()

window.mainloop()
