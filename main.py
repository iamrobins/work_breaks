import datetime
import time
import threading
from playsound import playsound
from notifypy import Notify
from custom_types import AppState

notification = Notify()
continue_reminder_time: int = 5 #5 minutes

def main():
    print("Simple break reminder script\n")
    pref_time: int = prefered_time_inp()
    print("Script Started !!")
    break_reminder(pref_time)

def send_notification(title: str, message: str, icon: str) -> None:
    """
    Sends notification to user
    """
    notification.title = "Break Time!!"
    notification.message = "Do you know taking little breaks between your work is way of improving your efficiency."
    notification.icon = "images/logo.png"
    notification.send(block=False)


def prefered_time_inp() -> int:
    """Returns time in seconds"""
    while True:
        try:
            pref_time = 60 * \
                int(input("Enter your break preference in minutes: "))
            return pref_time
        except:
            print("Please provide a valid value “for example 20” ")
            continue


def continue_reminder(state) -> None:
    """Reminds about coming back to work after break"""
    time.sleep(continue_reminder_time)
    while(not state["break_over"]):
        send_notification(title="Continue Reminder", message="Don't forget to get back to work after the break", icon="images/logo.png")
        playsound("sound/countinue_work.mp3")
        time.sleep(continue_reminder_time)


def break_reminder(pref_time: int) -> None:
    """Reminds about taking a break based on preferred time"""
    last_time = datetime.datetime.now()

    while True:
        diff = (datetime.datetime.now() - last_time).total_seconds()
        if diff > pref_time:
            print("Hey, I am your assistant please take a break.")
            try:
                send_notification(title="Break Time!!", message="Do you know taking little breaks between your work is way of improving your efficiency.", icon="images/logo.png")
                playsound("sound/take_break.mp3")

                # Countinue Work
                state: AppState = {
                    "break_over": False
                }
                continue_reminder_t: threading.Thread = threading.Thread(target=continue_reminder, args=(state,))
                continue_reminder_t.start()
                input("Did you take the break?\nPress any key to continue.")
                state["break_over"] = True
                print("You are doing good. Keep up")
            except:
                print("No speech found")
            last_time = datetime.datetime.now()


main()