import datetime
import time
import threading
from playsound import playsound
from notifypy import Notify

notification = Notify()
continue_reminder_time = 300 #5 minutes

def main():
    print("Simple break reminder script\n")
    pref_time = prefered_time_inp()
    print("Script Started !!")
    break_reminder(pref_time)


def prefered_time_inp():
    while True:
        try:
            pref_time = 60 * \
                int(input("Enter your break preference in minutes: "))
            return pref_time
        except:
            print("Please provide a valid value “for example 20” ")
            continue


def continue_reminder(state):
    time.sleep(continue_reminder_time)
    while(not state["break_over"]):
        playsound("sound/countinue_work.mp3")
        time.sleep(continue_reminder_time)


def break_reminder(pref_time):
    last_time = datetime.datetime.now()

    while True:
        diff = (datetime.datetime.now() - last_time).total_seconds()
        if diff > pref_time:
            print("Hey, I am your assistant please take a break.")
            try:
                notification.title = "Break Time!!"
                notification.message = "Do you know taking little breaks between your work is way of improving your efficiency."
                notification.icon = "images/logo.png"
                notification.send(block=False)
                playsound("sound/take_break.mp3")

                # Countinue Work
                state = {
                    "break_over": False
                }
                countinue = threading.Thread(target=continue_reminder, args=(state,))
                countinue.start()
                confirmation = input("Did you take the break?\nPress any key to continue.")
                state["break_over"] = True
                print("You are doing good. Keep up")
            except:
                print("No speech found")
            last_time = datetime.datetime.now()


main()