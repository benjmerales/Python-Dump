import keyboard

keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered ', 'hotkey'))

keyboard.add_hotkey('/', lambda: keyboard.write('foobar'))
