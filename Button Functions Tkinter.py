import tkinter as tk
from functools import partial

buttons = [[None for j in range(3)] for i in range(3)]
def hi(i, j, event):
	buttons[i][j]['background'] = "#123424"
window = tk.Tk()
for i in range(3):
	window.columnconfigure(i, weight=1, minsize=75)
	window.rowconfigure(i, weight=1, minsize=50)

	for j in range(3):
		frame = tk.Frame( master=window, relief = tk.RAISED, borderwidth=1)
		frame.grid(row=i, column=j, padx=5, pady=5)

		button = tk.Button(master = frame, text=f"Row {i}\nColumn{j}")
		buttons[i][j] = button
		button.bind("<Button-1>", partial(hi,i,j))
		button.pack()
window.config(background="black")
window.mainloop()