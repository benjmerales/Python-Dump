import pyautogui,time
time.sleep(5)
#pyautogui.keyDown('win')
#pyautogui.press('d')
#pyautogui.keyUp('win')
#pyautogui.keyDown('ctrl')
#pyautogui.press('4')
#pyautogui.keyUp('ctrl')
try:
    while True:
        pyautogui.typewrite('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulumullamcorper mauris ut faucibus ullamcorper. Vivamus malesuada nisi non tellus imperdiet, a convallis eros congue. Integer vitae neque vulputate, vehicula leo tincidunt, volutpat neque. Vestibulum tincidunt enim eu ligula finibus, sed maximus ipsum elementum. Maecenas feugiat velit pulvinar, pulvinar nibh a, dignissim diam. Nullam viverra urna ac laoreet condimentum. Integer fermentum dui sed euismod gravida. Sed sem ligula, euismod vitae lacus vitae, facilisis ultrices orci. Fusce suscipit, diam non molestie vulputate, nisi justo maximus justo, dictum tincidunt massa justo consectetur risus. Praesent imperdiet metus id elit tincidunt, in condimentum mauris tempus. Nam interdum euismod sapien ac porta. Integer sit amet pulvinar sapien. Nullam venenatis, ipsum a molestie gravida, erat velit molestie nisl, ut auctor nunc justo at elit. Aliquam congue lectus sit amet pharetra sodales. Fusce faucibus, dolor nec lacinia malesuada, risus est placerat erat, in tincidunt erat leo quis sem.',0.001)
        #pyautogui.keyDown('ctrl')
        #pyautogui.press('n')
        #pyautogui.keyUp('ctrl')
        
except KeyboardInterrupt:
    print('Done')
