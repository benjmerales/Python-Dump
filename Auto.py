import keyboard
import pyautogui

toggle = False
while True:
    if keyboard.is_pressed('['):
        toggle = True
    elif keyboard.is_pressed(']'):
        toggle = False
    elif keyboard.is_pressed('\\'):
        print('Break')
        break

    if toggle:
        pyautogui.click(button='right')
