
import pyttsx3  # text to speech
import speech_recognition as sr  # speech to text
import datetime
import webbrowser   # opens websites via google
import os
import random
import requests
import psutil     # For Battery Health
import ctypes   # Calling windows function (log off, shut down)
import subprocess   # commands like shutdown,ping,ls
import platform    # gets system info.


# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change index if needed

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello Imaad Mahmood , I am Jarvis, your personal assistant. Please tell me how may I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 3000  # Adjust sensitivity
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


# Weather Update Function
def get_weather(city="Bahawalpur"):
    api_key = "47f5042f9812fe43a495b8daaf14ab5e"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == 200:
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temp = main["temp"]
        humidity = main["humidity"]
        speak(f"The temperature in {city} is {temp}°C with {weather_desc}. The humidity is {humidity}%.")
    else:
        speak("Sorry, I couldn't fetch the weather data.")


# List of random facts
facts = [
    "Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old and still edible.",
    "Bananas are berries, but strawberries are not.",
    "A day on Venus is longer than a year on Venus.",
    "The Eiffel Tower can grow more than 6 inches taller during the summer.",
    "Cleopatra lived closer in time to the moon landing than to the building of the Great Pyramid of Giza."
]


# List of inspirational quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer"
]


# Battery Status

def check_battery_status():
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        speak(f"The battery is at {percent}%")
    else:
        speak("Battery status is not available.")


# Function to increase the volume
def increase_volume():
    volume = engine.getProperty('volume')  # Get the current volume
    if volume < 1.0:  # Maximum volume is 1.0
        engine.setProperty('volume', volume + 0.1)  # Increase volume by 0.1
        speak("Volume increased.")
    else:
        speak("Volume is already at maximum.")

# Open Control Panel
def open_control_panel():
    os.system("control")
    speak("Opening Control Panel.")

# Open System Settings (Windows 10/11)
def open_system_settings():
    os.system("start ms-settings:")
    speak("Opening system settings.")


# Open Network Connections
def open_network_connections():
    os.system("ncpa.cpl")
    speak("Opening Network Connections.")

# Open Device Manager
def open_device_manager():
    os.system("devmgmt.msc")
    speak("Opening Device Manager.")

# Clear system cache (Windows)
def clear_system_cache():
    os.system("del /q/f/s %TEMP%\*")
    speak("System cache cleared.")

# Enable or disable Wi-Fi
def toggle_wifi(state):
    if state == 'enable':
        os.system("netsh interface set interface 'Wi-Fi' enabled")
        speak("Wi-Fi is enabled.")
    elif state == 'disable':
        os.system("netsh interface set interface 'Wi-Fi' disabled")
        speak("Wi-Fi is disabled.")

# Open File Explorer
def open_file_explorer():
    os.system("explorer")
    speak("Opening File Explorer.")

# Function to decrease the volume
def decrease_volume():
    volume = engine.getProperty('volume')  # Get the current volume
    if volume > 0.0:  # Minimum volume is 0.0
        engine.setProperty('volume', volume - 0.1)  # Decrease volume by 0.1
        speak("Volume decreased.")
    else:
        speak("Volume is already at minimum.")

# Change system volume (mute/unmute)
def mute_system():
    os.system("nircmd.exe mutesysvolume 1")  # Mutes the system volume
    speak("System volume is now muted.")

