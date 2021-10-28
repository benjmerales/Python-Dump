import tkinter as tk
import random
import winsound
from functools import partial

choices = [i+1 for i in range(9)]
window = tk.Tk()
count = 1
def press(i,j,thisbutton):
	global count, BUTTONS, data
	for b in BUTTONS:
		b['text'] = "0"
	this = data[i][j]
	if int(this) == count:
		thisbutton['background'] = "Green"
		winsound.Beep(1000,250)
		count+=1

		if count == 10:
			winner()
	else:
		thisbutton['background'] = "Red"
		winsound.Beep(500,250)
		winsound.Beep(400,250)
		print("Incorrect")
		count=1
		resetBoard(BUTTONS)
	return
def resetBoard(B):
	for b in B:
		b['background'] = "Yellow"

	cnt = 0 
	for i in range(3):
		for j in range(3):
			BUTTONS[cnt]['text'] = data[i][j]
			cnt+=1 
	return
def winner():
	winsound.Beep(1000,250)
	winsound.Beep(1500,250)
	winsound.Beep(1000,250)
	winsound.Beep(1700,250)
	generate()
def generate():
	data = [[0 for i in range(3)] for j in range(3)]
	choices = [i+1 for i in range(9)]
	cnt = 0 
	for i in range(3):
		for j in range(3):
			select = random.choice(choices)
			data[i][j] = select
			choices.remove(select)
			BUTTONS[cnt]['text'] = data[i][j]
			cnt+=1
	global count
	count = 1
BUTTONS = []
data = [[0 for i in range(3)] for j in range(3)]

for i in range(3):
	for j in range(3):
		select=random.choice(choices)
		data[i][j] = select
		choices.remove(select)

		button = tk.Button(master=window, text=str(select), background="Yellow")
		BUTTONS.append(button)
		button.config(command=partial(press,i,j,button))
		button.grid(row=i,column=j,padx=5,pady=5,sticky='nes')
print(data)
window.mainloop()