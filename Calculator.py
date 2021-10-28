import tkinter as tk
from functools import partial
def calculate():
    A = float(EntryA.get())
    B = float(EntryB.get())
    C = 0
    sign = Sign["text"]
    if sign is '+':
        C = A + B
    elif sign is '-':
        C = A - B
    elif sign is '*':
        C = A * B
    elif sign is '/':
        C = A / B
    Result["text"] = C
def change(signed):
    sign = signed
    Sign["text"] = sign

window = tk.Tk()
window.title("Simple Calculator")
FrameEntry = tk.Frame(master=window, relief = tk.SUNKEN, borderwidth = 1)
EntryA = tk.Entry(master=FrameEntry)
Sign = tk.Label(FrameEntry, text=" ")
EntryB = tk.Entry(master=FrameEntry)
Result = tk.Label(text="_____", master=FrameEntry)

FrameButton = tk.Frame(master=window, relief = tk.SUNKEN, borderwidth = 1)
B_plus = tk.Button(text="+", master=FrameButton, command=partial(change, '+'))
B_minu = tk.Button(text="-", master=FrameButton, command=partial(change, '-'))
B_time = tk.Button(text="*", master=FrameButton, command=partial(change, '*'))
B_divi = tk.Button(text="/", master=FrameButton, command=partial(change, '/'))
B_equa = tk.Button(text="=", master=FrameButton, command=calculate)
B = [B_plus, B_minu, B_time, B_divi, B_equa]

FrameEntry.grid(row=0, column=1, padx=10, pady=10)
FrameButton.grid(row=0, column=2,padx=10, pady=10)

EntryA.grid(row=0, column=1)
Sign.grid(row=1, column=1)
EntryB.grid(row=2, column=1)
Result.grid(row=3, column=1)

for i in B:
    i.grid()
window.mainloop()
