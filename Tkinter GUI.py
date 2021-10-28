import tkinter as tk

window = tk.Tk()
greeting = tk.Label(
    text="Python Rocks!",
    fg="black",
    bg="#34A2FE",
    width=10,
    height=10)

#greeting.pack()

button = tk.Button(
    text="Click Me!",
    width=25,
    height=5,
    bg = "blue",
    fg = "#34A2FE")

#button.pack()

label = tk.Label(text="Name: ")
entry = tk.Entry()
#label.pack()
#entry.pack()

#entry.get()
#entry.delete(0, tk.END)
#entry.insert(0, "Python")
#window.mainloop() # tkinter event loop

text_box = tk.Text()
text_box.pack()
