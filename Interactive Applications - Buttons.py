import tkinter as tk
def handle_click(event):
    print("The button was clicked!")
window = tk.Tk()
button = tk.Button(text="Click me!")
button.bind("<Button-1>", handle_click)
button.grid()
window.mainloop()
