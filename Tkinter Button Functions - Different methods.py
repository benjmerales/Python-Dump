elif version_info.major == 3:
    import tkinter as tk
    
from functools import partial
    

    
app = tk.Tk()
labelExample = tk.Button(app, text="0")

def change_label_number(num):
    counter = int(str(labelExample['text']))
    counter += num
    labelExample.config(text=str(counter))
    
#Pass Arguments to command in Tkinter Button With partials
buttonExample = tk.Button(app, text="Increase", width=30,
                          command=partial(change_label_number, 2))

#Pass Arguments to command in Tkinter Button With lambda Function
buttonExample2 = tk.Button(app, text="Increase", width=30,
                          command=lambda: change_label_number(2))

buttonExample.pack()
labelExample.pack()
app.mainloop()