import pyautogui,time
time.sleep(5)
#NOTE PLS USE SUBLIME OR ANY TEXT EDITORS
#pyautogui.click(100,100)    # sends click to the coordinates 100,100

pyautogui.typewrite('Hello world',0.25)
pyautogui.typewrite(['enter','a','b','left','left','X','Y'],0.10)
pyautogui.keyDown('ctrl')
pyautogui.press('n')
pyautogui.keyUp('ctrl')

