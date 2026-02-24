import pyautogui
import time
import datetime 

time.sleep(2)

while True:
    print(datetime.datetime.now())
    pyautogui.typewrite("Reminder: Drink water!")
    pyautogui.press("enter")
    time.sleep(31)

    print(datetime.datetime.now())
    pyautogui.typewrite("Reminder: Take medicine!")
    pyautogui.press("enter")
    time.sleep(31)

    print(datetime.datetime.now())
    pyautogui.typewrite("Reminder: Take the dog for a walk!")
    pyautogui.press("enter")
    time.sleep(31)