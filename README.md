# Personal-Assistant-Jarvis
A personal assistant that does your job with a single voice command with salient features


****1. Modules and Libraries****
 Imported Modules
 pyttsx3: Used for text-to-speech functionality.
 speech_recognition: Enables speech recognition to convert spoken words into text.
 datetime: Helps fetch the current date and time.
 webbrowser: Opens web pages in the default browser.
 os: Provides OS-level functionalities (e.g., file and application handling).
 random: Generates random choices (used for facts, quotes, and websites).
 requests: Handles HTTP requests (used for weather API calls).

**2. Initialization**
 The text-to-speech engine (pyttsx3) is initialized with a voice property.
 voices[0] is selected as the default voice. You can adjust this index to change the voice.

**3. Functions**
 speak(audio)
 Converts text (audio) into speech and plays it aloud.

wishMe()
Greets the user based on the time of the day:

Morning: Before 12 PM.
Afternoon: Between 12 PM and 6 PM.
Evening: After 6 PM.
Introduces itself as "Jarvis" and asks how it can assist.
takeCommand()
Listens to the user's voice input via the microphone.
Converts the audio into text using Google's speech recognition API.
Returns the recognized text or "None" if recognition fails.
get_weather(city)
Uses the OpenWeatherMap API to fetch current weather information for a given city.
Extracts and announces:
Temperature
Weather description
Humidity
In case of errors (e.g., invalid city), apologizes to the user.

**4. Data Collections**
Lists
facts: Stores random interesting facts.
quotes: Stores motivational quotes.
websites: Stores URLs of popular websites.

**5. Main Program Logic**
Greeting
The program begins by calling wishMe() to greet the user.

**Command Loop**
The program continuously listens for commands in a loop. Based on the user's input (query), it performs specific tasks:
a. Opening Applications and Websites
YouTube, Chrome, Facebook, Twitter: Opens respective URLs.
WhatsApp: Attempts to open the desktop app (if installed); falls back to WhatsApp Web.
b. Entertainment
Play Music: Plays the first song from a predefined directory.
Tell a Joke: Provides a humorous statement.
Tell a Quote: Recites a motivational quote.
Tell a Fact: Shares a random fact.
c. Utility Tasks
Display Time/Date: Speaks the current time or date.
Search on Google: Performs a Google search for user-provided input.
Open Random Website: Opens a randomly selected website from the list.
Set an Alarm: Accepts an alarm time and confirms the setup (basic logic; actual functionality not implemented).
d. Weather Updates
Asks for a city name, fetches the weather data using the get_weather function, and announces the results.
e. Stop
Ends the loop and says goodbye.
**

**6. API Key**
The weather function uses a placeholder API key (47f5042f9812fe43a495b8daaf14ab5e). Replace this with your own valid OpenWeatherMap API key for real-world use.

**7. Error Handling**
Gracefully handles speech recognition errors by asking the user to repeat themselves.
Provides fallback mechanisms (e.g., for WhatsApp and weather data retrieval).

**8. Example Commands**
Here are sample commands and their corresponding actions:

"Open YouTube": Opens YouTube in the browser.
"Play music": Plays the first song from the predefined directory.
"Tell about weather": Provides weather updates for a specified city.
"Display time": Announces the current time.
"Stop": Exits the program.
This script demonstrates modular design, voice interaction, and real-time API integration to deliver a user-friendly virtual assistant experience.
