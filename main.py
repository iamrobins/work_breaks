import datetime
from playsound import playsound
from notifypy import Notify

notification = Notify()

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
                playsound("sound/speech.mp3")
            except:
                print("No speech found")
            last_time = datetime.datetime.now()


main()