def unmute_system():
    os.system("nircmd.exe mutesysvolume 0")  # Unmutes the system volume
    speak("System volume is now unmuted.")


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'increase volume' in query:
            increase_volume()

        elif 'decrease volume' in query:
            decrease_volume()

        elif 'mute system' in query:
            mute_system()

        elif 'unmute system' in query:
            unmute_system()
        
        elif 'open control panel' in query:
            open_control_panel()

        elif 'open system settings' in query:
            open_system_settings()

        elif 'open network connections' in query:
            open_network_connections()

        elif 'open device manager' in query:
            open_device_manager()

        elif 'clear system cache' in query:
            clear_system_cache()

        elif 'enable Wi-Fi' in query:
            toggle_wifi('enable')

        elif 'disable wifi' in query:
            toggle_wifi('disable')

        elif 'open file explorer' in query:
            open_file_explorer()

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
            speak("Opening youtube")
        
        elif 'open chrome' in query:
            webbrowser.open("https://google.com")  # Opens Chrome
            speak("Opening Google Chrome")
        
        elif 'play music' in query:
            music_dir = 'D:\\Non critical\\Music\\songs'  # Change to your music directory
            songs = os.listdir(music_dir)
            print("Available songs:", songs)
            if songs:  # Check if there are any songs in the directory
                os.startfile(os.path.join(music_dir, songs[0]))  # Plays the first song
            else:
                print("No songs found in the directory.")
        
        elif 'display time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif 'check battery' in query:
            check_battery_status()

        elif 'open microsoft edge' in query:
            webbrowser.open("https://www.microsoft.com")
            speak("Opening microsoft edge")
        
        elif 'display date' in query:
            strDate = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Sir, today's date is {strDate}")
        
        elif 'tell a joke' in query:
            jokes = ["Tell me the first ten digits of your sister's phone number."]
            speak(jokes[0])  # Speak the first joke
        
        elif 'open whatsapp' in query:
            speak("Trying to open WhatsApp")
    
            # Path to WhatsApp executable (change according to your system)
            whatsapp_path = r"C:\Users\YourUsername\AppData\Local\WhatsApp\WhatsApp.exe"  # Replace with actual path
    
            # Check if the path exists
            if os.path.exists(whatsapp_path):
             speak("Opening WhatsApp Desktop")
             os.startfile(whatsapp_path)
            else:
             speak("WhatsApp is not installed or the path is incorrect. Trying WhatsApp Web.")
             webbrowser.open("https://web.whatsapp.com")
             speak("Opening Whatsapp web")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("Opening Facebook")
        
        elif 'open twitter' in query:
            webbrowser.open("https://www.twitter.com")
            speak("Opening twitter")
        
        elif 'open instagram' in query:
            webbrowser.open("https://instagram.com")
            speak("Opening Instagram")
        
        elif 'tell me a best line' in query:
            quote = random.choice(quotes)  # Select a random quote
            speak(quote)
        
        elif 'search' in query:
            speak("What would you like to search for?")
            search_query = takeCommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'open email' in query:
            webbrowser.open("https://mail.google.com")
            speak("Opening Google Email")
        
        elif 'open wikipedia' in query:
            webbrowser.open("https://www.wikipedia.org")
            speak("Opening wikipedia for you")

        elif 'set an alarm' in query:
            speak("Please tell me the time for the alarm (in HH:MM format).")
            alarm_time = takeCommand().lower()
            # Simple alarm set logic
            speak(f"Alarm set for {alarm_time}.")
        
        elif 'tell a random fact' in query:
            fact = random.choice(facts)
            speak(fact)
        
        elif 'tell about weather' in query:
            speak("Which city would you like the weather for?")
            city = takeCommand().lower()  # Capture city input from user
            city = city.capitalize()  # Capitalize the first letter for consistency
            get_weather(city)  # Call the get_weather function with the city name
                
        elif 'open money converter' in query:
            webbrowser.open("https://www.xe.com") 
            speak("Opening a Currency Converter")
        
        elif 'open bbc' in query:
            webbrowser.open("https://www.bbc.com")
            speak("Opening BBC News Website")

        elif 'open cnn' in query:
            webbrowser.open("https://edition.cnn.com") 
            speak("Opening CNN news website")

        elif 'open Al Jazeera' in query:
            webbrowser.open("https://www.alijazeera.com")
            speak("Opening Al Jazeera News Website")

        elif 'open hindustan times' in query:
            webbrowser.open("https://hindustantimes.com")
            speak("Opening Hindustan Times News Website")
        
        elif 'open Dawn' in query:
            webbrowser.open("https://www.dawn.com")
            speak("Opening Dawn News Website")           
        
        elif 'open google maps' in query:
            webbrowser.open("https://www.google.com/maps")
            speak("Opening Google Maps")
        
        elif 'open google drive' in query:
            webbrowser.open("https://drive.google.com")
            speak("Opening Google Drive")
        
        elif 'open google translate' in query:
            webbrowser.open("https://translate.google.com/")
            speak("Opening Google Translate")
        
        elif 'make notes' in query:
            webbrowser.open("https://keep.google.com")
            speak("Opening Google Notes")

        elif 'open google calendar' in query:
            webbrowser.open("https://calendar.google.com")
            speak("Opening Google Calendar")
        
        elif 'open calculator' in query:
            webbrowser.open("https://www.desmos.com")
            speak("Opening Google Calculator")
        
        elif 'watch movies in hindi' in query:
            webbrowser.open("https://hdmovies.show")
            speak("Opening the website")
        
        elif 'watch english movies' in query:
            webbrowser.open("https://gomovies.sx")    
            speak("Ooening go movies.com")
        
        elif 'play songs online' in query:
            webbrowser.open("https://music.youtube.com")
            speak("Opening youtube music")
        
        elif 'generate image' in query:
            webbrowser.open("https://ideogram.ai")    
            speak("Opening ideogram")

        elif 'open chat' in query:
            webbrowser.open("https://chatgpt.com")
            speak("Opening Chat Gpt")

        elif 'check horoscope' in query:
            webbrowser.open("https://www.horoscope.com")
            speak("Showing you the Horoscope")
        
        elif 'open gemini' in query:
            webbrowser.open("https://gemini.google.com")
            speak("Opening Google Gemini")
        
        elif 'watch anime' in query:
            webbrowser.open("https://aniwatchtv.to")
            speak("Opening Ani Watch Tv")
        
        elif 'open microsoft store' in query:
            webbrowser.open("https://apps.microsoft.com")
            speak("Opening microsoft store")
        
        elif 'tell about stocks' in query:
            webbrowser.open("https://www.psx.com.pk")
            speak("The Stock Prices in Pakistan today are being shown to you.")
        
        elif 'play a game' in query:
            speak("Let's play Rock, Paper, Scissors. Say your choice.")
            user_choice = takeCommand().lower()
            choices = ['rock', 'paper', 'scissors']
            computer_choice = random.choice(choices)
            speak(f"I chose {computer_choice}.")
            if user_choice == computer_choice:
               speak("It's a tie!")
            elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                 (user_choice == 'paper' and computer_choice == 'rock') or \
                 (user_choice == 'scissors' and computer_choice == 'paper'):
                speak("You win!")
            else:
                speak("I win!")

        
        elif 'shutdown system' in query:
            speak("Shutting down the system.")
            os.system("shutdown /s /t 1")
            speak("Shutting Dowm system")
    
        elif 'restart system' in query:
            speak("Restarting the system.")
            os.system("shutdown /r /t 1")
            speak("Restarting the system")
    
        elif 'lock system' in query:
            speak("Locking the system.")
            os.system("rundll32.exe user32.dll,LockWorkStation")
            speak("Locking Your System right now Sir")

        elif 'stop' in query:
            speak("Goodbye, Sir!")
            break

