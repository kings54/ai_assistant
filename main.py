# main.py
import threading
from speech import listen_google_api
from nlp import ask_openai
from tts import speak
from automation import automate_task
from scheduler import start_scheduler

def main():
    while True:
        print("\nSay something to the assistant...")
        command = listen_google_api()
        print("You said:", command)

        if "exit" in command.lower():
            speak("Goodbye!")
            break
        elif "automate" in command.lower():
            automate_task(command)
        else:
            response = ask_openai(command)
            print("AI:", response)
            speak(response)

if __name__ == "__main__":
    # Start the scheduler in a background thread
    threading.Thread(target=start_scheduler, daemon=True).start()

    # Start the assistant
    main()
