import pyautogui
import random
import time

while True:
    random_time = random.randint(1, 5)

    time.sleep(random_time)

    myScreenshot = pyautogui.screenshot()

    file_name = str(time.time())+".png"
    myScreenshot.save(file_name)
