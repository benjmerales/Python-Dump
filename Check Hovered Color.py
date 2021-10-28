import pyautogui as pag
import tkinter as tk
import time
window = tk.Tk()
frame = tk.Frame(master=window, width=100, height=100, bg="black")
frame.pack()


while True:
   frame.pack()
   im = pag.screenshot()
   pos = pag.position()
   color = im.getpixel(pos)
   print(color)


