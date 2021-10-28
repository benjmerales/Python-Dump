import keyboard
import pyautogui as pag
while True:
    key = keyboard.read_key()
    print(key)
    if key is 'esc':
        break
    if key is 'space':
        pag.click()     
