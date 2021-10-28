import keyboard, pyautogui,time,math

print("Press P to quit")
drag = False
while True:
    try:
        if keyboard.is_pressed('p'):
            print('\b Quitting',end=""); time.sleep(0.5);
            print('.',end=""); time.sleep(0.5);
            print('.',end=""); time.sleep(0.5);
            print('.',end="");
            break
        if keyboard.is_pressed('w'):
            if drag is False:
                print("Released W")
                pyautogui.moveRel(0,-10)
                pass
            else:
                print("Dragged W")
                pyautogui.dragRel(0,-10)
                pass
        elif keyboard.is_pressed('a'):
            if drag is False:
                print("Released A")
                pyautogui.moveRel(-10,0)
                pass
            else:
                print("Dragged A")
                pyautogui.dragRel(-10,0)
                pass
        elif keyboard.is_pressed('s'):
            if drag is False:
                print("Released S")
                pyautogui.moveRel(0,10)
                pass
            else:
                print("Dragged S")
                pyautogui.dragRel(0,10)
                pass
        elif keyboard.is_pressed('d'):
            if drag is False:
                print("Released D")
                pyautogui.moveRel(10,0)
                pass
            else:
                print("Dragged D")
                pyautogui.dragRel(10,0)
                pass
        elif keyboard.is_pressed('j'):
            drag = True
            print("Drag is Toggled")
            pass
        elif keyboard.is_pressed('k'):
            drag = False
            print("Release is Toggled")
            pass
        else:
            pass
    except:
        break
