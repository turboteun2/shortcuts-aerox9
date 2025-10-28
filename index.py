import keyboard
import os
import pyautogui
import time

startApp = False
last_key = None
last_key_time = 0
debounce_time = 2

def toggle_boolean(value):
    """Toggles a boolean value."""
    return not value

# C:/Users/tgr/AppData/Roaming/Microsoft/Excel/XLSTART/PERSONAL.XLSB
os.startfile(r"C:/Users/tgr/AppData/Roaming/Microsoft/Excel/XLSTART/PERSONAL.XLSB")

def start_app(key):
    """Starts specific applications or runs commands based on the key pressed."""
    global startApp
    app_paths = {
        "f13": r"C:/Users/tgr/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/AFAS Insite.lnk",  
        "f15": r"C:/Users/tgr/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Microsoft OneNote.lnk", 
        "f14": r"C:/Users/tgr/OneDrive - Eshuis Accountants en Adviseurs/Bureaublad/Microsoft Teams (work or school).lnk",   
        "f16": r"C:/Users/tgr/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Microsoft Outlook.lnk",
        "f19": r"C:/Users/tgr/AppData/Roaming/Microsoft/Excel/XLSTART/PERSONAL.XLSB",
        "f18": r"C:/system32/notepad.exe", # <-- werkt niet
    }
    
    if key in app_paths:
        os.startfile(app_paths[key])
        startApp = False
    elif key == "f17":
        pyautogui.hotkey('ctrl', 'alt', 'c')
    elif key == "f23":
        # os.system("")  # Add system command if needed
        toggle_boolean(startApp)

def excel_shortcuts(logging):
    """Executes specific Excel shortcuts based on the key pressed."""
    shortcuts = {
        "f13": [('ctrl', 'shift', 'p'), ('ctrl', 'x'), ('ctrl', 'v')],
        "f14": [('ctrl', 'shift', 't'), ('ctrl', 'x'), ('ctrl', 'v')],
        "f15": [('ctrl', 'shift', 'm')],
        "f16": [('ctrl', 'v')],
        "f17": [],
        "f18": [('ctrl', 'pgdn')],
        "f19": [('ctrl', 'pgup')]
    }

    if logging in shortcuts:
        for keys in shortcuts[logging]:
            pyautogui.hotkey(*keys)
            time.sleep(0.2)
    elif logging == "f16":
        pyautogui.hotkey('alt')
        pyautogui.hotkey('w')

def log_key_press(event):
    """Logs key presses and triggers the corresponding action with debounce protection."""
    global startApp, last_key, last_key_time
    key = event.name

    # Debounce mechanism: ignore if the key is the same as the last one and within the debounce time
    current_time = time.time()
    if key == last_key and (current_time - last_key_time) < debounce_time:
        return  # Ignore repeated key presses within debounce time

    # Update last key and time
    last_key = key
    last_key_time = current_time

    if key == "f20":
        startApp = toggle_boolean(startApp)
    elif startApp:
        start_app(key)
    else:
        excel_shortcuts(key)

# Register the callback for all key presses
keyboard.on_press(log_key_press)

# To keep the script running, until 'esc' is pressed
keyboard.wait()
