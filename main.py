import datetime
import time
import threading
from playsound import playsound
from notifypy import Notify
from custom_types import AppState
from sys import exit, stderr
import gui

notification = Notify()
continue_reminder_time: int = 300 #5 minutes

def main():
    print("Simple break reminder script\n")
    pref_time: int = prefered_time_inp()
    print("Script Started !!")
    break_reminder(pref_time)

def get_input_from_gui() -> int:
    """
    Gets user's input, for prefered minutes, from gui window
    """
    graphics = gui.GUI()
    user_minutes = graphics.minutes
    
    while (user_minutes <= 0):
        graphics.create_input_gui()
        user_minutes = graphics.minutes
    return user_minutes

def get_continue_input_from_gui() -> int:
    """
    Gets user's input, for whether they want to keep receiving 
    notifications, or change the prefered time, from gui window
    """
    continue_window = gui.GUI()
    repeat = continue_window.repeat

    while(repeat == -1):
        continue_window.create_continue_gui()
        repeat = continue_window.repeat
    return repeat


def send_notification(title: str, message: str, icon: str) -> None:
    """
    Sends notification to user
    """
    notification.title = title
    notification.message = message
    notification.icon = icon
    notification.send(block=False)


def prefered_time_inp() -> int:
    """Returns time in seconds"""
    while True:
        try:
            float_input = float(input("Enter your break preference in minutes: "))
            pref_time = round(60 * float_input)
            return pref_time
        except ValueError:
            print("Please provide a valid value “for example 20” ")
        except KeyboardInterrupt:
            print("\nExiting program")
            exit()

def safe_playsound(path: str):
    try:
        playsound(path)
    except:
        print(f"Could not play sound: {path}", file=stderr)


def continue_reminder(state) -> None:
    """Reminds about coming back to work after break"""
    time.sleep(continue_reminder_time)
    while(not state.break_over and not state.quit):
        send_notification(title="Continue Reminder", message="Don't forget to get back to work after the break", icon="images/logo.png")
        safe_playsound("sound/countinue_work.mp3")
        time.sleep(continue_reminder_time)


def break_reminder(pref_time: int) -> None:
    """Reminds about taking a break based on preferred time"""
    last_time = datetime.datetime.now()

    while True:
        diff = (datetime.datetime.now() - last_time).total_seconds()
        if diff > pref_time:
            print("Hey, I am your assistant please take a break.")
            send_notification(title="Break Time!!", message="Do you know taking little breaks between your work is way of improving your efficiency.", icon="images/logo.png")
            safe_playsound("sound/take_break.mp3")
            # Continue Work
            state: AppState = AppState(break_over=False)
            continue_reminder_t: threading.Thread = threading.Thread(target=continue_reminder, args=(state,))
            continue_reminder_t.start()
            try:
                input("Did you take the break?\nPress Enter to continue or Ctrl-C to quit.\n")
            except KeyboardInterrupt:
                print("\nExiting program")
                state.quit = True
                exit()
            state.break_over = True
            #Verify that thread has actually stopped
            continue_reminder_t.join()
            print("You are doing good. Keep it up")
            last_time = datetime.datetime.now()

if __name__ == "__main__":
    main()
