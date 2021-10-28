import tkinter as tk
def convert():
    fahrenheit = float(ent_temperature.get())
    lbl_result["text"] = (N - 32) * (5/9)
window = tk.Tk()

frame = tk.Frame(
    master = window,
    relief = tk.SUNKEN,
    borderwidth = 1
    )
frame.pack()
ent_temperature = tk.Entry(master=frame)
ent_temperature.grid(row=1, column=1, padx=10, pady=10)
F = tk.Label(master=frame, text="\N{DEGREE FAHRENHEIT}")
F.grid(row=1,column=2 , padx=10, pady=10)
btn_convert = tk.Button(master=frame, text="\N{RIGHTWARDS BLACK ARROW}", command=convert)
btn_convert.grid(row=1, column=3 , padx=10, pady=10)
lbl_result = tk.Label(master=frame, text="")
lbl_result.grid(row=1, column=4 , padx=10, pady=10)
C = tk.Label(master=frame, text="\N{DEGREE CELSIUS}")
C.grid(row=1, column=5, padx=10, pady=10)
