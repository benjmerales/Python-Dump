import tkinter as tk
import time
import keyboard
import random
WINH = "#BC5F4E"
WINC = "#6b7b89"
class Cell:
    def __init__(self, key, pos, frame, label):
        self.key = key
        self.pos = pos
        self.frame = frame
        self.label = label
        self.set_cnt = 1
    def property(self):
        print("Key:", key,
              "\nPosition:", pos,
              "\nFrame:", frame,
              "\nLabel:", label)
    def set(self, N = 0):
        if N == 0:
            if self.set_cnt % 2 == 0:
                color = WINC
                if self.key in sequence:
                    sequence.remove(self.key)
            else:
                color = WINH
            self.frame["background"] = color
            self.label["background"] = color
            self.set_cnt += 1
        elif N == 1:
            self.frame["background"] = WINH
            self.label["background"] = WINH
            
        elif N == 2:
            self.frame["background"] = WINC
            self.label["background"] = WINC
            self.set_cnt = 1
    def set_cnt(self, c):
        self.set_cnt = c
    def get_cnt(self):
        return self.set_cnt
def handle_keypress(event):
    key = event.char
    if key in randKeys:
        cell = CellsDict[key]
        if key not in sequence:
            sequence.append(key)
        cell.set()

    elif key is "\\":
        print(sequence)
        if sequence == randKeys:
            print("Correct")
            sequence.clear()
            for i in CellsDict[i]:
                CellsDict[i].set(2)
    elif key is '`':
        sequence.clear()
        for i in CellsDict:
            CellsDict[i].set(2)


win = tk.Tk()
win["background"] = WINC
win.title("Game")
#win.rowconfigure(1, minsize=100, weight=1)
#win.columnconfigure(1, minsize=100, weight=1)
C = 0
R = 0
cnt = 0
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
randKeys = random.sample(letters, 9)
CellsDict = {}
sequence = []

for i in range(3):
    for j in range(3):
        frame = tk.Frame(master = win, relief = tk.GROOVE, borderwidth = 1, background= WINC )
        this = tk.Label(text=randKeys[cnt], master=frame, background = WINC)
        CellsDict[randKeys[cnt]] = Cell(randKeys[cnt], [C,R], frame, this )
        frame.grid(column=C, row=R, padx=10, pady=10)
        this.grid( padx=10, pady=10)
        C += 1
        cnt+=1
    R += 1
    C = 0


win.bind("<Key>", handle_keypress)
win.mainloop()    
