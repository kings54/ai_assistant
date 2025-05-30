# automation.py
import pyautogui
from selenium import webdriver
from tts import speak

def automate_task(task_name):
    if "open browser" in task_name.lower():
        driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
        driver.get("https://www.google.com")
        speak("Opening Google in your browser.")
    elif "type something" in task_name.lower():
        pyautogui.write("Hello, this is your AI assistant typing for you!")
        pyautogui.press("enter")
        speak("Typed the message for you.")
    else:
        speak("Sorry, I don't know how to do that yet!")
