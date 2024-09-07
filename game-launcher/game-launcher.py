# compile to exe using PyInstaller:
# pyinstaller --onefile --noconsole game-launcher.py
# select as not steam game 
# in game properties add the game name

import sys
import pyautogui
import psutil
import time

if len(sys.argv) < 2: # check for required args
    print("plz add a target string")
    sys.exit(1)

target = sys.argv[1]

# win key
pyautogui.press('win')

# enter the target
pyautogui.typewrite(target)

# submit
pyautogui.press('enter')

# is process alive?
def is_app_running(app_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and app_name.lower() in proc.info['name'].lower():
            return True
    return False


time.sleep(10) # some games change their name after launch

# Main loop to check if the application is running
while True:
    time.sleep(1)
    if not is_app_running(target):
        print(f"{target} is not running. Exiting...")
        sys.exit(0)
    
