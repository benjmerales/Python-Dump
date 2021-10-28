import winsound as W 
import tkinter as tk

INTERVAL = 1
CNT = 0
def getCNT():
	global CNT
	return CNT
def setCNT(x):
	global CNT
	CNT+=x
def increase(event):
	get = int(level["text"])
	get += INTERVAL*1000
	level["text"]=get
def decrease(event):

	get = int(level["text"])

	get -= INTERVAL*1000
	if get >= 0:
		level["text"]=get
def playSound(event):
	setCNT(1)
	print("Working... Button Press Attempt", getCNT())

	W.Beep(int(level["text"]),1000)
win = tk.Tk()

setting_frame = tk.Frame(master=win,relief=tk.RAISED, borderwidth=1)
setting_frame.grid(padx=20, pady=10)

button1 = tk.Button(text=" < ", master=setting_frame)
button1.bind("<Button-1>", decrease)
button2 = tk.Button(text=" > ", master=setting_frame)
button2.bind("<Button-1>", increase)
level = tk.Label(master=setting_frame, text="1000")
play = tk.Button(text="Play!")
play.bind("<Button-1>", playSound)

button1.grid(row=0, column=0)
button2.grid(row=0, column=2)
level.grid(row=0, column=1)
play.grid(row=1, pady=10)
win.mainloop()
#W.Beep(15000,5000)