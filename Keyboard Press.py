import keyboard

while True:
    try:
        
        if keyboard.is_pressed('q'):
            print('You Pressed q')
            break   #Finish loop
        else:
            pass
    except:
        break   # if user pressed a key other than 'q' then loop will break
