# Start program in Windows Key + R - 'shell:startup' to start this script.
import keyboard
import os
import keyboard
import pyautogui
import keyboard
import time

startApp = False

def toggle_boolean(value):
    return not value

def start_app(key):
    global startApp
    # Start AFAS
    if key == "f13":
        os.startfile(r"")
        startApp = False
    # Start Paint
    elif key == "f14":
        os.startfile(r"")
        startApp = False
    # Start text file which is empty
    elif key == "f15":
        os.startfile(r"")
        startApp = False
    elif key == "f16":
        os.startfile(r"")
        startApp = False
    elif key == "f17":
        os.startfile(r"")
        startApp = False
    elif key == "f18":
        os.startfile(r"")
        startApp = False
    elif key == "f19":
        os.startfile(r"")
        startApp = False
    elif key == "f20":
        os.system("")
        startApp = False
        # quit()

# Function to log key presses
def log_key_press(event):
    global startApp
    logging = event.name
    if logging == "f23":
        startApp = toggle_boolean(startApp)
    elif startApp == True:
        start_app(logging)
    else:
        # Excel shortcuts, specify macro's
        # print(f"{logging}")
        if logging == "f13":
            # Perform Ctrl + Shift + P
            pyautogui.hotkey('ctrl', 'shift', 'p')
            # time.sleep(0.1)  # Wait for the shortcut to execute
            # Perform Ctrl + X
            pyautogui.hotkey('ctrl', 'x')
            # time.sleep(0.1)
            # Perform Ctrl + V
            pyautogui.hotkey('ctrl', 'v')
        elif logging == "f14":
            # Perform Ctrl + Shift + P
            pyautogui.hotkey('ctrl', 'shift', 't')
            # time.sleep(0.1)  # Wait for the shortcut to execute
            # Perform Ctrl + X
            pyautogui.hotkey('ctrl', 'x')
            # time.sleep(0.1)
            # Perform Ctrl + V
            pyautogui.hotkey('ctrl', 'v')
        elif logging == "f15":
            pyautogui.hotkey('ctrl', 'shift', 'm')
        elif logging == "f16":
            pyautogui.hotkey('ctrl', 'c')
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(.01)
            pyautogui.hotkey('alt')
            pyautogui.hotkey('w')


# Register the callback for all key presses
keyboard.on_press(log_key_press)

# To keep the script running, until 'esc' is pressed
keyboard.wait()
