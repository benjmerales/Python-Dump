import tkinter as tk
import random
import winsound
from functools import partial


def resetBoard(B):
	for b in B:
		b['background'] = "Yellow"
	cnt = 0
	generate()
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
			cnt+=1
	return data
def printB(choices):
	print(choices)
	return
def gui(data):
	def press(i,j,thisbutton):
		print(thisbutton['text'], " | ", data[i][j])
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
	count = 1
	BUTTONS = []
	window = tk.Tk()
	for i in range(3):
		for j in range(3):

			button = tk.Button(master=window, text=str(data[i][j]), background="Yellow")
			BUTTONS.append(button)
			button.config(command=partial(press,i,j,button))
			button.grid(row=i,column=j,padx=5,pady=5,sticky='nes')
	window.mainloop()

def MAIN():
	data = generate()
	gui(data)

MAIN()