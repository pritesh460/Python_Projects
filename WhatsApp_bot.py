import pyautogui
import pyperclip
import time
from openai import OpenAI

client = OpenAI()

def get_last_sender(chat_text):
    messages = chat_text.strip().split("/2026]")
    last_msg = messages[-1]

    if ":" in last_msg:
        sender = last_msg.split(":")[0].strip()
        return sender
    return None

time.sleep(2)
pyautogui.click(463, 750)   
time.sleep(1)

while True:

    pyautogui.moveTo(507, 192)
    pyautogui.mouseDown()
    pyautogui.moveTo(728, 671, duration=1.0)
    pyautogui.mouseUp()

    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    chat_text = pyperclip.paste()

    pyautogui.click(1300, 186)

    print("Copied Text:")
    print(chat_text)

    last_sender = get_last_sender(chat_text)

    if last_sender and last_sender.lower() != "pritesh":

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a person named Pritesh who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Pritesh, [6:13 pm, 17/1/2026] Pritesh: Output should be the next chat response (text message only)"},
                {"role": "user", "content": chat_text}
            ]
        )

        ai_message = response.choices[0].message.content

        print("\nGenerated Message:")
        print(ai_message)

        time.sleep(1)
        pyautogui.click(700, 720)   
        time.sleep(0.5)

        pyperclip.copy(ai_message)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.3)
        pyautogui.press('enter')