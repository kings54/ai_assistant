# scheduler.py
import schedule
import time
from tts import speak

def scheduled_task():
    print("Scheduled task executed!")
    speak("I completed your scheduled task.")

def start_scheduler():
    schedule.every(1).minutes.do(scheduled_task)

    while True:
        schedule.run_pending()
        time.sleep(1)
