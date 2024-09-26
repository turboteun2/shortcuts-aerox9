import keyboard
import os
import pyautogui
import time

startApp = False

def toggle_boolean(value):
    """Toggles a boolean value."""
    return not value

def start_app(key):
    """Starts specific applications or runs commands based on the key pressed."""
    global startApp
    app_paths = {
        "f13": r"",  # Add path for AFAS
        "f14": r"",  # Add path for Paint
        "f15": r"",  # Add path for text file
        "f16": r"",
        "f17": r"",
        "f18": r"",
        "f19": r""
    }
    
    if key in app_paths:
        os.startfile(app_paths[key])
        startApp = False
    elif key == "f20":
        os.system("")  # Add system command if needed
        startApp = False

def excel_shortcuts(logging):
    """Executes specific Excel shortcuts based on the key pressed."""
    shortcuts = {
        "f13": [('ctrl', 'shift', 'p'), ('ctrl', 'x'), ('ctrl', 'v')],
        "f14": [('ctrl', 'shift', 't'), ('ctrl', 'x'), ('ctrl', 'v')],
        "f15": [('ctrl', 'shift', 'm')],
        "f16": [('ctrl', 'c'), ('ctrl', 'v')],
    }

    if logging in shortcuts:
        for keys in shortcuts[logging]:
            pyautogui.hotkey(*keys)
            time.sleep(0.1)
    elif logging == "f16":
        pyautogui.hotkey('alt')
        pyautogui.hotkey('w')

def log_key_press(event):
    """Logs key presses and triggers the corresponding action."""
    global startApp
    key = event.name

    if key == "f23":
        startApp = toggle_boolean(startApp)
    elif startApp:
        start_app(key)
    else:
        excel_shortcuts(key)

# Register the callback for all key presses
keyboard.on_press(log_key_press)

# To keep the script running, until 'esc' is pressed
keyboard.wait()
