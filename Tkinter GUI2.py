import tkinter as tk

window = tk.Tk()

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}
'''
frameA = tk.Frame()
frameB = tk.Frame()

labelA = tk.Label(master=frameA, text="I'm in Frame A")
labelA.pack()

labelB = tk.Label(master=frameB, text="I'm in Frame B")
labelB.pack()

frameB.pack()
frameA.pack()
'''

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()
window.mainloop()
