import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to microphone input and return recognized text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()  # Return lowercase for easier comparison
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError as e:
        speak(f"Could not request results; {e}")
        return ""

# Example usage
while True:
    command = listen()
    
    if "hello" in command:
        speak("Hello there! How can I help you?")
    elif "goodbye" in command:
        speak("Goodbye! Have a nice day!")
        break
    elif command:  # If command isn't empty
        speak(f"You said: {command}")