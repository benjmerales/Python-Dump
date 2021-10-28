import keyboard
import time
import pyautogui

toggle = False
while True:
    if keyboard.is_pressed('['):
        pyautogui.mouseDown()
        
        toggle = True
    elif keyboard.is_pressed(']'):
        
        pyautogui.mouseUp()
        toggle = False
        print(toggle)
        
    if toggle:
        keyboard.press('w')
        time.sleep(1)
