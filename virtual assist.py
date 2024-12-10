import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import time
import webbrowser

# Initialize the speech engine
engine = pyttsx3.init()

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's command
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # To reduce noise
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"Command recognized: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        speak("Sorry, the service is down.")
        return None

# Function to set reminders
def set_reminder():
    speak("What should I remind you about?")
    reminder = listen()
    if reminder:
        speak(f"Reminder set for: {reminder}")
        # You can implement reminder functionality with time.sleep() for simplicity
        time.sleep(5)  # For demo purposes, waits for 5 seconds
        speak(f"Reminder: {reminder}")

# Function to play music
def play_music():
    speak("What song would you like me to play?")
    song = listen()
    if song:
        speak(f"Playing {song}")
        kit.playonyt(song)

# Function to search the web
def search_web():
    speak("What would you like to search for?")
    query = listen()
    if query:
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

# Main function to control the assistant
def main():
    speak("Hello, I am your virtual assistant. How can I help you today?")
    
    while True:
        command = listen()
        
        if command:
            if 'reminder' in command:
                set_reminder()
            elif 'play music' in command:
                play_music()
            elif 'search' in command:
                search_web()
            elif 'time' in command:
                current_time = datetime.datetime.now().strftime("%H:%M")
                speak(f"The time is {current_time}")
            elif 'stop' in command or 'exit' in command:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I didn't catch that. Please try again.")

if __name__ == "__main__":
    main()
