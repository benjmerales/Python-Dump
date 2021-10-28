import tkinter as tk

window = tk.Tk()

def handle_keypress(event):
    print(event.char)
def handle_click(event):
    print("Left Mouse Button Was Clicked!")
window.bind("<Key>", handle_keypress)
window.bind("<Button-1>", handle_click)
window.mainloop()
