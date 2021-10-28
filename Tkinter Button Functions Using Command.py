import tkinter as tk 
from functools import partial
def change_label_number(num):
	counter = int(str(label['text']))
	counter+=num
	label.config(text=str(counter))
win = tk.Tk()
label = tk.Label(win, text="0")
button = tk.Button(win, text="Button", command=partial(change_label_number, 1))
button.pack()
label.pack()
win.mainloop()