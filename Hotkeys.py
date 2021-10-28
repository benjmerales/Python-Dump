import pyautogui as pag
import keyboard

register_cnt = 0
register = []
coordinates = []
while True:
    key = keyboard.read_key()
    if key == 'enter':
        break
    if key not in register:
        coordinates.append(pag.position())
        register.append(key)
    
print(register)
print(coordinates)

while True:
    key = keyboard.read_key()
    if key is 'esc':
        break
    if key in register:
        current_coordinate = pag.position()
        location = register.index(key)
        print(location)
        pag.moveTo(coordinates[location])
        pag.click()
        pag.moveTo(current_coordinate)
        pag.click()
        
