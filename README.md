# Keyboard Automation Script - for mouse with lots of buttons

This Python script automates the use of keyboard shortcuts and application launches using the `keyboard` and `pyautogui` modules. It allows for the execution of specific tasks with function keys, including launching applications and performing keyboard macros in Excel.

## Setup Instructions

1. **Install dependencies:**
   - Install the required Python packages by running:
     ```bash
     pip install keyboard pyautogui
     ```

2. **Add the script to Startup:**
   - Press `Windows Key + R` and type `shell:startup`.
   - Place the script in the Startup folder to ensure it runs automatically when Windows starts.

3. **Configure the Script:**
   - Modify the paths in the `app_paths` dictionary for each function key to specify the location of applications you want to launch (e.g., AFAS, Paint, etc.).
   - Optionally, add a system command for `f20` in the `os.system()` function.

4. **Hotkeys:**
   - `f13-f19`: Used to launch specific applications or perform system commands.
   - `f23`: Toggles the state for launching applications.
   - Excel shortcuts (performed without toggling `f23`):
     - `f13`: Executes `Ctrl + Shift + P`, `Ctrl + X`, and `Ctrl + V`.
     - `f14`: Executes `Ctrl + Shift + T`, `Ctrl + X`, and `Ctrl + V`.
     - `f15`: Executes `Ctrl + Shift + M`.
     - `f16`: Copies with `Ctrl + C` and pastes with `Ctrl + V`.

5. **Run the Script:**
   - Once the script is in the Startup folder, it will run in the background and listen for keypresses.
   - To terminate the script, press `Esc`.

## Dependencies

- `keyboard`: Allows listening to global keypresses.
- `pyautogui`: Automates keyboard shortcuts and other GUI interactions.

## License

This project is licensed under the MIT License.
